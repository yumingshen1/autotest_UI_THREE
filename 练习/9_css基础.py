# -*- coding:utf-8 -*-
# @Time : 2023/8/19 22:33
# Auther : shenyuming
# @File : 9_css基础.py
# @Software : PyCharm
from selenium.webdriver.common.by import By

print()
'''
    标签名：tag_name,     如： p  、 html
    id的值： #id_value 、 如：#ls_username
    class值：.class1.class2  如： .px.pm
    组合：  input#ls_username.px.pm
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://www.baidu.com/')
driver.find_element_by_css_selector("#s-top-loginbtn").click()
time.sleep(2)
driver.find_element_by_css_selector("#TANGRAM__PSP_11__userName").send_keys('123')
time.sleep(2)
driver.find_element_by_css_selector("input#TANGRAM__PSP_11__password.pass-text-input.pass-text-input-password").send_keys('456')
time.sleep(2)
driver.find_element_by_css_selector("#TANGRAM__PSP_11__submit.pass-button.pass-button-submit")
driver.quit()