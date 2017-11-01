#Dit is led rood#


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT) #LED rood
GPIO.setup(16,GPIO.OUT) #LED geel
GPIO.setup(12,GPIO.OUT) #LED groen


# Als machine start voor de eerste keer

for i in range(10, 60, 10):
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(12, GPIO.LOW)




# def rood():
#     GPIO.output(26, GPIO.HIGH)
#
#
# def geel():
#     GPIO.output(16, GPIO.HIGH)
#
#
# def groen():
#     GPIO.output(12, GPIO.HIGH)
#
#
#
#



GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        input_state = GPIO.input(18)
        if input_state ==False:
        print('Motion detected')
        time.sleep(0.2)