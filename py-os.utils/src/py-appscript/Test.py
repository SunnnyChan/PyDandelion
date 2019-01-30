#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-30 15:43
# @Author: sunnnychan@gmail.com
# @File  : Test.py

from appscript import app
import time


def open_safari():
    safari = app("Safari")
    time.sleep(1)
    safari.windows.first.current_tab.URL.set("http://www.google.com")


def open_chrome():
    chrome = app("Google Chrome")
    time.sleep(1)
    chrome.windows.first.current_tab.URL.set("http://www.google.com")


def main():
    open_safari()
    open_chrome()


if __name__ == '__main__':
    main()
