import time
from concurrent import futures

import cv2
import grpc
import numpy as np

import image_streaming_pb2
import image_streaming_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ImageStreamingServicer(image_streaming_pb2_grpc.ImageStreamingServicer):
    def VideoStart(self, requset_iterator, context):
        count = 1
        for req in requset_iterator:
            frame = np.array(list(req.img)) # (bytes,)
            frame = frame.reshape((req.height, req.width))# (h, w)
            frame = np.array(frame, dtype=np.uint8)
            count += 1

            #display processed video
            cv2.imshow('Image through gRPC', frame)
            cv2.waitKey(1)

            yield image_streaming_pb2.ImgResponse(counts=count)


# Starting the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_streaming_pb2_grpc.add_ImageStreamingServicer_to_server(
        ImageStreamingServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
