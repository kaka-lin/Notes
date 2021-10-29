#include <algorithm>
#include <iostream> // char
#include <string>

#include <opencv2/opencv.hpp>
#include <grpc/grpc.h>
#include <grpcpp/server.h>
#include <grpcpp/security/server_credentials.h>
#include <grpcpp/server_builder.h>

#include "src/image_streaming.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::ServerReader;
using grpc::ServerReaderWriter;
using grpc::ServerWriter;
using grpc::Status;

using imagestreaming::ImageStreaming;
using imagestreaming::ImgRequest;
using imagestreaming::ImgResponse;

class ImageStreamingImpl final : public ImageStreaming::Service {
 public:
  explicit ImageStreamingImpl() {};

  // grpc::ServerReaderWriter<W, R>
  Status VideoStart(ServerContext* context,
                    ServerReaderWriter<ImgResponse, ImgRequest>* stream) override {

    ImgRequest req;
    ImgResponse res;
    size_t count = 0;

    while (stream->Read(&req)) {
      std::string str_decode = req.img();
      // Image decode
      std::vector<uchar> buf(str_decode.begin(), str_decode.end());
      cv::Mat frame = cv::imdecode(buf, 1);

      // display processed video
      cv::imshow("Image through gRPC", frame);
      cv::waitKey(1);

      count += 1;
      res.set_counts(count);
      stream->Write(res);
    }

    return Status::OK;
  }
};

void RunServer() {
  std::string server_address("0.0.0.0:50051");
  ImageStreamingImpl service;

  ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<Server> server(builder.BuildAndStart());
  std::cout << "Server listening on " << server_address << std::endl;
  server->Wait();
}

int main(int argc, char** argv) {
  RunServer();

  return 0;
}
