#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-24 10:11
# @Author: sunnnychan@gmail.com
# @File  : Mouse.py

import pyautogui as pag


class Mouse:
    @staticmethod
    def click_center():
        screen_width, screen_height = pag.size()
        pag.click(screen_width / 2, screen_height / 2)

