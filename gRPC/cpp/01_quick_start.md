# Quick start

This guide gets you started with gRPC in C++ with a simple working example.

## Build the example

The example code is part of the grpc repo source, which you cloned as part of the steps of the previous section.

1. Change to the example's directory

    ```bash
    $ cd examples/cpp/helloworld
    ```

2. Build the example using `cmake`:

    ```bash
    $ mkdir -p build && cd build
    $ cmake -DCMAKE_BUILD_TYPE=Debug ..
    $ make -j8 # or cmake --build .
    ```

## Run the example

1. Run the server:

    ```bash
    $ ./greeter_server
    ```

2. From a different terminal, run the client and see the client output:

    ```bash
    $ ./greeter_client
    ```
