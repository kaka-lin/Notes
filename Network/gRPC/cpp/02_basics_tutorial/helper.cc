#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <sstream>

#include "route_guide.grpc.pb.h"

#define MAXPATHLEN 256

namespace routeguide {

std::string GetDbFileContent(int argc, char** argv) {
  std::string db_path;
  std::string arg_str("--db_path");
  char cwd[MAXPATHLEN];
  std::string path;
  size_t pos;

  if (argc > 1) {
    std::string argv_1 = argv[1];
    size_t start_position = argv_1.find(arg_str);
    if (start_position != std::string::npos) {
      start_position += arg_str.size();
      if (argc > 2) {
        db_path = argv[2];
      } else if (argv_1[start_position] == ' ' || argv_1[start_position] == '=') {
        db_path = argv_1.substr(start_position + 1);
      }
    }
  } else if (getcwd(cwd, sizeof(cwd)) != NULL) {
    printf("Current working dir: %s\n", cwd);
    path = std::string(cwd);
    pos = path.find("build");
    db_path = path.substr(0, pos) + "route_guide_db.json";
  } else {
    db_path = "route_guide_db.json";
  }

  std::ifstream db_file(db_path);
  if (!db_file.is_open()) {
    std::cout << "Failed to open " << db_path << std::endl;
    return "";
  }
  std::stringstream db;
  db << db_file.rdbuf();
  return db.str();
}

// A simple parser for the json db file.
// It requires the db file to have the exact form of
// [{"location": { "latitude": 123, "longitude": 456}, "name":
// "the name can be empty" }, { ... } ...
// The spaces will be stripped.
class Parser {
 public:
  explicit Parser(const std::string& db) : db_(db) {
    // Remove all spaces.
    db_.erase(std::remove_if(db_.begin(), db_.end(), isspace), db_.end());
    if (!Match("[")) {
      SetFailedAndReturnFalse();
    }
  }

  bool Finished() { return current_ >= db_.size(); }

  bool TryParseOne(Feature* feature) {
    if (failed_ || Finished() || !Match("{")) {
      return SetFailedAndReturnFalse();
    }
    if (!Match(location_) || !Match("{") || !Match(latitude_)) {
      return SetFailedAndReturnFalse();
    }
    long temp = 0;
    ReadLong(&temp);
    feature->mutable_location()->set_latitude(temp);
    if (!Match(",") || !Match(longitude_)) {
      return SetFailedAndReturnFalse();
    }
    ReadLong(&temp);
    feature->mutable_location()->set_longitude(temp);
    if (!Match("},") || !Match(name_) || !Match("\"")) {
      return SetFailedAndReturnFalse();
    }
    size_t name_start = current_;
    while (current_ != db_.size() && db_[current_++] != '"') {
    }
    if (current_ == db_.size()) {
      return SetFailedAndReturnFalse();
    }
    feature->set_name(db_.substr(name_start, current_ - name_start - 1));
    if (!Match("},")) {
      if (db_[current_ - 1] == ']' && current_ == db_.size()) {
        return true;
      }
      return SetFailedAndReturnFalse();
    }
    return true;
  }

 private:
  bool SetFailedAndReturnFalse() {
    failed_ = true;
    return false;
  }

  bool Match(const std::string& prefix) {
    bool eq = db_.substr(current_, prefix.size()) == prefix;
    current_ += prefix.size();
    return eq;
  }

  void ReadLong(long* l) {
    size_t start = current_;
    while (current_ != db_.size() && db_[current_] != ',' &&
           db_[current_] != '}') {
      current_++;
    }
    // It will throw an exception if fails.
    *l = std::stol(db_.substr(start, current_ - start));
  }

  bool failed_ = false;
  std::string db_;
  size_t current_ = 0;
  const std::string location_ = "\"location\":";
  const std::string latitude_ = "\"latitude\":";
  const std::string longitude_ = "\"longitude\":";
  const std::string name_ = "\"name\":";
};

void ParseDb(const std::string& db, std::vector<Feature>* feature_list) {
  feature_list->clear();

  std::string db_content(db);
  db_content.erase(
      std::remove_if(db_content.begin(), db_content.end(), isspace),
      db_content.end());

  Parser parser(db_content);
  Feature feature;

  while (!parser.Finished()) {
    feature_list->push_back(Feature());
    if (!parser.TryParseOne(&feature_list->back())) {
      std::cout << "Error parsing the db file";
      feature_list->clear();
      break;
    }
  }

  // for (Feature& f : *feature_list) {
  //   // element is a reference to the element in the vector
  //   std::cout << f.name() << "\n";
  // }

  std::cout << "DB parsed, loaded " << feature_list->size() << " features."
            << std::endl;
}

} // namespace routeguide
