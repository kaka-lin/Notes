# gRPC Video Streaming

## Prepare

### Generating client and server code

```bash
$ python3 -m grpc_tools.protoc \
    -I ./protos \
    --python_out=./src\
    --grpc_python_out=./src \
    image_streaming.proto
```

## Get Started

#### Run server

```bash
$ python3 image_streaming_server.py
```

#### Run client

```bash
$ python3 image_streaming_client.py
```
