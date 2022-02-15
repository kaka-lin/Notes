# Running the GUI application in a Docker container on a remote machine via `SSH`.

![](images/mac_gui_docker_ssh.png)

- [Method 1](#method-1)
- [Method 2](#method-2-without---net-host)

## Method 1

1. xhost開啟權限

   X server (SSH client) side
   ```bash
   $ xhost +
   ```

2. 不需要 `/tmp/.X11-unix`

   因為 `/tmp/.X11-unix` 是用在本機之間的溝通，詳細請看 [what is /tmp/.X11-unix](https://github.com/kaka-lin/Notes/blob/master/DevOps/Docker/GUI%20in%20Container/01_docker_on_local.md#what-is-tmpx11-unix)

3. Container 的網路設定和實體主機使用相同的網路設定

    ```
    $ --network=host
    ```

4. `X11 connection rejected because of wrong authentication`

    使用 X11 Forwarding 時，會隨機產生一個授權的 cookie，存放在 SSH Server (remote machine, X11 Client) 的 `~/.Xauthority` 文件中。這個 cookie 會在每次 X11 Clinet 發送數據時用到。

    當我們使用了 `--network=host` 參數後，容器中的 X11 Clinet (X Application) 將直接通過 `TCP/IP` 與外部通訊。然而容器內並沒有這個授權文件，因此我們需要將它 mount 進容器內，如下:

    ```
    -v $HOME/.Xauthority:/root/.Xauthority
    ```

完整的 `Command` 如下所示:

```basd
XSOCK=/tmp/.X11-unix # root path
XAUTH=/root/.Xauthority

docker run \
  -it \
  --gpus all \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -e XAUTHORITY=$XAUTH \
  -v $XSOCK:$XSOCK \
  -v $HOME/.Xauthority:$XAUTH \
  --shm-size="20g" \
  --volume="$PWD:/app/project/" \
  --network=host \
  project2-dev bash
```

You can see this repo: [Sensor Fusion Exercises](https://github.com/kaka-lin/nd013-c2-fusion-exercises) for more detail and using it.

## Method 2: without "--net host"

- Reference: [Run X application in a Docker container reliably on a server connected via SSH without "--net host"](https://stackoverflow.com/questions/48235040/run-x-application-in-a-docker-container-reliably-on-a-server-connected-via-ssh-w)

When you are connecting to a computer with SSH and using X11 forwarding, `/tmp/.X11-unix` is not used for the X communication.

Any X application rather uses the hostname in `$DISPLAY`, typically `localhost` and connects using `TCP`. This is then tunneled back to the SSH client. *When using "--net host" for the Docker, "localhost" will be the same for the Docker container as for the Docker host, and therefore it will work fine.*

When not specifying `--net host`, the Docker is using the default bridge network mode. This means that `localhost` means something else inside the container than for the host, and X applications inside the container will not be able to see the X server by referring to `localhost`. So in order to solve this, one would have to replace `localhost` with the actual IP-address of the host. This is usually `172.17.0.1` or similar. `Check "ip addr" for the "docker0" interface`.

This can be done with a sed replacement:

```bash
DISPLAY=`echo $DISPLAY | sed 's/^[^:]*\(.*\)/172.17.0.1\1/'`
```

Additionally, the SSH server is commonly not configured to accept remote connections to this X11 tunnel. This must then be changed by editing /etc/ssh/sshd_config (at least in Debian) and setting:

```
X11UseLocalhost no
```
and then restart the SSH server, and re-login to the server with "ssh -X".

If any firewall is running on the Docker host, the TCP port associated with the X11-tunnel must be opened. The port number is the number between the : and the . in $DISPLAY added to 6000.

To get the TCP port number, you can run:

```bash
X11PORT=`echo $DISPLAY | sed 's/^[^:]*:\([^\.]\+\).*/\1/'`
TCPPORT=`expr 6000 + $X11PORT`
```

The next step is to make a X authentication file with proper permissions and mount this to a volume for the container to use. Here is an example of a run command doing just this:

```bash
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
touch $XAUTH
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

# docker run's command
-e XAUTHORITY=$XAUTH
```

[Option] Then, open up this port for the Docker containers in the 172.17.0.0 subnet:

If using ufw as firewall
```
ufw allow from 172.17.0.0/16 to any port $TCPPORT proto tcp
```

All the commands together can be put into a script:

```bash
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
touch $XAUTH
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | sudo xauth -f $XAUTH nmerge -
sudo chmod 777 $XAUTH
X11PORT=`echo $DISPLAY | sed 's/^[^:]*:\([^\.]\+\).*/\1/'`
TCPPORT=`expr 6000 + $X11PORT`
DISPLAY=`echo $DISPLAY | sed 's/^[^:]*\(.*\)/172.17.0.1\1/'`
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -e XAUTHORITY=$XAUTH \
  -v $XAUTH:$XAUTH \
  ubuntu:18.04
```

In container

```bash
$ apt update && apt install x11-apps mesa-utils
```

and run `xclock`, `xeyes`, and `glxgears` for testing.
