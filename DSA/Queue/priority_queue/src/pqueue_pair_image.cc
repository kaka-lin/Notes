#include <iostream>
#include <queue>
#include <vector>
#include <mutex>
#include <thread>
#include <unistd.h>

#include <opencv2/opencv.hpp>

typedef std::pair<int, cv::Mat> ImagePair;
// custom compare func
class PairComp {
 public:
  // 由小到大排序
  bool operator()(const ImagePair& n1, const ImagePair& n2) const {
    //因為優先出列判定為!cmp，所以反向定義實現最小值優先
    if (n1.first == n2.first) {
      return (n1.first > n2.first);
    }

    return n1.first > n2.first;;
  }
};

std::mutex mtx_queue_show;
std::priority_queue<ImagePair, std::vector<ImagePair>, PairComp> queue_show;
// std::queue<ImagePair> queue_show;

void read_frame() {
  cv::VideoCapture cap;
  if (cap.open(0)) {
    std::cout << ">>>> ERROR: Unable to open camera"
              << std::endl;
  }

  int input_img_idx = 0;
  while (true) {
    // because cv::Mat is shallow copy
    // so we create new cv::Mat every times
    // or we can use .clone()
    cv::Mat img;
    cap.read(img);
    if (img.empty()) {
      std::cout << "ERROR! blank frame grabbed" << std::endl;
      break;
    }

    mtx_queue_show.lock();
    queue_show.push(std::make_pair(input_img_idx++, img));
    mtx_queue_show.unlock();
  }

  cap.release();
}

void display_frame() {
  cv::Mat frame;
  int output_img_idx = 0;

  while (true) {
    mtx_queue_show.lock();
    if (queue_show.empty()) {
      mtx_queue_show.unlock();
      usleep(10);
    } else if (output_img_idx == queue_show.top().first) {
      frame = queue_show.top().second;
      output_img_idx++;
      queue_show.pop();
      mtx_queue_show.unlock();

      cv::imshow("ADAS Detection@ZU19EG DPU", frame);
      if (cv::waitKey(1) == 'q') {
        break;
      }
    }
  }
}

int main(int argc, char** argv) {
  std::vector<std::thread> threads_list;

  threads_list.push_back(std::thread(read_frame));
  threads_list.push_back(std::thread(display_frame));

  for (auto& thread : threads_list) {
    thread.join();
  }

  return 0;
}
