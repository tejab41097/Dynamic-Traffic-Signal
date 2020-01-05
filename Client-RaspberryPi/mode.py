import time
import runsignal
import RPi.GPIO as GPIO
import time

class Modechanger:
    
    def check_manual_auto(self):
        
        t0,t1,t2,t3=0,0,0,0
        gettimers = 0
        with open('Config.txt') as f:
            for i,line in enumerate(f):
                if i == 2:
                    bit = line.strip('\n\r')
                    if bit == '1':
                        gettimers = 1
                    elif bit == '0':
                        break
                if i == 4 and gettimers == 1:
                    t0 = int(line.strip('\n\r'))
                if i == 5 and gettimers == 1:
                    t1 = int(line.strip('\n\r'))
                if i == 6 and gettimers == 1:
                    t2 = int(line.strip('\n\r'))
                if i == 7 and gettimers == 1:
                    t3 = int(line.strip('\n\r'))
        return gettimers,t0,t1,t2,t3

    def check_emerg(self):
        
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

        if emerg == '0' or emerg == '1' or emerg == '2' or emerg == '3': 
            file=open("Config.txt", "w")
            file.write(id+"\n")
            file.write(str(info_no_of_signals)+"\n")
            file.write(manual+"\n")
            file.write(emerg+"\n")
            file.write(t0+"\n")
            file.write(t1+"\n")
            file.write(t2+"\n")
            file.write(t3+"\n")
            file.write('1'+"\n")
            file.close()
            print("Starting Emergency Mode for 20 sec!!!")
            emergobject=runsignal.TimerSet()
            emergobject.emergency(emerg)
            print("Ending Emergency Mode!!!")
