# -*- coding:utf-8 -*-
# @Time : 2023/9/4 22:40
# Auther : shenyuming
# @File : 18_js.py
# @Software : PyCharm
print()
'''
在浏览器 Console中先尝试输入的是否正确
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.bilibili.com/?spm_id_from=333.874.0.0')
time.sleep(2)

flage = 3

if flage == 4: #document.getElementById().value = ?
    pass


if flage == 3: #滚动条
    print(driver.get_window_size())
    list_dic = []
    items = driver.get_window_size()
    for v in items.values():
        list_dic.append(v)
    time.sleep(2)
    driver.set_window_size(list_dic[0]/2, list_dic[1]/2)
    print(driver.get_window_size())
    js3 = 'window.scrollTo(0,10000)'
    driver.execute_script(js3)
    time.sleep(2)
    js4 = 'window.scrollTo(0,0)'
    driver.execute_script(js4)
    time.sleep(2)
    js5 = 'window.scrollTo(10000,0)'
    driver.execute_script(js5)
    time.sleep(2)
    driver.execute_script(js4)
    time.sleep(2)
    js6 = 'window.scrollTo(0,document.body.scrollHeight)' #y轴最大值
    driver.execute_script(js6)

if flage == 2:      #获得单签的title和url，return不能少
    js1 = 'return document.title'
    js2 = 'return document.URL'
    print(driver.execute_script(js1))
    print(driver.execute_script(js2))

if flage == 1:      #打开一个新的窗口
    driver.execute_script('window.open()')

time.sleep(2)
driver.quit()