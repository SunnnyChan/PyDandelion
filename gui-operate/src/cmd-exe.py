#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-25 10:55
# @Author: sunnnychan@gmail.com
# @File  : cmd-exe.py

import pyautogui as pag
from plumbum import cli
import time


class MyApp(cli.Application):
    PROGNAME = "cmd-exe"
    VERSION = "1.0.0"

    def main(self, conf_file):
        print("config file {0}".format(conf_file))
        inputs = open(conf_file, 'r')
        for line in inputs.readlines():
            pag.click(450, 450)
            pag.typewrite(line.strip('\n'))
            pag.press('enter')
            time.sleep(2)


if __name__ == '__main__':
    MyApp.run()

