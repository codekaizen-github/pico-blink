from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
for i in range(20):
    try:
        pin.toggle()
        sleep(.25)  # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
