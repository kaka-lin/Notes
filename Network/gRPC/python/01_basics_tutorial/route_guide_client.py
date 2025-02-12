import grpc

import route_guide_pb2
import route_guide_pb2_grpc


def guide_get_one_feature(stub, point):
    feature = stub.GetFeature(point)

    if not feature.location:
        print("Server returned imcomplete feature")
        return

    if feature.name:
        print("Feature called {} at {}".format(feature.name, feature.location))
    else:
        print("Found no feature at {}".format(feature.location))

def guide_get_feature(stub):
    guide_get_one_feature(
        stub, route_guide_pb2.Point(
            latitude=409146138, longitude=-746188906))
    guide_get_one_feature(
        stub, route_guide_pb2.Point(
            latitude=0, longitude=0))


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    # Creating a stub
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        print("-------------- GetFeature --------------")
        guide_get_feature(stub)


if __name__ == "__main__":
    run()
