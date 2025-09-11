import time

led_pins = [1, 2, 3]  # Dummy LEDs

def only_one_on(active_led):
    for pin in led_pins:
        if pin == active_led:
            print(f"LED {pin} => ON")
    print("-" * 20)

while True:
    only_one_on(1)
    time.sleep(0.5)

    only_one_on(2)
    time.sleep(0.5)

    only_one_on(3)
    time.sleep(0.5)
