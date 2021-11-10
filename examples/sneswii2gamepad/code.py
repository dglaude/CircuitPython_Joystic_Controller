# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# You must add a gamepad HID device inside your boot.py file
# in order to use this example.
# See this Learn Guide for details:
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/hid-devices#custom-hid-devices-3096614-9

import time
import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (0, 0, 0)

# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT

# Classic Controller also work with CLV-202.
# But the "Super Nintendo SNES Classic Mini Controller" has less button and not stick.

from wiichuck.classic_controller import ClassicController
controller = ClassicController(board.I2C())

# SPDX-FileCopyrightText: Copyright (c) 2021 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import usb_hid

from hid_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

x=0
y=0
oldx=0
oldy=0

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
        print("button R")
    if buttons.L:
        led[0] = (0, 0, 0)
        print("button L")
    if buttons.start:
        led[0] = (0, 0, 0)
        print("button start")
    if buttons.select:
        led[0] = (0, 0, 0)
        print("button select")
    if (y!=0) and not (dpad.up or dpad.down):
        y=0
    if dpad.up:
        y = 127
        led[0] = (0, 0, 0)
        print("dpad up")
    if dpad.down:
        y = -127
        led[0] = (0, 0, 0)
        print("dpad down")
    if (x!=0) and not (dpad.right or dpad.left):
        x=0
    if dpad.right:
        x = 127
        led[0] = (0, 0, 0)
        print("dpad right")
    if dpad.left:
        x = -127
        led[0] = (0, 0, 0)
        print("dpad left")

    gp.move_joysticks(x, y)

