import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Board pins for LEDs
led_pins = [3, 5, 7]   # yahan 3 LEDs ke liye pins assign kiye

# Sabko OUTPUT banaya
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Function: ek LED ko ON karo, baaki sabko OFF
def only_one_on(active_pin):
    for pin in led_pins:
        if pin == active_pin:
            GPIO.output(pin, True)   # sirf yeh LED ON
        else:
            GPIO.output(pin, False)  # baaki OFF

try:
    while True:
        # 1st LED ON, baaki OFF
        only_one_on(led_pins[0])
        print("LED 1 ON")
        time.sleep(1)

        # 2nd LED ON, baaki OFF
        only_one_on(led_pins[1])
        print("LED 2 ON")
        time.sleep(1)

        # 3rd LED ON, baaki OFF
        only_one_on(led_pins[2])
        print("LED 3 ON")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
