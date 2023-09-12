# -*- coding:utf-8 -*-
# @Time : 2023/8/11 23:19
# Auther : shenyuming
# @File : 2_导入webdriver方式.py
# @Software : PyCharm

'''
    导入webdriver的方法
'''
import os.path
import time

#第一种直接导入
from selenium import webdriver
webdriver = webdriver.Chrome()
webdriver.get()


#另一种导入webdriver的方式
from selenium.webdriver.chrome.webdriver import WebDriver  # noqa
driver = WebDriver()
driver.get()
