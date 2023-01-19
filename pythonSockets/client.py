import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.56.1"
port = 123

s.connect((host, port))

message = s.recv(1024)
print(message)

while True:

    text = input("Message:" + " ")
    s.sendall(text.encode())

    if (text == "help"):
        print("HELP BRUH")

