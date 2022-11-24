import socket
import datetime

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, addr = server_socket.accept()
    print("connection from: " + str(addr))
    
    data = datetime.datetime.now()

    while True:
        conn.send(str(data).encode())

    conn.close()

if __name__ == '__main__':
    server_program()
