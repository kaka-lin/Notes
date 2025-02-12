import socket


def main(host, port):
    # 創建 socket 物件 (AF_INET 表示 IPv4, SOCK_STREAM 表示 TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))  # 連接到伺服器

    message = "Hello, Server!"
    client_socket.sendall(message.encode())  # 發送數據
    data = client_socket.recv(1024)  # 接收伺服器回應

    print(f"Received from server: {data.decode()}")

    client_socket.close()


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65432

    main(HOST, PORT)
