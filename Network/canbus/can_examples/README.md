# CanBus Examples

This is example C code for SocketCAN on Linux.

Detail description please see [description.md](./description.md).

## Usage

### 0. Setup your CAN

Please setup your CAN devices. As SocketCAN for example:

```sh
# socketcan setup
$ sudo ip link set can0 type can bitrate 500000
$ sudo ip link set can0 up
```

### 1. Build

```bahs
$ ./cmake-build.sh
```

### 2. Run

Open two terminals.

- The first terminal

    ```bash
    $ ./build/receive
    ```

- The second terminal

    ```bash
    $ ./build/transmit
    ```

Reslut:

```sh
user@server:~/can_examples $ ./build/transmit
```

```sh
user@server:~/can_examples $ ./build/receive
0x123 [4] DE AD BE 11
```


### 3. Clean

```bash
$ ./clean.sh
```
