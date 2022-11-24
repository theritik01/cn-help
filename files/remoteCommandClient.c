import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        data = input(" -> ")
        client_socket.send(data.encode())
        client_socket.close()
    

if __name__ == "__main__":
    client_program()