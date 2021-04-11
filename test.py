#! /user/bin/env python
# -*- coding: utf-8 -*-
"""
@author: gingkg
@contact: sby2015666@163.com
@software: PyCharm
@project: pymarl
@file: test.py
@date: 2021/4/9
@desc: 测试 sacred
"""

from sacred import Experiment
from sacred.observers import FileStorageObserver
from main import ex

# r = ex.run()

# ex = Experiment(name="test1")
# ex.observers.append(FileStorageObserver("my_run_test1"))
#
#
# @ex.config
# def my_config():
#     message = "hello world"
#
#
# @ex.automain
# def my_main(message):
#     print(message)


# Python program to explain os._exit() method

# importing os module
import os

return_codes=[os.EX_OK]

print(return_codes)










