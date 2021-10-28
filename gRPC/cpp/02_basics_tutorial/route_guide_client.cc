#include <iostream>
#include <string>

#include "helper.h"

#include <grpc/grpc.h>
#include <grpcpp/channel.h>
#include <grpcpp/client_context.h>
#include <grpcpp/create_channel.h>
#include <grpcpp/security/credentials.h>
#include "route_guide.grpc.pb.h"

using routeguide::Feature;
using routeguide::Point;
using routeguide::RouteGuide;

Point MakePoint(long latitude, long longitude) {
  Point p;
  p.set_latitude(latitude);
  p.set_longitude(longitude);
  return p;
}

class RouteGuideClient {
 public:
  RouteGuideClient(std::shared_ptr<grpc::Channel> channel)
      : stub_(RouteGuide::NewStub(channel)) {}

  void GetFeature() {
    Point point;
    Feature feature;
    point = MakePoint(409146138, -746188906);
    GetOneFeature(point, &feature);
    point = MakePoint(0, 0);
    GetOneFeature(point, &feature);
  }
 private:
  bool GetOneFeature(const Point& point, Feature* feature) {
    grpc::ClientContext context;
    grpc::Status status = stub_->GetFeature(&context, point, feature);
    if (!status.ok()) {
      std::cout << "GetFeature rpc failed." << std::endl;
      return false;
    }
    if (!feature->has_location()) {
      std::cout << "Server returns incomplete feature." << std::endl;
      return false;
    }
    if (feature->name().empty()) {
      std::cout << "Found no feature at "
                << feature->location().latitude() / kCoordFactor_ << ", "
                << feature->location().longitude() / kCoordFactor_ << std::endl;
    } else {
      std::cout << "Found feature called " << feature->name() << " at "
                << feature->location().latitude() / kCoordFactor_ << ", "
                << feature->location().longitude() / kCoordFactor_ << std::endl;
    }
    return true;
  }

  const float kCoordFactor_ = 10000000.0;
  std::unique_ptr<RouteGuide::Stub> stub_;
};


int main(int argc, char** argv) {
  // Except only arg: --db_path=path/to/route_guide_db.json
  std::string db = routeguide::GetDbFileContent(argc, argv);
  RouteGuideClient guide(
      grpc::CreateChannel("localhost:50051",
                          grpc::InsecureChannelCredentials())
  );

  std::cout << "-------------- GetFeature --------------" << std::endl;
  guide.GetFeature();

  return 0;
}
