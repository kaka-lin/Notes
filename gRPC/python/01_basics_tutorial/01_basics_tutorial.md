# gRPC Basics tutorial

A basic tutorial introduction to gRPC in Python

1. Define a service in a .proto file.
2. Generate server and client code using the protocol buffer compiler.
3. Use the Python gRPC API to write a simple client and server for your service.


## 1. Defining the service

Define the `*.proto` file that includes the `gRPC service` and the `method request and response types` using [protocol buffer](https://developers.google.com/protocol-buffers/docs/overview)

```protobuf
// gRPC service
service RouteGuide {
    // Obtains the feature at a given position.
    rpc GetFeature(Point) returns (Feature) {}
}

// protocol buffer message type
// for all the req and res types
message Point {
    int32 latitude = 1;
    int32 longitude = 2;
}
```

## 2. Generating client and server code

Now, we can generate the gRPC client and server interfaces from `*.proto` fuile

```bash
$ python3 -m grpc_tools.protoc \
    -I <the path of proto fule> \
    --python_out=<output file path>\
    --grpc_python_out=<grpc output file path> \
    <proto file>
```

The would generate two code files, `*_pb2.py` and `*_pb2_grpc.py`.
Assume have *helloWorld* service

- `*_pb2.py`:
    classes for the `messages defined` in *.proto
- `*_pb2_grpc.py`:
    - classes for the `service defined` in *.proto
        - `helloWorldStub`: clients to invoke *helloWorld* RPCs
        - `helloWorldServicer`: definces the interface for implementations of the *helloWorld* service
    - a function for the sercvice defined in *.proto
        - `add_helloWorldServicer_to_server`: adds a `helloWorldServicer` to a `grpc.Server`

### Example:

```bash
python3 -m grpc_tools.protoc \
    -I . \
    --python_out=.\
    --grpc_python_out=. \
    route_guide.proto
```

Then generate two code files, `route_guide_pb2.py` and `route_guide_pb2_grpc.py`

- `route_guide_pb2.py`:
    classes for the `messages defined` in route_guide.proto
- `route_guide_pb2_grpc.py`:
    - classes for the `service defined` in route_guide.proto
        - `RouteGuideStub`: clients to invoke RouteGuide RPCs
        - `RouteGuideServicer`: definces the interface for implementations of the service
    - a function for the sercvice defined in route_guide.proto
        - `add_RouteGuideServicer_to_server`: adds a `RouteGuideServicer` to a `grpc.Server`

## 3. Creating the server

Creating and running a `RouteGuide` server breaks down into two works items:

- Implementing the server interface generated from our service definition with function that perform the *"work"* of the service.
- Running a gRPC server to listen for requests from clients and transmit responses.

### 3-1. Implementing server

*Using route_guide as an example.*

1. Creating `route_guide_server.py`, then create a `RouteGuideServicer` class that inherited from `route_guide_pb2_grpc.RouteGuideServicer`.

    ```python
    # RouteGuideServicer provides an implementation of the methods of the RouteGuide service.
    class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    ```

    `RouteGuideServicer` implements all the `RouteGuide` service methods

2. Implementing all service methods defined in the `RouteGuide`

    Detail content please see the source code.

### 3-2. Starting the server

Once you have implemented all the `RouteGuide` methods, next step is to start up a gRPC server so that client can actually use your service.

`route_guide_server.py`

```python
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server)
    server.add_insecure_port('[::]:50051') # Opens an insecure port for accepting RPCs.
    server.start() # non-blocking
    server.wait_for_termination()
```

## 4. Creating the client

*Using route_guide as an example.*
*Creating route_guide_client.py*

### 4-1. Creating a stub (client)

To call service methods, we first need to create a *stub*.

We instantiate the `RouteGuideStub` class of the `route_guide_pb2_grpc module`, generated from our *.proto.

```python
channel = grpc.insecure_channel('localhost:50051')
stub = route_guide_pb2_grpc.RouteGuideStub(channel)
```

### 4-2. Calling service methods

For example:

- Simple RPC

    ```python
    feature = stub.GetFeature(point)
    ```

## 5. Run

Run the server:

```python
$ python3 route_guide_server.py
```

From a different terminal, run the client:

```python
$ python3 route_guide_client.py
```
