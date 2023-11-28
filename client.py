import socket

host = 'localhost'
port = 9000

for i in range(1, 11):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))


    #Send data
    message = "Hello from client. This is message {}".format(i)
    client_socket.send(message.encode('utf-8'))

    #receive data
    data = client_socket.recv(1024)
    print(data.decode('utf-8'))

    client_socket.close()