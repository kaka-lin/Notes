# Build and Install gRPC and Protocol Buffers

This section explains how to build and install gRPC and Protocol Buffers using `cmake`.

## 1. Setup

Choose a directory to hold locally installed packages. Assumes we installed in `$HOME/.local`.

```bash
$ export GRPC_INSTALL_DIR=$HOME/.local
$ mkdir -p $GRPC_INSTALL_DIR
```

Add the local `bin` folder to your path variable

```bash
$ export PATH="$GRPC_INSTALL_DIR/bin:$PATH"
```

## 2. Install cmake

You need version 3.13 or later of `cmake`

- macOS:

    ```bash
    $ brew install cmake
    ```

- Linux:

    ```bash
    $ sudo apt install -y cmake
    ```

Under Linux, the version of the system-wide `cmake` can often be too old. You can install a more recent version following methods as mentioned: [How do I install the latest version of cmake from the command line?](https://askubuntu.com/questions/355565/how-do-i-install-the-latest-version-of-cmake-from-the-command-line)

For example:

```bash
$ wget -q -O cmake-linux.sh https://github.com/Kitware/CMake/releases/download/v3.19.6/cmake-3.19.6-Linux-x86_64.sh
$ sh cmake-linux.sh -- --skip-license --prefix=$GRPC_INSTALL_DIR
$ rm cmake-linux.sh
```

## 3. Install other required tools

- macOS:

    ```bash
    $ brew install autoconf automake libtool pkg-config
    ```

- Linux:

    ```bash
    $ sudo apt install -y build-essential autoconf libtool pkg-config
    ```

## 4. Install gRPC and Protocol Buffers

### 4-1. Clone the `grpc` repo

Clone the [grpc](https://github.com/grpc/grpc) repo and its submodules:

```bash
$ git clone --recurse-submodules -b v1.41.0 https://github.com/grpc/grpc
```

### 4-2. Build and install gRPC and Protocol Buffers

While not mandatory, gRPC applications usually leverage [Protocol Buffers](https://developers.google.com/protocol-buffers) for service definitions and data serialization, and the example code uses [proto3](https://developers.google.com/protocol-buffers/docs/proto3).

The following commands build and locally install gRPC and Protocol Buffers:

```bash
$ cd grpc
$ mkdir -p cmake/build
$ pushd cmake/build
$ cmake -DgRPC_INSTALL=ON \
      -DgRPC_BUILD_TESTS=OFF \
      -DCMAKE_INSTALL_PREFIX=$GRPC_INSTALL_DIR \
      ../..
$ make -j8
$ sudo make install
$ popd
```

#### More information:

- You can find a completed set of instruction for building gRPC C++ in [Building from source](https://github.com/grpc/grpc/blob/master/BUILDING.md#build-from-source).

- For general instruction on how to add gRPC as a dependency to your C++ project, see [Start using gPRC C++](https://github.com/grpc/grpc/tree/master/src/cpp#to-start-using-grpc-c).
