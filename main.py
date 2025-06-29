from machine import Pin
led_pin = Pin(15, mode=Pin.OUT)
button_pin = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
BUTTON_ON = 0
BUTTON_OFF = 1

flash_pattern = [50000, 40000, 20000, 30000, 700000]

if True:
    for cycles in flash_pattern:
        led_pin.toggle()
        for _ in range(cycles):
            pass
    led_pin.toggle()
