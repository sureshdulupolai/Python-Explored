
"""
| Library            | Purpose                                              |
| ------------------ | ---------------------------------------------------- |
| `pyserial`         | Communicate with Arduino over USB                    |
| `pynput`           | Optional: control Arduino with keyboard/mouse events |
| `Tkinter` / `PyQt` | Optional: GUI to control Arduino                     |
| `Matplotlib`       | Plot sensor data in real-time                        |

"""


import serial
import time

# Connect to Arduino (check COM port)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Wait for Arduino to initialize

# Turn LED ON
arduino.write(b'H')
time.sleep(1)

# Turn LED OFF
arduino.write(b'L')
time.sleep(1)

arduino.close()
