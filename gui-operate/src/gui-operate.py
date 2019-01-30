#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-30 14:38
# @Author: sunnnychan@gmail.com
# @File  : gui-operate.py

from pynput.mouse import Controller as Mouse
from pynput.mouse import Button
from pynput.keyboard import Controller as Keyboard
from pynput.keyboard import Key
import time


def main():
    mouse = Mouse()
    mouse.move(450, 450)
    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(2)

    keyboard = Keyboard()
    keyboard.type('sunny')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


if __name__ == '__main__':
    main()


