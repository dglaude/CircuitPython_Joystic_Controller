# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT

# Classic Controller also work with CLV-202.
# But the "Super Nintendo SNES Classic Mini Controller" has less button and not stick.

import time
import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (0, 0, 0)

import usb_hid
from adafruit_hid.mouse import Mouse

# The mouse object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
mouse = Mouse(usb_hid.devices)

from wiichuck.classic_controller import ClassicController

controller = ClassicController(board.I2C())

while True:
    _, buttons, dpad, _ = controller.values

    if buttons.A:
        led[0] = (255, 0, 0)
    if buttons.B:
        led[0] = (255, 255, 0)
    if buttons.X:
        led[0] = (0, 0, 255)
    if buttons.Y:
        led[0] = (0, 255, 0)
    if buttons.R:
        led[0] = (0, 0, 0)
        mouse.click(Mouse.RIGHT_BUTTON)
        print("button R")
    if buttons.L:
        led[0] = (0, 0, 0)
        mouse.click(Mouse.LEFT_BUTTON)
        print("button L")
    if buttons.start:
        led[0] = (0, 0, 0)
        print("button start")
    if buttons.select:
        led[0] = (0, 0, 0)
        print("button select")
    if dpad.up:
        led[0] = (0, 0, 0)
        print("dpad up")
    if dpad.down:
        led[0] = (0, 0, 0)
        print("dpad down")
    if dpad.right:
        led[0] = (0, 0, 0)
        print("dpad right")
    if dpad.left:
        led[0] = (0, 0, 0)
        print("dpad left")
