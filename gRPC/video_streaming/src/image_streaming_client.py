import cv2
import numpy as np
import grpc

import image_streaming_pb2
import image_streaming_pb2_grpc


def video_thread():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()

        if ret:
            frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_CUBIC)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            #print("Camera not ready!")
            frame = np.zeros((480, 640), dtype=np.uint8)

        h, w = frame.shape
        frame = bytes(frame)

        yield image_streaming_pb2.ImgRequest(img=frame, width=w, height=h, channel=1)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = image_streaming_pb2_grpc.ImageStreamingStub(channel)

        for res in stub.VideoStart(video_thread()):
            print("Frame receive count: {}".format(res.counts))


if __name__ == "__main__":
    run()
