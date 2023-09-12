# -*- coding:utf-8 -*-
# @Time : 2023/8/12 23:11
# Auther : shenyuming
# @File : 5_tag定位.py
# @Software : PyCharm

'''
tag容易定位body中的， head中的不好定位
tag基本不用
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r'file://'+'/Users/shenyuming/PycharmProjects/autotest_UI_THREE/html/test.html')
# driver.get(r'file://'+'Users/shenyuming/PycharmProjects/autotest_UI_THREE/html/test_min.html')

webelement = driver.find_element_by_tag_name('p')
print('标签文本：',webelement.text)
print('标签名：',webelement.tag_name)

#定位head中的title的文本 ,
ele = driver.find_element_by_xpath('/html/head/title')
print(ele.get_attribute("textContent"))

time.sleep(2)
driver.quit()