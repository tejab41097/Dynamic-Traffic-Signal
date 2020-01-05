from tkinter import *
import pyodbc

def delete():
    screen.destroy()

def delete2():
    screen2.destroy()
    
def delete3():
    screen3.destroy()
 
def delete4():
    screen4.destroy()
 
def delete5():
    screen5.destroy()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Password Error")
  screen4.geometry("200x120")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete4).pack()
 
def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("200x120")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete5).pack()

def Store_Data():
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 10.0};Server=127.0.0.1;Database=Store;username=sa;password=1234;Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute('insert into signal values(?,4,0,-1,0,0,0,0);',(id))
    conn.commit()
    delete()

def getid():
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 10.0};Server=127.0.0.1;Database=Store;username=sa;password=1234;Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    tid = cursor.execute('select max(id) from signal;').fetchval()
    tid=tid+1
    return str(tid)

def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Configure Signal")
  screen3.geometry("700x500")
  Label(screen3, text = "").pack()

  global id

  id= StringVar()

  Label(screen3, text = "").pack()
  Label(screen3, text = "").pack()
  id = getid()
  Label(screen3, text = " ID: "+id).pack()
  
  Label(screen3, text = "").pack()
  Label(screen3, text = "").pack()
  Label(screen3, text = "").pack()
  Label(screen3, text = "").pack()

  Button(screen3, text = "OK ADD SIGNAL", width = 10, height = 1,fg="green", command = Store_Data).pack()
  Button(screen3, text = "EXIT", command =delete3, fg="red").pack()

def login_verify():
    conn = pyodbc.connect(
         "Driver={SQL Server Native Client 10.0};Server=127.0.0.1;Database=Store;username=sa;password=1234;Trusted_Connection=yes;"
    )
    email = username_verify.get()
    password = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    
    cursor = conn.cursor()
    login = 0
    cursor.execute('select * from auth_table;')
    for row in cursor:
        if email == row.email and password == row.password:
            login = 1
            break
        elif email == row.email and password != row.password:
            login = 2
            break
        else:
            continue
        
    if login == 1:
        login_sucess()
    elif login == 2:
        password_not_recognised()
    else:
        user_not_found()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("500x500")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()
 
  global username_verify
  global password_verify
   
  username_verify = StringVar()
  password_verify = StringVar()
 
  global username_entry1
  global password_entry1
   
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  Button(screen2, text = "EXIT", command =delete2).pack()
   
   
def main():
    
    global screen
    screen = Tk()
    screen.geometry("500x500")
    screen.title("Dynamic Traffic Signal - Configuration")
    Label(text = "Welcome To 1st Setup Of Dynamic Traffic Signal!!", bg = "green", fg="white", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(screen, text = "EXIT", command =delete).pack()
    screen.mainloop()

main()
 

  
