from machine import Pin
from time import sleep_us
led_pin = Pin(15, mode=Pin.OUT)
button_pin = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
BUTTON_ON = 0
BUTTON_OFF = 1

flash_pattern = []
total_cycles = 500000
sampling_rate = 1


def playback():
    while True:
        led_pin.off()
        for cycles in flash_pattern:
            led_pin.toggle()
            for _ in range(cycles):
                if button_pin.value() == BUTTON_ON:
                    led_pin.off()
                    return
                sleep_us(sampling_rate)


def record():
    cycle_counter = 0
    flash_pattern.clear()
    button_pin_state = BUTTON_ON
    led_pin.on()
    while cycle_counter < total_cycles:
        print(cycle_counter)
        toggle_counter = 0
        while button_pin.value() == button_pin_state and cycle_counter < total_cycles:
            toggle_counter += 1
            cycle_counter += 1
            sleep_us(sampling_rate)
        button_pin_state = button_pin.value()
        flash_pattern.append(toggle_counter)
        if button_pin_state == BUTTON_ON:
            led_pin.on()
        else:
            led_pin.off()


def recording_ended():
    alert_pattern = [50000, 50000, 50000, 50000,
                     50000, 50000, 25000, 25000, 25000, 100000]
    led_pin.off()
    for cycles in alert_pattern:
        led_pin.toggle()
        for _ in range(cycles):
            sleep_us(sampling_rate)


while True:
    record()
    recording_ended()
    playback()
