import socket
import pyodbc
import time
def check_emerg(id):
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 10.0};Server=127.0.0.1;Database=Store;username=sa;password=1234;Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("select emerg from signal where id = ?;",str(id))
    for row in cursor:
        return row.emerg

def stop_emerg(id):
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 10.0};Server=127.0.0.1;Database=Store;username=sa;password=1234;Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("update signal set emerg = '-1' where id = ? ;",str(id))
    conn.commit()

def check_manual(id):
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 10.0};Server=127.0.0.1;Database=Store;username=sa;password=1234;Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("select * from signal where id = ?;",str(id))
    for row in cursor:
        return row.manual,row.t0,row.t1,row.t2,row.t3

def server_program():

    emergbit="emerg"
    manualbit="manual"
    mbit=0
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket() 
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()
    id = conn.recv(1024).decode()
    print(id)
    
    while True:
        
        sigval = check_emerg(id)
        
        if sigval == 0 or sigval == 1 or sigval == 2 or sigval == 3:
            conn.send(emergbit.encode())
            conn.send(str(sigval).encode())
            data = conn.recv(1024).decode()
            print("Emergency Mode for 20 sec!!")
            time.sleep(10)
            stop_emerg(id)

        sigval2,t0,t1,t2,t3 = check_manual(id)
        print(sigval,sigval2,t0,t1,t2,t3)
        
        time.sleep(5)
        
        if sigval2 == 1 and mbit == 0:
            conn.send(manualbit.encode())
            time.sleep(0.5)
            conn.send(str(sigval2).encode())
            time.sleep(0.5)
            conn.send(str(t0).encode())
            time.sleep(0.5)
            conn.send(str(t1).encode())
            time.sleep(0.5)
            conn.send(str(t2).encode())
            time.sleep(0.5)
            conn.send(str(t3).encode())
            mbit=1

        if sigval2 == 0 and mbit == 1:
            conn.send(manualbit.encode())
            time.sleep(0.5)
            conn.send(str(sigval2).encode())
            time.sleep(0.5)
            conn.send(str(0).encode())
            time.sleep(0.5)
            conn.send(str(0).encode())
            time.sleep(0.5)
            conn.send(str(0).encode())
            time.sleep(0.5)
            conn.send(str(0).encode())
            mbit=0
            
    conn.close()

if __name__ == '__main__':
    server_program()
