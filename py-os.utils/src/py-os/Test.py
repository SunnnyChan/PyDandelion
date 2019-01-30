#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-30 16:03
# @Author: sunnnychan@gmail.com
# @File  : Test.py

import os


def main():
    os.system('open -a /Applications/Safari.app http://www.google.com')
    os.system('open -a "/Applications/Google Chrome.app" http://www.google.com')


if __name__ == '__main__':
    main()