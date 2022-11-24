import socket

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    while True:
        data = server_socket.recv(1024).decode('utf-8')
        print("from connected user: " + data)

    
if __name__ == "__main__":
    server_program()