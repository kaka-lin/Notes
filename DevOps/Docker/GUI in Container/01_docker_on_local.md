# Running the container with GUI application as an X client on the local machine

- [Ubuntu](#ubuntu)
- [MacOS](#macos)

## Ubuntu

1. `xhost` 開放權限

    ```bash
    # xhost +local:
    $ xhost +local:docker
    ```

2. 將 `/tmp/.X11-unix` 共享到容器中

    docker run add the command as below:
    ```bash
    --volume="/tmp/.X11-unix:/tmp/.X11-unix"
    ```

3. For Qt Applications (Option)

    Stops Qt form using the MIT-SHM X11 extension.

    docker run add the command as below:
    ```bash
    -e QT_X11_NO_MITSHM=1
    ```

#### Example 1:

A Ubuntu container

```bash
$ docker run --rm -it \
    -e DISPLAY=$DISPLAY \
    -e QT_X11_NO_MITSHM=1 \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    ubuntu:18.04
```

In Container:

```bash
$ apt update && apt install -y x11-apps mesa-utils
```

and run `xclock`, `xeyes`, and `glxgears` for testing.

#### Example 2: A Qt application

Please see [qt-template](https://github.com/kaka-lin/qt-template/tree/master/docker).


## MacOS

Need to install `xquartz` and `socat`

```bash
$ brew install --cask xquartz
$ brew install socat
```

1. `xhost` 開放權限

    ```bash
    $ xhost +localhost
    ```

2. 將 `/tmp/.X11-unix` 共享到容器中

    docker run add the command as below:
    ```bash
    --volume="/tmp/.X11-unix:/tmp/.X11-unix"
    ```

    - /tmp/.X11-unix 是什麼: [請看這](#what-is-tmpx11-unix)

3. 轉發 X11 socket

    Creating a bridge between a network socket with a TCP listener on port 6000 (the default port of the X window system) and the X window server on my OS X host.

   ```bash
   $ socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
   ```

4. For Qt Applications (Option)

    - Stops Qt form using the MIT-SHM X11 extension.

        docker run add the command as below:
        ```bash
        -e QT_X11_NO_MITSHM=1
        ```
    -  Failed to create vertex shader

        QGLXContext: Failed to create dummy context
        ```bash
        -e QT_QUICK_BACKEND=software
        ```

Example 1:

A Ubuntu container

```bash
$ docker run --rm -it \
    -e DISPLAY=host.docker.internal:0 \
    -e QT_X11_NO_MITSHM=1 \
    -e QT_QUICK_BACKEND=software \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    ubuntu:18.04
```

In Container:

```bash
$ apt update && apt install -y x11-apps mesa-utils
```

and run `xclock`, `xeyes`, and `glxgears` for testing.

Example 2: A Qt application

Please see [qt-template](https://github.com/kaka-lin/qt-template/tree/master/docker)

## what is /tmp/.X11-unix

X11 Server 需要有一個途徑來跟 X11 Client來進行溝通。在網路上他們可以通過 `TCP/IP Socket` 來實現溝通，而在本機上他們通過一個 `Unix-domain socket` 來溝通。

`Unix-domain socket` 其實跟 `TCP/IP socket` 很類似，只不過他指向的是一個`文件路徑`，而且無需通過網卡進行轉發，因此相對來說更安全，更快些。

而 `/tmp/.X11-unix` 其實就是存放這些 `Unix-domain Socket` 的地方。

一般来说 `/tmp/.X11-unix` 下面只會有一個 `Unix-domain Socket`(因為一般只有一個 X Server 在運行)，但若系統同時運行多個 X Server，也可能會有多個 `Unix Domain Socket` 出現的情況。

```bash
$ ls -l /tmp/.X11-unix
```
