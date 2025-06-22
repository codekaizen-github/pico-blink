# pico-blink

## Examples

### Example: Light an LED when a button is pressed

```python
from machine import Pin
led_pin = Pin(15, mode=Pin.OUT)
led_pin.on()
button_pin = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
```
