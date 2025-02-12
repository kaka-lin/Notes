# gRPC Basics tutorial

A basic tutorial introduction to gRPC in C++.

## 1. Defining the service

Define the `*.proto` file that includes the `gRPC service` and the `method request and response types` using [protocol buffer](https://developers.google.com/protocol-buffers/docs/overview)

```protobuf
// gRPC service
service RouteGuide {
    // A simple gRPC
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

Now, we can generate the gRPC client and server interfaces from `*.proto` file. We do this using the protocol buffer compiler `protoc` with a special gRPC C++ plugin.

```bash
$ protoc -I ./protos --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ./protos/route_guide.proto
$ protoc -I ./protos --cpp_out=. ./protos/route_guide.proto
```

Running this command generates the following files in your current directory:

- `route_guide.pb.h`: the header which declares your generated `message classes`
- `route_guide.pb.cc`: which contains the implementation of your message classes
- `route_guide.grpc.pb.h`: the header which declares your generated `service classes`
- `route_guide.grpc.pb.cc`: which contains the implementation of your service classes

## 3. Creating the server

Creating and running a `RouteGuide` server breaks down into two works items:

- Implementing the server interface generated from our service definition with function that perform the *"work"* of the service.
- Running a gRPC server to listen for requests from clients and transmit responses.

### 3-1. Implementing server

*Using route_guide as an example.*

1. Creating `route_guide_server.cc`, then create a `RouteGuideImpl` class that implements the generated `RouteGuide::Service` interface.

    ```c++
    class RouteGuideImpl final : public RouteGuide::Service {
    ...
    }
    ```

2. Implementing all service methods defined in the `RouteGuide`

    Detail content please see the source code.

### 3-2. Starting the server

Once we’ve implemented all our methods, we also need to start up a gRPC server so that clients can actually use our service. The following snippet shows how we do this for our
`RouteGuide` service:

```c++
void RunServer(const std::string& db_path) {
    std::string server_address("0.0.0.0:50051");
    RouteGuideImpl service(db_path);

    # we build and start our server using a ServerBuilder
    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;
    server->Wait();
}
```

## 4. Creating the client

In this section, we’ll look at creating a C++ client for our `RouteGuide` service.

Creating `route_guide_client.cc`.

### 4-1. Creating a stub (client)

To call service methods, we first need to create a *stub*.

First we need to create a gRPC *channel* for our stub, specifying the server address and port we want to connect to - in our case we’ll use no SSL:

```c++
grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials());
```

Now we can use the channel to create our stub using the `NewStub` method provided in the `RouteGuide` class we generated from our `.proto`.

```c++
public:
    RouteGuideClient(std::shared_ptr<ChannelInterface> channel)
        : stub_(RouteGuide::NewStub(channel)) {
        ...
    }
```

### 4-2. Calling service methods

For example:

- Simple RPC

    ```c++
    Point point;
    Feature feature;
    point = MakePoint(409146138, -746188906);
    GetOneFeature(point, &feature);

    ...

    bool GetOneFeature(const Point& point, Feature* feature) {
        ClientContext context;
        Status status = stub_->GetFeature(&context, point, feature);
        ...
    }
    ```

## 5. Build and Run

Build the client and server:

```bash
$ mkdir -p build && cd build
$ cmake -G Ninja -DCMAKE_BUILD_TYPE=Debug ..
$ cmake --build .

#or
$ chmod +x cmake-build.sh
$ ./cmake-build.sh
```

Run the server:

```bash
$ ./route_guide_server
```

From a different terminal, run the client:

```bash
$ ./route_guide_client
```
