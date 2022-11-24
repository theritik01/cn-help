import socket
from getmac import get_mac_address as gma

def server_program():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    print(ip)
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(3)
    conn, addr = server_socket.accept()
    print("connection from: " + str(addr))
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        if (data == str(ip)):
            print("sending mac address")
            conn.send(gma().encode())

    conn.close()

if __name__ == '__main__':
    server_program()