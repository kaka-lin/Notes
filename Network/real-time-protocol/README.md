# 即時影音串流協定 (Real-time video streaming protocol)

這類協定主要用於影音串流，確保低延遲傳輸。

- RTMP (Real-Time Messaging Protocol)
  - 主要用於 Flash 時代的影音直播，基於 TCP，適合高畫質影音但延遲較高。
  - 目前多數直播平台 (如 YouTube、Twitch) 仍支援 RTMP，但逐漸被 WebRTC 取代。

- RTSP (Real-Time Streaming Protocol)
    - 主要用於控制媒體串流（如監視器影像），通常搭配 RTP/RTCP 進行實際影音傳輸。
    - 允許播放、暫停、停止等控制操作，應用於安防監控、IP Camera。

- RTP (Real-time Transport Protocol)
    - 主要用於即時影音數據傳輸，通常與 RTSP、SIP 搭配使用。
    - 基於 UDP，可與 RTCP (Real-time Transport Control Protocol) 搭配進行網路品質監測。

- WebRTC (Web Real-Time Communication)
    - 低延遲 P2P 視訊通訊協定，適用於視訊會議、線上語音、多人通話。
    - 基於 UDP (SRTP) 傳輸，支援 STUN/TURN 進行 NAT 穿透。
