import socket


if __name__ == "__main__":
    hostname = "example.org"
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address of the `{hostname}` is: {ip_address}")
