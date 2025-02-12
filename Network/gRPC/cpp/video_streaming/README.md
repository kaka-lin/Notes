# gRPC Video Streaming (C++)

## Prepare

### Generating client and server code

```bash
$ protoc -I ./protos --grpc_out=./src --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ./protos/image_streaming.proto
$ protoc -I ./protos --cpp_out=./src ./protos/image_streaming.proto
```

## Get Started

Build the client and server:

```bash
$ chmod +x cmake-build.sh
$ ./cmake-build.sh
```

Run the server:

```bash
$ ./image_streaming_server
```

From a different terminal, run the client:

```bash
$ ./image_streaming_client
```
