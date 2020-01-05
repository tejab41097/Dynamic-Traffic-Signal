import RPi.GPIO as GPIO
import time
import videoprocess
import mode

class TimerSet:
    
    def detect_TRAFFIC4(self):
        modechanger = mode.Modechanger()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        try:
            #RED SIGNALS
            r1=23
            r2=25
            r3=7
            r4=21
            GPIO.setup(r1,GPIO.OUT)
            GPIO.setup(r2,GPIO.OUT)
            GPIO.setup(r3,GPIO.OUT)
            GPIO.setup(r4,GPIO.OUT)
            
            #GREEN SIGNALS
            g1=18
            g2=24
            g3=8
            g4=20
            GPIO.setup(g1,GPIO.OUT)
            GPIO.setup(g2,GPIO.OUT)
            GPIO.setup(g3,GPIO.OUT)
            GPIO.setup(g4,GPIO.OUT)
            
            cam1= videoprocess.Cameras('video3.mp4')
            cam2= videoprocess.Cameras('video1.mp4')
            cam3= videoprocess.Cameras('video3.mp4')
            cam4= videoprocess.Cameras('video1.mp4')
            
            print ("Signal 1 Green")
    
            GPIO.output(g1,GPIO.HIGH)
            GPIO.output(r2,GPIO.HIGH)
            GPIO.output(r3,GPIO.HIGH)
            GPIO.output(r4,GPIO.HIGH)
            
            count1=cam1.count_CARS()
    
            GPIO.output(g1,GPIO.LOW)
            GPIO.output(r2,GPIO.LOW)
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(r4,GPIO.LOW)
            modechanger.check_emerg()
            
            print ("Signal 2 Green")
    
            GPIO.output(g2,GPIO.HIGH)
            GPIO.output(r1,GPIO.HIGH)
            GPIO.output(r3,GPIO.HIGH)
            GPIO.output(r4,GPIO.HIGH)
    
            count2=cam2.count_CARS()
    
            GPIO.output(g2,GPIO.LOW)
            GPIO.output(r1,GPIO.LOW)
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(r4,GPIO.LOW)
            modechanger.check_emerg()
    
            print ("Signal 3 Green")

            GPIO.output(g3,GPIO.HIGH)
            GPIO.output(r2,GPIO.HIGH)
            GPIO.output(r1,GPIO.HIGH)
            GPIO.output(r4,GPIO.HIGH)
    
            count3=cam3.count_CARS()

            GPIO.output(g3,GPIO.LOW)
            GPIO.output(r2,GPIO.LOW)
            GPIO.output(r1,GPIO.LOW)
            GPIO.output(r4,GPIO.LOW)
            modechanger.check_emerg()

            print ("Signal 4 Green")
    
            GPIO.output(g4,GPIO.HIGH)
            GPIO.output(r2,GPIO.HIGH)
            GPIO.output(r1,GPIO.HIGH)
            GPIO.output(r3,GPIO.HIGH)
    
            count4=cam4.count_CARS()

            GPIO.output(g4,GPIO.LOW)
            GPIO.output(r2,GPIO.LOW)
            GPIO.output(r1,GPIO.LOW)
            GPIO.output(r3,GPIO.LOW)
            modechanger.check_emerg()
    
            total_count=count1+count2+count3+count4
            per1=count1/total_count
            per2=count2/total_count
            per3=count3/total_count
            per4=count4/total_count
    
            total_timer=40
            timer1=per1*total_timer
            timer2=per2*total_timer
            timer3=per3*total_timer
            timer4=per4*total_timer
            return timer1,timer2,timer3,timer4

        except KeyboardInterrupt: 
            print("Keyboard interrupt")

        except:
            print("some error")

        finally:
            GPIO.cleanup()

    def run_SIGNAL4(self,t1,t2,t3,t4):
        modechanger = mode.Modechanger()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        try:
            #RED SIGNALS
            r1=23
            r2=25
            r3=7
            r4=21
            GPIO.setup(r1,GPIO.OUT)
            GPIO.setup(r2,GPIO.OUT)
            GPIO.setup(r3,GPIO.OUT)
            GPIO.setup(r4,GPIO.OUT)
    
            #GREEN SIGNALS
            g1=18
            g2=24
            g3=8
            g4=20
            GPIO.setup(g1,GPIO.OUT)
            GPIO.setup(g2,GPIO.OUT)
            GPIO.setup(g3,GPIO.OUT)
            GPIO.setup(g4,GPIO.OUT)
    
            print ("Signal 1 Green")
    
            GPIO.output(g1,GPIO.HIGH)
            GPIO.output(r2,GPIO.HIGH)
            GPIO.output(r3,GPIO.HIGH)
            GPIO.output(r4,GPIO.HIGH)
            time.sleep(t1)
            GPIO.output(g1,GPIO.LOW)
            GPIO.output(r2,GPIO.LOW)
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(r4,GPIO.LOW)
            modechanger.check_emerg()
    
            print ("Signal 2 Green")
    
            GPIO.output(g2,GPIO.HIGH)
            GPIO.output(r1,GPIO.HIGH)
            GPIO.output(r3,GPIO.HIGH)
            GPIO.output(r4,GPIO.HIGH)
            time.sleep(t2)
            GPIO.output(g2,GPIO.LOW)
            GPIO.output(r1,GPIO.LOW)
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(r4,GPIO.LOW)
            modechanger.check_emerg()
    
            print ("Signal 3 Green")

            GPIO.output(g3,GPIO.HIGH)
            GPIO.output(r2,GPIO.HIGH)
            GPIO.output(r1,GPIO.HIGH)
            GPIO.output(r4,GPIO.HIGH)
            time.sleep(t3)
            GPIO.output(g3,GPIO.LOW)
            GPIO.output(r2,GPIO.LOW)
            GPIO.output(r1,GPIO.LOW)
            GPIO.output(r4,GPIO.LOW)
            modechanger.check_emerg()

            print ("Signal 4 Green")
    
            GPIO.output(g4,GPIO.HIGH)
            GPIO.output(r2,GPIO.HIGH)
            GPIO.output(r1,GPIO.HIGH)
            GPIO.output(r3,GPIO.HIGH)
            time.sleep(t4)
            GPIO.output(g4,GPIO.LOW)
            GPIO.output(r2,GPIO.LOW)
            GPIO.output(r1,GPIO.LOW)
            GPIO.output(r3,GPIO.LOW)
            modechanger.check_emerg()

        except KeyboardInterrupt: 
            print("Keyboard interrupt")

        except:
            print("some error")

        finally: 
            GPIO.cleanup()

    def emergency(self,sigside):
        control = '0'
        left = '1'
        right = '2'
        oppo = '3'
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        try:
            #RED SIGNALS
            r1=23
            r2=25
            r3=7
            r4=21
            GPIO.setup(r1,GPIO.OUT)
            GPIO.setup(r2,GPIO.OUT)
            GPIO.setup(r3,GPIO.OUT)
            GPIO.setup(r4,GPIO.OUT)
    
            #GREEN SIGNALS
            g1=18
            g2=24
            g3=8
            g4=20
            GPIO.setup(g1,GPIO.OUT)
            GPIO.setup(g2,GPIO.OUT)
            GPIO.setup(g3,GPIO.OUT)
            GPIO.setup(g4,GPIO.OUT)
            
            if sigside == control:
                print ("Controller Signal Green")
            
                GPIO.output(g1,GPIO.HIGH)
                GPIO.output(r2,GPIO.HIGH)
                GPIO.output(r3,GPIO.HIGH)
                GPIO.output(r4,GPIO.HIGH)
                time.sleep(20)
                GPIO.output(g1,GPIO.LOW)
                GPIO.output(r2,GPIO.LOW)
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(r4,GPIO.LOW)
            
            if sigside == left:
                print ("Left Signal Green")

                GPIO.output(g2,GPIO.HIGH)
                GPIO.output(r1,GPIO.HIGH)
                GPIO.output(r3,GPIO.HIGH)
                GPIO.output(r4,GPIO.HIGH)
                time.sleep(20)
                GPIO.output(g2,GPIO.LOW)
                GPIO.output(r1,GPIO.LOW)
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(r4,GPIO.LOW)
    
            if sigside == right:
                print ("Right Signal Green")
                
                GPIO.output(g3,GPIO.HIGH)
                GPIO.output(r2,GPIO.HIGH)
                GPIO.output(r1,GPIO.HIGH)
                GPIO.output(r4,GPIO.HIGH)
                time.sleep(20)
                GPIO.output(g3,GPIO.LOW)
                GPIO.output(r2,GPIO.LOW)
                GPIO.output(r1,GPIO.LOW)
                GPIO.output(r4,GPIO.LOW)
            
            
            if sigside == oppo:
                print ("Opposite Signal Green")
                
                GPIO.output(g4,GPIO.HIGH)
                GPIO.output(r2,GPIO.HIGH)
                GPIO.output(r1,GPIO.HIGH)
                GPIO.output(r3,GPIO.HIGH)
                time.sleep(20)
                GPIO.output(g4,GPIO.LOW)
                GPIO.output(r2,GPIO.LOW)
                GPIO.output(r1,GPIO.LOW)
                GPIO.output(r3,GPIO.LOW)

        except KeyboardInterrupt: 
            print("Keyboard interrupt")

        except:
            print("some error")
