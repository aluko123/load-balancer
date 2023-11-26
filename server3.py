"""
server.py to simulate servers that'd accept the connection
"""

import socket

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen(1)
    print(f"Server 3 listening on port {port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        data = client_socket.recv(1024)
        print(f"Received data: {data}")
        client_socket.sendall(b"Hello from Server 3!")
        client_socket.close()

if __name__ == "__main__":
    start_server(8003)