# CAN / CAN bus

控制器區域網路 (Controller Area Network, 簡稱 CAN 或 CAN bus)是一種網路，其特點是允許網路上的多個微控制器或設備直接互相通訊，網路上不需要主機(Host)控制通訊，並且提供高安全等級及有效率的即時控制。

## SocketCAN

由於系統將 CAN 裝置作為網路裝置進行管理，因此在 CAN 匯流排應用開發方面， `Linux 提供了 SocketCAN 介面`，使得 CAN 匯流排通訊近似於和乙太網的通訊，應用程式開發介面 更加通用， 也更加靈活。

[SocketCAN](https://docs.kernel.org/networking/can.html) provides several CAN interface types:
  - virtual interfaces like `vcan0`
  - Native (real hardware) interfaces like `can0`
  - SLCAN based interfaces like `slcan0`

If you then want to send/receive data on the CAN interface, you should install [can-utils](https://github.com/linux-can/can-utils), as below:

```sh
$ sudo apt install can-utils
```

其他 command 請看: [socketcan.sh](./socketcan.sh)

## Develop CAN applications with Python

- [python-can](https://github.com/hardbyte/python-can)

## Utils/Example

- [CanBus Tool](https://github.com/kaka-lin/canbus-tool)

## Reference

- [CAN - 成大資工Wiki](http://wiki.csie.ncku.edu.tw/embedded/CAN)
- [SocketCAN, Wiki](https://en.wikipedia.org/wiki/SocketCAN)
