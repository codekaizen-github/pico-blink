from machine import mem32
from utime import sleep

# Base addresses
IO_BANK0_BASE = 0x40014000
SIO_BASE = 0xD0000000

# Offsets
GPIO_CTRL_OFFSET = 0x04  # Offset to the control register for each GPIO
GPIO_FUNCSEL_GPIO = 5    # Function select value for GPIO

# SIO register offsets
GPIO_OE_SET = SIO_BASE + 0x0024
GPIO_OUT_SET = SIO_BASE + 0x0014
GPIO_OUT_CLR = SIO_BASE + 0x0018

# Bitmask for GPIO 0–29
ALL_GPIO_MASK = (1 << 30) - 1  # 0b0011_1111_1111_1111_1111_1111_1111_1111

# Step 1: Tell each pin to act as a GPIO
for pin in range(30):  # Pins 0 to 29
    ctrl_reg = IO_BANK0_BASE + (pin * 8) + GPIO_CTRL_OFFSET
    mem32[ctrl_reg] = GPIO_FUNCSEL_GPIO  # Select function 5 = SIO (GPIO)

# Step 2: Enable all GPIOs as outputs
mem32[GPIO_OE_SET] = ALL_GPIO_MASK

# Step 3: Toggle them
for i in range(100):
    mem32[GPIO_OUT_SET] = ALL_GPIO_MASK
    print("GPIOs set to HIGH")
    sleep(1)

    mem32[GPIO_OUT_CLR] = ALL_GPIO_MASK
    print("GPIOs set to LOW")
    sleep(1)
