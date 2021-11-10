# boot.py
# SPDX-FileCopyrightText: Copyright (c) 2021 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

### This pretend to use gamepad_controller but in fact it is just a copy of the radial controller

import usb_hid

import gamepad_controller.device

REPORT_ID = 5

gamepad_controller_device = gamepad_controller.device.device(REPORT_ID)
usb_hid.enable((gamepad_controller_device,))
print("Only gamepad enabled...")
