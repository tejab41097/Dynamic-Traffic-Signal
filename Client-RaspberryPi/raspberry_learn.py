from tkinter import *
import DTS

def delete():
    screen.destroy()

def delete2():
    screen2.destroy()


def Store_Data():
    info_id = id.get()
    file=open("Config.txt", "w")
    file.write(info_id+"\n")
    file.write('4'+"\n")
    file.write('0'+"\n")
    file.write('-1'+"\n")
    file.write('0'+"\n")
    file.write('0'+"\n")
    file.write('0'+"\n")
    file.write('0'+"\n")
    file.write('0'+"\n")
    file.close()
    delete()
    mainobject=DTS.Main_class()
    mainobject.startSignal()

def login_sucess():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Configure Signal")
    screen2.geometry("700x500")
    Label(screen2, text = "").pack()

    global id

    id = StringVar()

    global eid

    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Enter ID You have got from Central Server:").pack()
    eid = Entry(screen2, textvariable = id)
    eid.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()

    Button(screen2, text = "START SIGNAL", width = 10, height = 1,fg="green", command = Store_Data).pack()
    Button(screen2, text = "EXIT", command =delete2, fg="red").pack()

def main():
    
    global screen
    screen = Tk()
    screen.geometry("500x500")
    screen.title("Dynamic Traffic Signal - Configuration")
    Label(text = "Welcome To 1st Setup Of Dynamic Traffic Signal!!", bg = "green", fg="white", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Start Configuration", height = "2", width = "30", command = login_sucess).pack()
    Label(text = "").pack()
    Button(screen, text = "EXIT", command =delete).pack()
    screen.mainloop()

main()
 

  
