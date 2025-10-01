"""
pip install RPi.GPIO
pip install gpiozero
pip install adafruit-blinka

pip install pyserial


"""

# a) Raspberry Pi LED Blink

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Pin 18 as output

for i in range(5):
    GPIO.output(18, True)
    time.sleep(1)
    GPIO.output(18, False)
    time.sleep(1)

GPIO.cleanup()


# b) Arduino + Python Serial Communication
import serial
import time

arduino = serial.Serial('COM3', 9600)  # COM port for Arduino
time.sleep(2)  # Wait for Arduino to initialize

arduino.write(b'H')  # Send 'H' to Arduino
data = arduino.readline()
print(data.decode())  # Read response


# c) Read Temperature Sensor (DS18B20)
import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    temp_line = lines[1].split('t=')[-1]
    return float(temp_line)/1000

while True:
    print("Temperature:", read_temp(), "°C")
    time.sleep(1)
