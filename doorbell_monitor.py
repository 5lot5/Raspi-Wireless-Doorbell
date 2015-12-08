#!/usr/bin/env python

'''
   This script checks the status of my wireless doorbell and sends
   an email to my cellphone when someone is at the door

   written by 5lot5 - 5lot5 at telenet dot be

'''

import RPi.GPIO as GPIO
import os, time

doorbell = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(doorbell, GPIO.IN, pull_up_down = GPIO.PUD_UP)
status = GPIO.input(doorbell)


while True:
      status = GPIO.input(doorbell)
      if status == 0:
           file2mail = open("/tmp/file2mail.tmp", "w")
           logtime = time.strftime("%d-%m-%Y %H:%M")
           os.system("echo "+logtime+" >> /var/log/doorbell.log")
           file2mail.write("From: Doorbell@Home\nTo:YourEmail@Yourmailserver.com\nSubject:You got a visitor at the door!\n\n"+logtime+"\n")
           file2mail.close()
           os.system("ssmtp YourEmail@Yourmailserver.com < /tmp/file2mail.tmp")
           print 'done.'
           time.sleep(7)
      else:
           time.sleep(1)
           pass
