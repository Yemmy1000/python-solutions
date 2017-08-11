import socket

ip = input("Input IP: ")
port = int(input("Input PORT: "))
s = socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip, port)):
    print ("Port", port, "is closed")
else:
    print ("Port", port, "is open")
