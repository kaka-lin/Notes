#!/bin/bash

# Method 1
XSOCK=/tmp/.X11-unix
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

# Methods 2: without --network=host

# XSOCK=/tmp/.X11-unix
# XAUTH=/tmp/.docker.xauth
# touch $XAUTH
# xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | sudo xauth -f $XAUTH nmerge -
# sudo chmod 777 $XAUTH
# X11PORT=`echo $DISPLAY | sed 's/^[^:]*:\([^\.]\+\).*/\1/'`
# TCPPORT=`expr 6000 + $X11PORT`
# DISPLAY=`echo $DISPLAY | sed 's/^[^:]*\(.*\)/172.17.0.1\1/'`

# if [ ! -f $XAUTH ]
# then
#     xauth_list=$(xauth nlist $DISPLAY | sed -e 's/^..../ffff/')
#     if [ ! -z "$xauth_list" ]
#     then
#         echo $xauth_list | sudo xauth -f $XAUTH nmerge -
#     else
#         touch $XAUTH
#     fi
#     chmod a+r $XAUTH
# fi

# docker run \
#     -it \
#     --gpus all \
#     -e DISPLAY=$DISPLAY \
#     -e QT_X11_NO_MITSHM=1 \
#     -e XAUTHORITY=$XAUTH \
#     --volume=$XSOCK:$XSOCK \
#     --volume=$XAUTH:$XAUTH \
#     --shm-size="20g" \
#     --volume="$PWD:/app/project/" \
#     project2-dev bash
