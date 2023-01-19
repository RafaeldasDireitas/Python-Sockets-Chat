import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.56.1"
port = 123

s.bind((host, port))
s.listen(5)
conn, addr = s.accept()

print("User" + " " + host + " " + "has joined")

while True:

    welcomeMessage = "Welcome."
    conn.send(welcomeMessage.encode("utf-8"))

    data = conn.recv(1024).decode()
    print(host + " " + "wrote:" + " " + data)



