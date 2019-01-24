#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-23 17:40
# @Author: sunnnychan@gmail.com
# @File  : main.py

import pyautogui as pag
import gui.Mouse

dictRawFile = 'dict.t'
dictFile = 'dict1.t'

pag.FAILSAFE = True


def handle_dict():
    rf = open(dictRawFile, 'r')
    wf = open(dictFile, 'w')
    lines = rf.readlines()
    for line in lines:
        line = line.strip('\n')
        wf.write(line + '\n')
        upper = line.upper()
        if ~ lines.__contains__(upper):
            wf.write(upper + '\n')
        capitalize = line.capitalize()
        if ~ lines.__contains__(upper):
            wf.write(capitalize + '\n')


def main():
    handle_dict()
    gui.Mouse.Mouse.click_center()
    rf1 = open(dictFile, 'r')
    for line1 in rf1:
        line1 = line1.strip('\n')
        rf2 = open(dictFile, 'r')
        for line2 in rf2:
            password = line1 + line2.strip('\n')
            print(password)
#            pag.typewrite(password)
    rf1.close()


if __name__ == '__main__':
    main()
