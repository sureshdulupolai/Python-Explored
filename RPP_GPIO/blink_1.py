# Raspberry Pi => RPi.GPIO

# sudo apt-get update
# sudo apt-get install python3-rpi.gpio

import RPi.GPIO as GPIO
import time

# GPIO Pin No Use = 2 for ground
# GPIO.setmode(GPIO.BCM)

# GPIO Board Pin Use = 3 for ground
GPIO.setmode(GPIO.BOARD)

# Board Pin No Ko assing kiya hai ek variable mai
# led is a output device
led = 3

# GPIO.OUT => output perpose ke liye use hone wala hai isliye usko bata rahe hai 
# ki led use for output perpose in setup
GPIO.setup(led, GPIO.OUT)

# no other loop work in this GPIO, it work with WHILE True for infinity loop
while True:

    # led one, git take 0,1 => 1 = True, 0 = False; 1 On, 0 Off
    GPIO.output(led, True) # logic pass hoga 1

    # blink kitne time tak karna hai, delay time
    time.sleep(1) # 1 = one second
    GPIO.output(led, False) # logic pass hoga 0 = off
    time.sleep(2) # off for 2 second only