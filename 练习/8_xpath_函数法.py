# -*- coding:utf-8 -*-
# @Time : 2023/8/13 17:10
# Auther : shenyuming
# @File : 8_xpath_函数法.py
# @Software : PyCharm

'''
    xpath函数法
    动态变化的值，使用函数法可以获得
'''
import os.path

from selenium import webdriver
import time
driver = webdriver.Chrome()
time.sleep(3)
path = os.path.abspath('../html/test_min.html')
driver.get(r'file://'+path)
time.sleep(2)
#value以pro开头的
ele1 = driver.find_element_by_xpath('//*[starts-with(@value,"pro")]')
# ele1.click()


#value属性包含 conf
ele2 = driver.find_element_by_xpath('//*[contains(@value,"conf")]')
# ele2.click()

#获得 p标签 文本 = xx的元素
ele3 = driver.find_element_by_xpath('//p[text()="这是min的段落"]')
print(ele3.text)

#获得 p标签下，包含 '这' 的文本
ele4 = driver.find_element_by_xpath('//p[contains(text(),"这")]')
print(ele4.text)

driver.quit()
