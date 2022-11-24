import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.connect((host, port))

    data = input(" -> ")
    client_socket.sendto(data.encode(), (host, port))
    

    
if __name__ == "__main__":
    client_program()