import cv2
import grpc
import numpy as np

import image_streaming_pb2
import image_streaming_pb2_grpc


def video_thread():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()

        if ret:
            frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_CUBIC)
        else:
            print("Camera not ready!")
            frame = np.zeros((480, 640, 1), dtype=np.uint8)

        if frame.ndim == 2:
            h, w = frame.shape
            channel = 1
        else:
            h, w, channel = frame.shape

        frame = bytes(frame)

        yield image_streaming_pb2.ImgRequest(img=frame, width=w, height=h, channel=channel)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = image_streaming_pb2_grpc.ImageStreamingStub(channel)

        for res in stub.VideoStart(video_thread()):
            print("Frame receive count: {}".format(res.counts))


if __name__ == "__main__":
    run()
