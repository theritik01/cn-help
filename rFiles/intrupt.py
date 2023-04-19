import RPi.GPIO as GPIO
import time

led1=27
led2=31
input1=29
input2=33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(input1,GPIO.IN)
GPIO.setup(input2,GPIO.IN)

pos_edge=0
neg_edge=0

GPIO.output(led2,GPIO.HIGH)

def INTL2H():
    print("Inside Interrupt 1")
    global pos_edge
    GPIO.output(led1,GPIO.HIGH)
    pos_edge+=1
    time.sleep(1)
    GPIO.output(led1,GPIO.LOW)
    print("Number of positive edges",pos_edge)
    print("Existing interrupt 1....")
    time.sleep(1)
    
def INTH2L(): 
    print("Entering interrupt 2")
    global neg_edge
    GPIO.output(led2,GPIO.LOW)
    neg_edge=+1
    time.sleep(1)
    GPIO.output(led2,GPIO.HIGH) 
    print("Number of negative edges",neg_edge)
    print("Existing interrupt 2....")
    time.sleep(1)

while True:
    if input("Press Y to enter interrupt 1")=="Y":
        INTL2H()
    if input("Press Y to enter interrupt 2")=="Y":
        INTH2L()
    if input("Press Y to exit")=="Y":
        break