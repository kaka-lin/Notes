# GStreamer

## Open/Show USB Camera

```bash
$ gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! ximagesink
```
