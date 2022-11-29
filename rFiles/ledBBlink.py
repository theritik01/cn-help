import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT)
while True:
    GPIO.output(8, GPIO.HIGH) 
    sleep(1)
    GPIO.output(8, GPIO.LOW) 
    sleep(1)

#Brightness Change 

import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM) 
GPIO.setup(18,GPIO.OUT)
pwm = GPIO.PWM(18, 500) 
pwm.start(100)
while True:
    duty_S = input("enter the brightness") 
    duty = int(duty_S) 
    pwm.ChangeDutyCycle(duty)