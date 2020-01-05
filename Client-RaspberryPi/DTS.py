import runsignal
import os
import mode

class Main_class:
    
    def startSignal(self):
        modechanger = mode.Modechanger()
        signal = runsignal.TimerSet()
        configfile='Config.txt'
        list_of_files = os.listdir()
        if configfile in list_of_files:
            print("First Configuration Is Already Done!!")
            while True:
                modebit,t0,t1,t2,t3 = modechanger.check_manual_auto()
                print(t0,t1,t2,t3)
                if modebit == 1:
                    signal.run_SIGNAL4(t0,t1,t2,t3)
                elif modebit == 0:
                    timer0,timer1,timer2,timer3=signal.detect_TRAFFIC4()
                    print(timer0,timer1,timer2,timer3)
                    signal.run_SIGNAL4(timer0,timer1,timer2,timer3)
        else: 
            import raspberry_learn
            
mainobject=Main_class()
mainobject.startSignal()
