# -*- coding:utf-8 -*-
# @Time : 2023/9/2 16:37
# Auther : shenyuming
# @File : 13_无头浏览器options.py
# @Software : PyCharm

from selenium import webdriver
import time
option = webdriver.ChromeOptions()
option.add_argument('--headless')
# option.add_argument('--incognito') #无痕模式
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(1)
print('窗口大小：',driver.get_window_size())
driver.get(r'http://172.18.31.26:8601/jobinfo?jobGroup=16')
time.sleep(2)
driver.find_element_by_name('userName').clear()
driver.find_element_by_name('userName').send_keys('admin')
driver.find_element_by_name('password').clear() #div.form-group.has-feedback>[placeholder*="密码"]  css
driver.find_element_by_name('password').send_keys('123456') #.login-box-body>:nth-last-child(2)  css
driver.find_element_by_css_selector('.row>.col-xs-4').click()
time.sleep(2)
driver.find_element_by_css_selector('.fa.fa-circle-o.text-yellow').click()
#driver.find_element_by_xpath("//span[text()='任务管理']").click()  #xpath
driver.find_element_by_css_selector('.input-group>#jobGroup option:nth-last-child(3)').click()

time.sleep(2)
driver.quit()
print('无头浏览器关闭')