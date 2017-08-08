'''
    Simple socket server using threads
'''
 
import socket, sys
 
HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(10)
print('Socket now listening')
 
conn, addr = s.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]))

while True:
    #now keep talking with the client
    #wait to accept a connection - blocking call
    data = conn.recv(1024)
    print(str(len(data)))

    if(len(data) > 0):
        decode = data.decode()
        if ( decode == 'quit'):
            print("quit")
            break

        else:
            print("Server received: ", decode)
            message = "Sending to client back " + str(decode)
            conn.sendall(message.encode())
s.close()
sys.exit()