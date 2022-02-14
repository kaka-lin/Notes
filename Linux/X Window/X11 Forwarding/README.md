# X11 Forwarding

SSH 提供了 `X11 Forwarding` 來簡單的實現，可以通過一個支持 X Server 的 SSH 客戶端，連接到遠端的 Linux Server。

## Using

We can running `xclock`, `xeyes`, and `glxgears` for testing.

- [Ubuntu: X11 forwarding to view GUI applications running on server hosts](https://fabianlee.org/2018/10/14/ubuntu-x11-forwarding-to-view-gui-applications-running-on-server-hosts/)
- [macOS 使用 XQuartz 支援 X11 實現 Linux 圖形化介面顯示](https://www.gushiciku.cn/pl/pwWt/zh-tw)

    * Note: 不需要改 `DISPLAY` 的值，用 `XQuartz` 設置好的就可以。
    * `OpenGL on Mac OS`: OpenGL is not enabled in XQuartz by default.

        If you are running XQuartz 2.8 or later, do the following one-time configuration:

        ```bash
        $ defaults write org.xquartz.X11 enable_iglx -bool true
        ```

## Reference

- [Setting up X11 and OpenGL on your laptop/desktop ](https://twiki.nevis.columbia.edu/twiki/bin/view/Main/X11OnLaptops)
