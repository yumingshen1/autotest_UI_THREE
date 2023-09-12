# -*- coding:utf-8 -*-
# @Time : 2023/8/20 21:47
# Auther : shenyuming
# @File : 11_find_elements.py
# @Software : PyCharm

'''
    find_elements : 多个元素
'''

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.baidu.com')
driver.implicitly_wait(1)
elements = driver.find_elements_by_css_selector('.title-content-title')
for ele in elements:
    print(ele.text)
time.sleep(2)
driver.quit()
