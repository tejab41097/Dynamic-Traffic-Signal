import socket
from itertools import islice
import time

def getid():
    with open('Config.txt') as f:
        id = f.readline().strip('\n\r')
    print(id)
    return id

def stop_emerg():
    id,info_no_of_signals,manual,emerg,t0,t1,t2,t3 = 0,0,0,0,0,0,0,0        
    with open('Config.txt') as f:
        id = f.readline().strip('\n\r')
        info_no_of_signals = f.readline().strip('\n\r')
        manual = f.readline().strip('\n\r')
        emerg = f.readline().strip('\n\r')
        t0 = f.readline().strip('\n\r')
        t1 = f.readline().strip('\n\r')
        t2 = f.readline().strip('\n\r')
        t3 = f.readline().strip('\n\r')
        emergstart = f.readline().strip('\n\r')

    file=open("Config.txt", "w")
    file.write(id+"\n")
    file.write(str(info_no_of_signals)+"\n")
    file.write(manual+"\n")
    file.write('-1'+"\n")
    file.write(t0+"\n")
    file.write(t1+"\n")
    file.write(t2+"\n")
    file.write(t3+"\n")
    file.write('0'+"\n")
    file.close()

def check_startemerg():
    start = '0'
    while start != '1' :
        time.sleep(3)
        with open('Config.txt') as f:
            for i,line in enumerate(f):
                if i == 8 :
                    start = line.strip('\n\r')

def update_emerge(sigval):
    with open('Config.txt') as f:
        id = f.readline().strip('\n\r')
        info_no_of_signals = f.readline().strip('\n\r')
        manual = f.readline().strip('\n\r')
        emerg = f.readline().strip('\n\r')
        t0 = f.readline().strip('\n\r')
        t1 = f.readline().strip('\n\r')
        t2 = f.readline().strip('\n\r')
        t3 = f.readline().strip('\n\r')
        emergstart = f.readline().strip('\n\r')
                
    file=open("Config.txt", "w")
    file.write(id+"\n")
    file.write(str(info_no_of_signals)+"\n")
    file.write(manual+"\n")
    file.write(str(sigval)+"\n")
    file.write(t0+"\n")
    file.write(t1+"\n")
    file.write(t2+"\n")
    file.write(t3+"\n")
    file.write('0'+"\n")
    file.close()

def update_manual(sigval,t0,t1,t2,t3):
    with open('Config.txt') as f:
        for i,line in enumerate(f):
            if i==0:
                id = line.strip('\n\r')
            if i==1:
                info_no_of_signals = line.strip('\n\r')
    file=open("Config.txt", "w")
    file.write(id+"\n")
    file.write(str(info_no_of_signals)+"\n")
    file.write(str(sigval)+"\n")
    file.write('-1'+"\n")
    file.write(t0+"\n")
    file.write(t1+"\n")
    file.write(t2+"\n")
    file.write(t3+"\n")
    file.close()

def client_program():
    host = '192.168.43.190'
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    id = getid()
    client_socket.send(id.encode())

    while True:
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        
        if data == "emerg":
            sigval = client_socket.recv(1024).decode()
            update_emerge(sigval)
            check_startemerg()
            client_socket.send('1'.encode())
            print("Emergency Mode ON for 20 sec!! Not accepting any request!!")
            stop_emerg()
            time.sleep(20)

        if data == "manual":
            sigval = client_socket.recv(1024).decode()
            t0 = client_socket.recv(1024).decode()
            t1 = client_socket.recv(1024).decode()
            t2 = client_socket.recv(1024).decode()
            t3 = client_socket.recv(1024).decode()
            update_manual(sigval,t0,t1,t2,t3)

    client_socket.close()

if __name__ == '__main__':
    client_program()
