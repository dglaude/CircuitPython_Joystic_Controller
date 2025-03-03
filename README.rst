Warning
=======

This is NOT WORKING and an attempt to make JOYSTIC USB-HID support in Circuit Python based on Radial Controler.

The goal is to take the code structure, but replace by the report and description from gamepad from this learn guide:
https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/hid-devices

Work in Progress, do not expect anything yet.

This library make no sense... there is already gamepad support in CircuitPython_HID library:
* https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/examples/hid_gamepad.py
* https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/examples/hid_simple_gamepad.py
* https://circuitpython.readthedocs.io/projects/hid/en/latest/examples.html#simple-gamepad

The learn guide say it, but you have one piece of information in the learn guide and the other in the readthedocs or code.
You have to put both together to figure it out... but I don't have to write any code, or just the glue to the Wii controller.

"You will also need to write a CircuitPython driver to handle your new device. There are examples in the adafruit_hid library."


So, I'll first try to use that...

Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-radial_controller/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/radial_controller/en/latest/
    :alt: Documentation Status


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/adafruit/Adafruit_CircuitPython_Radial_Controller/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_Radial_Controller/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

HID Radial Controller device helper library


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.


Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-radial_controller/>`_.
To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-radial-controller

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-radial-controller

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-radial-controller



Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install radial_controller

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://circuitpython.readthedocs.io/projects/radial_controller/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_Radial_Controller/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
