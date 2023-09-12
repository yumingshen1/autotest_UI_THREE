# -*- coding:utf-8 -*-
# @Time : 2023/8/12 22:57
# Auther : shenyuming
# @File : 4_webelement对象属性和方法.py
# @Software : PyCharm

'''
webelement对象属性和方法
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r'file://'+'/Users/shenyuming/PycharmProjects/autotest_UI_THREE/html/test_min.html')
time.sleep(3)
webelement = driver.find_element_by_id('alert')
webelement.click()
time.sleep(3)

#获得webelement的所有方法和属性
for i in dir(webelement):
    if i[0] != '_':
        print(i)

driver.quit()



driver.get('https://www.runoob.com/')
element = "//*[contains(text(),'网站建设指南')]"
driver.find_element_by_xpath(element).location_once_scrolled_into_view
driver.find_element_by_xpath(element).click()
time.sleep(2)
driver.quit()


'''
clear
click
find_element
find_element_by_class_name
find_element_by_css_selector
find_element_by_id
find_element_by_link_text
find_element_by_name
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_xpath
find_elements
find_elements_by_class_name
find_elements_by_css_selector
find_elements_by_id
find_elements_by_link_text
find_elements_by_name
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_xpath
get_attribute
get_property
id
is_displayed
is_enabled
is_selected
location
location_once_scrolled_into_view  ----------> 移动到某个元素上
parent
rect
screenshot
screenshot_as_base64
screenshot_as_png
send_keys
size
submit
tag_name
text
value_of_css_property

Process finished with exit code 0

'''