#!/bin/bash

# socketcan setup
sudo ip link set can0 type can bitrate 500000
sudo ip link set can0 up

sudo ip link set can0 down

# socketcan send
cansend can0 123#DEADBEEF

# socketcan dump
candump can0

# show detail info
sudo ip -details link show can0
