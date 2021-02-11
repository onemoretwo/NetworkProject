from socket import *

HOST = '127.0.0.1'   # or 127.0.0.1 or localhost
PORT = 20300
ADDR = (HOST,PORT)
BUFFER = 4096

#create a socket (SRV)
#see python docs for socket for more info

srv = socket(AF_INET,SOCK_STREAM)

#bind socket to address
srv.bind((ADDR))	#double parens create a tuple with one object
srv.listen(1) # maximum queued connections is 1
print("Server is ready")

while True:
    conn,addr = srv.accept() #accepts the connection
    print('...connected by', addr)
     
    height = conn.recv(BUFFER).decode()
    height = int(height) + 1
    conn.send(str(height).encode())

    conn.close()