from machine import Pin
led_pin = Pin(15, mode=Pin.OUT)
button_pin = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
BUTTON_ON = 0
BUTTON_OFF = 1
while True:
    if (BUTTON_ON == button_pin.value()):
        led_pin.on()
    else:
        led_pin.off()
