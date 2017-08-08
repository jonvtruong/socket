import socket, sys

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
HOST = socket.gethostname()                           
PORT = 8888

# connection to hostname on the port.
s.connect((HOST, PORT))                               

# Receive no more than 1024 bytes
message = input("Input: ")

while True:
    s.sendall(message.encode())
    tm = s.recv(1024)
    print("Client received: " + str(tm.decode()))

    if(message == 'quit'):
        break
    message = input("Input: ")                                     

s.close()
sys.exit()