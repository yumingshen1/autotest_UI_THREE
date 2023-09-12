# -*- coding:utf-8 -*-
# @Time : 2023/9/3 18:53
# Auther : shenyuming
# @File : 17_ActionChains鼠标操作.py
# @Software : PyCharm

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
option = webdriver.ChromeOptions()
# option.add_argument('--headless')
user_data = '/Users/shenyuming/Library/Application Support/Google/Chrome'
option.add_argument(f'--user_data_dir={user_data}')
option.add_argument('--incognito') #无痕模式
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(1)
print('窗口大小：',driver.get_window_size())
driver.get('https://www.bilibili.com/')
time.sleep(2)

flage = 1

if flage == 1:
    #鼠标悬浮, 一:move_to_element   右侧按钮, 先找到悬浮位置，在移动鼠标
    bili_ele = driver.find_element_by_css_selector(".header-upload-entry")
    ActionChains(driver).move_to_element(bili_ele).perform()
    #点击投稿管理
    driver.find_element_by_xpath("//div[contains(text(),'投稿管理')]").click()

elif flage == 2:
    #鼠标悬浮， 二：move_by_offset
    bili_ele = driver.find_element_by_css_selector(".header-upload-entry")
    x = bili_ele.rect['x']+bili_ele.rect['width']/2
    y = bili_ele.rect['y']+bili_ele.rect['height']/2
    ActionChains(driver).move_by_offset(x,y).perform()

time.sleep(2)
driver.quit()
