from concurrent import futures

import grpc

import route_guide_pb2
import route_guide_pb2_grpc
import route_guide_resources


def get_feature(feature_db, point):
    """Returns Feature at given location or None."""
    for feature in feature_db:
        if feature.location == point:
            return feature
    return None


class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    """Provides methods that implement the functionality of RouteGuide server."""

    def __init__(self):
        self.db = route_guide_resources.read_route_guide_database()

    # Simple RPC
    def GetFeature(self, request, context):
        feature = get_feature(self.db, request)
        if feature is None:
            return route_guide_pb2.Feature(name="", location=request)
        return feature


# Starting the server
def serve():
    # ThreadPoolExectuor 執行 thread 層級的非同步任務
    # ProcessPoolExecutor 執行 process 層級的非同步任務
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
