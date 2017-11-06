import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT) #LED rood
GPIO.setup(16,GPIO.OUT) #LED geel
GPIO.setup(12,GPIO.OUT) #LED groen
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# BELANGRIJK: IP CHECKEN!
host = '192.168.43.82'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

for i in range(10, 60, 10):
    # lampjes springen omstebeurt aan bij opstarten
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(12, GPIO.LOW)

def button_pressed():
    # wanneer er op het knopje wordt gedrukt wordt signaal naar server gestuurd
    s.send(str.encode("button"))
    GPIO.output(16, GPIO.HIGH)
    print("button pressed")

    # na tien seconden gaat het lampje sowieso op rood
    time.sleep(10)
    print("10 seconden zijn voorbij")
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)

def listen_for_reply():
    # hij wacht op input van user (server) of het vals alarm of alarm is
    while True:
        reply = s.recv(1024).decode('UTF-8')
        print(reply)
        if reply == "alarm":
            GPIO.output(26, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
        elif reply == "falsealarm":
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)

while True:
    # een infinite loop die luistert op reactie server
    input_state = GPIO.input(18)
    print(input_state)
    if input_state == False:
        button_pressed()
        listen_for_reply()

s.close()
