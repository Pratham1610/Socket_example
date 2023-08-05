import socket
import sys



#creating a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = '192.168.1.13'
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))

#binding socket 
def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host, port))
        print("Socket is binded to port " + str(port))
        s.listen(5)
    except socket.error as err:
        print("socket creation failed with error %s" %(err))
        print("\nRetrying......")
        bind_socket()

#send commands
def send_commands(client):
    while True:
        cmd = input()
        if cmd == 'quit':
            client.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            client.send(str.encode(cmd))
            res = str(client.recv(1024), "utf-8")
            print(res, end="")
        
#accept socket
def accept_socket():
    client, adr = s.accept()
    print("Client Connected succesfully: " + (adr[0]))
    send_commands(client)
    client.close()


def main():
    create_socket()
    bind_socket()
    accept_socket()
    return
    
    
main()