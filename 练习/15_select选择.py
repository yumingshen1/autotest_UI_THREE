# -*- coding:utf-8 -*-
# @Time : 2023/9/2 18:09
# Auther : shenyuming
# @File : 15_select选择.py
# @Software : PyCharm
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
option = webdriver.ChromeOptions()
# option.add_argument('--headless')
option.add_argument('--incognito') #无痕模式
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(1)
print('窗口大小：',driver.get_window_size())
driver.get(r'http://172.18.31.26:8601/jobinfo?jobGroup=16')
time.sleep(2)
#登录
driver.find_element_by_name('userName').clear()
driver.find_element_by_name('userName').send_keys('admin')
driver.find_element_by_name('password').clear() #div.form-group.has-feedback>[placeholder*="密码"]  css
driver.find_element_by_name('password').send_keys('123456') #.login-box-body>:nth-last-child(2)  css
driver.find_element_by_css_selector('.row>.col-xs-4').click()
time.sleep(2)
#任务管理
driver.find_element_by_css_selector('.fa.fa-circle-o.text-yellow').click()
#driver.find_element_by_xpath("//span[text()='任务管理']").click()  #xpath

flage = 1
if flage == 1:
    #直接选择执行器
    driver.find_element_by_css_selector('.input-group>#jobGroup option:nth-last-child(3)').click()
if flage == 2:
    #select选择执行器
    sele_ele = driver.find_element_by_css_selector("#jobGroup")
    Select(sele_ele).select_by_index(18) #下标0开始 方式一
    Select(sele_ele).select_by_value('16') #value值  方式二
    Select(sele_ele).select_by_visible_text('armani任务')  #文本 方式三
#todo 反选  获取到外层元素，然后获取列表所有元素的共同元素返回一个列表，然后循环选择，之后使用 deselect_all(),

#选择第四页
driver.find_element_by_css_selector('ul.pagination>:nth-last-child(2)>[href*="#"]').click()
time.sleep(5)

#下拉框
xia_sele = "body > div:nth-child(2) > div:nth-child(4) > section:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(7) > div:nth-child(1) > button:nth-child(2)"
driver.find_element_by_css_selector(xia_sele).click()
time.sleep(2)
#执行一次
driver.find_element_by_css_selector("div[class='btn-group open'] a[class='job_trigger']").click()
#保存
driver.find_element_by_css_selector('.btn.btn-primary.ok').click()

time.sleep(2)
driver.quit()
