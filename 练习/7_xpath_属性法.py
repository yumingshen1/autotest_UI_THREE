# -*- coding:utf-8 -*-
# @Time : 2023/8/13 16:53
# Auther : shenyuming
# @File : 7_xpath_属性法.py
# @Software : PyCharm

'''
    xpath属性法[@属性=""] , 结合路径法使用 //*[@属性=""] ， //div/input[@属性=""]
'''
import os.path

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(5)
path = os.path.abspath('../html/test_min.html')
driver.get(r'file://'+path)
ele = driver.find_element_by_xpath('//div/input[@id="prompt" and @value="prompt"]')
ele.click()
time.sleep(2)
driver.quit()
