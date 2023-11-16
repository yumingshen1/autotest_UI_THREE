# -*- coding:utf-8 -*-
# @Time : 2023/11/15 19:19
# Auther : shenyuming
# @File : text_one.py
# @Software : PyCharm
'''
新文件
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.find_element(By.CSS_SELECTOR,"XX").clear()

print('selenium特性')
if __name__ == '__main__':
    pass