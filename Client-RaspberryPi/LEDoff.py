import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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
try:
    GPIO.setup(g1,GPIO.OUT)
    GPIO.setup(g2,GPIO.OUT)
    GPIO.setup(g3,GPIO.OUT)
    GPIO.setup(g4,GPIO.OUT)

    GPIO.output(g1,GPIO.LOW)
    GPIO.output(g2,GPIO.LOW)
    GPIO.output(g3,GPIO.LOW)
    GPIO.output(g4,GPIO.LOW)
    GPIO.output(r1,GPIO.LOW)
    GPIO.output(r2,GPIO.LOW)
    GPIO.output(r3,GPIO.LOW)
    GPIO.output(r4,GPIO.LOW)
finally:
    GPIO.cleanup()
