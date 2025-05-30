from machine import Pin
from utime import sleep

pin = Pin(13, Pin.OUT)
# pin.on()  # Turn the pin on to start with
# pin.value(0)  # Ensure the pin is off initially

print("LED starts flashing...")
for i in range(25):
    try:
        print(f"Flashing {i + 1}...")
        pin.toggle()
        sleep(.5)  # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
