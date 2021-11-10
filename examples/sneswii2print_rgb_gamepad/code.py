### This pretend to use gamepad_controller but in fact it is just a copy of the radial controller

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
###import adafruit_radial_controller
import gamepad_controller

###radial_controller = adafruit_radial_controller.RadialController(usb_hid.devices)
gamepad_controller = gamepad_controller.GamepadController(usb_hid.devices)

position = 0
last_position = 0
DEGREE_TENTHS_MULTIPLIER = 100

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
        position = position+1
        print("button R")
    if buttons.L:
        led[0] = (0, 0, 0)
        position = position-1
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

    delta = position - last_position
    if delta != 0:
        gamepad_controller.rotate(delta * DEGREE_TENTHS_MULTIPLIER)
        last_position = position
