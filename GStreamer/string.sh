#!/bin/bash

# Open/Show USB Camera
# xvimagesink 效能比 ximagesink 好
gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! xvimagesink

gst-launch-1.0 v4l2src device=/dev/video0 ! \
    video/x-raw, format=YUY2, width=640, height=480, pixel-aspect-ratio=1/1, framerate=30/1 ! \
    videoconvert ! xvimagesink

# Plat mp4 file
gst-launch-1.0 filesrc location=demo.mp4 ! \
    decodebin name=dec ! \
    queue ! \
    videoconvert ! \
    autovideosink dec. ! \
    queue ! \
    audioconvert ! \
    audioresample ! \
    autoaudiosink

# Testing: play YUV422 format
gst-launch-1.0 videotestsrc ! \
    video/x-raw, format=UYVY, width=1280, height=720, framerate=30/1 ! \
    videoconvert ! autovideosink

gst-launch-1.0 videotestsrc ! \
    video/x-raw, format=UYVY, width=1280, height=720, framerate=30/1 ! \
    xvimagesink

# Play YUV422 file (using "video/x-raw") (image)
gst-launch-1.0 filesrc blocksize=108748800 location=test.yuv ! \
    video/x-raw, format=UYVY, width=1280, height=720, framerate=30/1 ! \
    videoconvert ! imagefreeze ! autovideosink

# Play YUV422 file (using "videoparse") (video)
gst-launch-1.0 filesrc location=test.yuv ! \
    videoparse format=GST_VIDEO_FORMAT_UYVY width=1280 height=720 framerate=30/1 ! \
    videoconvert ! autovideosink

gst-launch-1.0 filesrc location=test.yuv ! \
    videoparse format=5 width=1280 height=720 framerate=30/1 ! \
    xvimagesink

# Play YUV422 (using "videoparse")
# sender
gst-launch-1.0 filesrc location=test.yuv ! \
    videoparse width=1280 height=720 framerate=30/1 format=5 ! \
    videoconvert ! appsink
