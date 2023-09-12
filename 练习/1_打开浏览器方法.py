# -*- coding:utf-8 -*-
# @Time : 2023/8/12 22:51
# Auther : shenyuming
# @File : 1_打开浏览器方法.py
# @Software : PyCharm


from selenium import webdriver
import time,os
driver = webdriver.Chrome()

#普通打开浏览器 , service_args=['--verbose']输出详细日志, service_log_path='selenium20230811.log 日志文件
driver = webdriver.Chrome(service_args=['--verbose'],service_log_path='selenium20230811.log')
driver.get('http://www.baidu.com')


#上下文管理器打开浏览器啊， with
with webdriver.Chrome() as driver:
    html = os.path.abspath('../html/test_min.html')  #获得绝对路径
    print(html)
    driver.get(r'file://'+html)
    time.sleep(3)







