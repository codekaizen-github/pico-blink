from machine import Pin
led_pin = Pin(15, mode=Pin.OUT)
button_pin = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
BUTTON_ON = 0
BUTTON_OFF = 1

flash_pattern = []
total_cycles = 665000


def playback():
    while True:
        led_pin.off()
        for cycles in flash_pattern:
            led_pin.toggle()
            for _ in range(cycles):
                if button_pin.value() == BUTTON_ON:
                    led_pin.off()
                    return
                pass


def record():
    cycle_counter = 0
    flash_pattern.clear()
    button_pin_state = BUTTON_ON
    led_pin.on()
    while cycle_counter < total_cycles:
        toggle_counter = 0
        while button_pin.value() == button_pin_state and cycle_counter < total_cycles:
            toggle_counter += 1
            cycle_counter += 1
        button_pin_state = button_pin.value()
        flash_pattern.append(toggle_counter)
        if button_pin_state == BUTTON_ON:
            led_pin.on()
        else:
            led_pin.off()


def recording_ended():
    alert_pattern = [200000, 200000, 200000, 200000,
                     200000, 200000, 50000, 50000, 50000, 50000]
    led_pin.off()
    for cycles in alert_pattern:
        led_pin.toggle()
        for _ in range(cycles):
            pass


while True:
    record()
    recording_ended()
    playback()
