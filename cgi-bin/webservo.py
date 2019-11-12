#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web LED')

print('<form action="" method="post">')
print('<input type="text" name="rad">')
print('<input type="submit" name="sender" value="SUBMIT">')
print('</form>')

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0
form = cgi.FieldStorage()
value = int(form.getvalue("rad"))

def setservo(x):
    pulse = ((top-bottom)*(x+90)/180)+bottom
    servo.ChangeDutyCycle(pulse)
    time.sleep(1.0)

stat = form.getvalue("sender")
print(stat)
if stat == 'SUBMIT':
	setservo(value)
	print(value)
