#include <algorithm>
#include <iostream>
#include <string>
#include <thread>

#include <opencv2/opencv.hpp>
#include <grpc/grpc.h>
#include <grpcpp/channel.h>
#include <grpcpp/client_context.h>
#include <grpcpp/create_channel.h>
#include <grpcpp/security/credentials.h>

#include "src/image_streaming.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::ClientReader;
using grpc::ClientReaderWriter;
using grpc::ClientWriter;
using grpc::Status;

using imagestreaming::ImageStreaming;
using imagestreaming::ImgRequest;
using imagestreaming::ImgResponse;

class ImageStreamingClient {
 public:
  ImageStreamingClient(std::shared_ptr<grpc::Channel> channel)
      : stub_(ImageStreaming::NewStub(channel)) {}

  void VideoStart() {
    ClientContext context;
    ImgRequest img_req;

    // grpc::ServerReaderWriter<W, R>
    std::shared_ptr<ClientReaderWriter<ImgRequest, ImgResponse> > stream(
        stub_->VideoStart(&context));

    std::thread writer([stream, &img_req, this]() {
      cv::Mat frame;

      // Open Camera
      cap.open(0);
      if (!cap.isOpened()) {
        std::cout << ">>>> ERROR: Unable to open camera" << std::endl;
        return;
      }

      while (true) {
        cap.read(frame);

        if (frame.empty()) {
          std::cout << "ERROR! blank frame grabbed" << std::endl;
          break;
        }

        // Get the width, height of image
        int height = frame.rows;
        int width = frame.cols;
        int channel = frame.channels();

        // Image encode
        std::vector<uchar> buf;
        cv::imencode(".jpg", frame, buf);
        // Change to string
        std::string str_encode(buf.begin(), buf.end());

        img_req.set_img(str_encode);
        img_req.set_width(width);
        img_req.set_height(height);
        img_req.set_channel(channel);
        stream->Write(img_req);
      }
      stream->WritesDone();
    });

    ImgResponse res;
    while (stream->Read(&res)) {
      std::cout << "Receive frame: " << res.counts() <<  std::endl;
    }

    writer.join();
    Status status = stream->Finish();
    if (!status.ok()) {
        std::cout << "VideoStart rpc failed." << std::endl;
    }

    cap.release();
  }

 private:
  std::unique_ptr<ImageStreaming::Stub> stub_;
  cv::VideoCapture cap;
};


int main(int argc, char** argv) {
  ImageStreamingClient image_stream(
      grpc::CreateChannel("localhost:50051",
                          grpc::InsecureChannelCredentials())
  );

  std::cout << "-------------- VideoStart --------------" << std::endl;
  image_stream.VideoStart();

  return 0;
}
