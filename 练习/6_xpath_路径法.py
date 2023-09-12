# -*- coding:utf-8 -*-
# @Time : 2023/8/13 16:06
# Auther : shenyuming
# @File : 6_xpath_路径法.py
# @Software : PyCharm

'''
    xpath 绝对路径法 | 相对路径
'''
import os.path

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(5)
path = os.path.abspath('../html/test_min.html')
print(path)
driver.get(r'file://'+path)
time.sleep(5)

#绝对路径
ele1 = driver.find_element_by_xpath('/html/body/div/div[1]/p')

#相对路径
ele2 = driver.find_element_by_xpath('//*[@id="div2"]/p')
print(ele1.text)
print(ele2.text)

driver.quit()