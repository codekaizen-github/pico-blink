from machine import mem32
from utime import sleep
# Base address for the SIO block
SIO_BASE = 0xD0000000

# SIO register offsets
GPIO_OE_SET = SIO_BASE + 0x0024  # Output enable set
GPIO_OUT_SET = SIO_BASE + 0x0014  # Set GPIO high
GPIO_OUT_CLR = SIO_BASE + 0x0018  # Set GPIO low

# Bitmask for GPIO 0–29 (bit 0 through bit 29 set to 1)
ALL_GPIO_MASK = (1 << 30) - 1  # 0b0011_1111_1111_1111_1111_1111_1111_1111

# Step 1: Enable all GPIOs as outputs
mem32[GPIO_OE_SET] = ALL_GPIO_MASK

for i in range(30):
    # Step 2: Set all pins HIGH
    mem32[GPIO_OUT_SET] = ALL_GPIO_MASK
    print(f"GPIO set to HIGH")

    # (wait, observe, or do something...)
    sleep(1)  # Sleep for 1 second to observe the state

    # Step 3: Set all pins LOW
    mem32[GPIO_OUT_CLR] = ALL_GPIO_MASK

    print(f"GPIO set to LOW")

    sleep(1)  # Sleep for 1 second to observe the state
