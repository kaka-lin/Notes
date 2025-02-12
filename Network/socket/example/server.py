import socket


def main(host, port):
    # 創建 socket 物件 (AF_INET 表示 IPv4, SOCK_STREAM 表示 TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))  # 綁定 IP 和 Port
    server_socket.listen()  # 開始監聽

    print(f"Server listening on {host}:{port}...")

    conn, addr = server_socket.accept()  # 等待客戶端連接
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)  # 接收數據（最大 1024 bytes）
        if not data:
            break
        print(f"Received: {data.decode()}")
        conn.sendall(data)  # 回傳相同的數據

    conn.close()
    server_socket.close()


if __name__ == "__main__":
    # 設定伺服器的 IP 和 Port
    HOST = '127.0.0.1'
    PORT = 65432

    main(HOST, PORT)
