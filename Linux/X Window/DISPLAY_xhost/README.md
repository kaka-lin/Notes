# DISPLAY and xhost

## DISPLAY

在 Linux/Unix 類操作系統上, `DISPLAY用來設置將圖形顯示到何處`，Default DISPLAY 為 `:0.0`，此設定圖形將顯示在本地視窗上。

DISPLAY 環境變數的格式為: `host:NumA.NumB`

- host: X Server 所在的`主機名或是 IP 位址`，如果host為空則表示 X Server 運行於本機。
- NumA: 為 `displaynumber`。
- NumB: 為 `screennumber`。

在某些機器上，可能有多個顯示設備共享使用同一套輸入設備，例如:

    在一臺PC上連接兩臺CRT顯示器，
    但是它們只共享使用一個鍵盤和一個鼠標。
    這一組顯示設備就擁有一個共同的displaynumber，
    而這組顯示設備中的每個單獨的設備則擁有自己單獨的 screennumber。

## xhost

`xhost 是用來控制 X Server 訪問權限的`，因為 X Server 預設情況下是不允許別的使用者的圖形顯示在當前螢幕上的，假如需要別的使用者的圖形顯示在當前螢幕上，則應以當前登陸的使用者，也就是切換身份前的使用者執行如下命令: `xhost +` 這個命令將答應別的使用者啟動的圖形程式將圖形顯示在當前螢幕上。

- `xhost +`: 使所有的用戶都能訪問 X Server
- `xhost + ip`: 使 IP 上的用戶能訪問 X Server
