"""
This code allows me to create a dynamic prefix, adds it to my clipboard manager and
clears exsiting history for easy access. I use modules to emulate the keyboard
and the datetime library to fetch the current date. I organized into functions
for easier organization
"""

import pyperclip as pc
import datetime as dt
from pynput.keyboard import Controller, Key
import time

kb = Controller()


def clear_cb():
    kb.press(Key.ctrl_l)
    kb.press(Key.shift_l)
    kb.press("x")
    kb.release(Key.ctrl_l)
    kb.release(Key.shift_l)
    kb.release("x")
    time.sleep(0.5)
    kb.press(Key.enter)
    kb.release(Key.enter)
    time.sleep(0.5)


def open_ray():
    kb.press(Key.cmd)
    kb.press(Key.shift_l)
    kb.press("c")


def release_ray():
    kb.release(Key.cmd)
    kb.release(Key.shift_l)
    kb.release("c")


def pin():
    kb.press(Key.cmd)
    kb.press(Key.shift_l)
    kb.press("p")
    time.sleep(2)
    kb.release(Key.cmd)
    kb.release(Key.shift_l)
    kb.release("p")


def clear_pin():
    pin()


def get_format_date():
    global file_prefix
    date = str(dt.datetime.now())
    month = date[5:7]
    day = date[8:10]
    if month[0] == "0":
        month = date[6:7]
    file_prefix = "Jinnette." + month + "_" + day + "."
    print(file_prefix)
    pc.copy(file_prefix)


def main():
    open_ray()
    time.sleep(0.5)
    release_ray()
    time.sleep(0.5)
    clear_cb()
    time.sleep(2)
    clear_pin()  # clears any prior pin
    clear_cb()
    time.sleep(0.5)
    # kb.tap(Key.esc)
    get_format_date()  # grabs/formats date
    time.sleep(2)
    # open_ray() #launches ClipB manager
    time.sleep(0.5)
    # release_ray() #makes sure no keys are still pressed
    pin()  # pins the latest entry to ClipB


if __name__ == main():
    main()
