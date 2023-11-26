'''
load balancer that simulates performing switching between different servers
using python socket library and threading using Round Robin Scheduler 

'''
import socket
import threading

#create a list of host and ports listening on for server request
servers = [("localhost", 8001), ("localhost", 8002), ("localhost", 8003)]
curr_server = 0

def handle_client(client_socket):
    
    #retreive current available server
    global curr_server
    host, port = servers[curr_server]

    #handle client request in socket stream
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.connect((host, port))
        data = client_socket.recv(1024)
        server_socket.sendall(data)
        response = server_socket.recv(1024)
        client_socket.sendall(response)

    #rr function to determine free server
    curr_server = (curr_server + 1) % len(servers)

#begin balancer
def start():
    bal_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bal_socket.bind(("localhost", 9000)) #create the load balancer to listen on a different port
    bal_socket.listen(5)
    print("Load Balancer listening on port 9000")

    #create thread
    while True:
        client_socket, addr = bal_socket.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start()