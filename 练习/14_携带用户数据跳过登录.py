# -*- coding:utf-8 -*-
# @Time : 2023/9/2 17:37
# Auther : shenyuming
# @File : 14_携带用户数据跳过登录.py
# @Software : PyCharm
print()
'''
携带用户数据跳过验证登录，有一定的概率
'''

from selenium import webdriver
import time

option = webdriver.ChromeOptions()
#在浏览器网址输入：chrome://version ,复制个人资料路径， 最后/Default 不要
user_data_dir = '/Users/shenyuming/Library/Application Support/Google/Chrome'
option.add_argument(f'--user_data_dir={user_data_dir}')

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(1)
print('窗口大小：',driver.get_window_size())
driver.get(r'http://172.18.31.26:8601/jobinfo?jobGroup=16')
time.sleep(2)

driver.quit()