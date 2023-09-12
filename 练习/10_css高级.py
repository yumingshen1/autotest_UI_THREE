# -*- coding:utf-8 -*-
# @Time : 2023/8/19 23:07
# Auther : shenyuming
# @File : 10_css高级.py
# @Software : PyCharm
print()

'''
    div p   : div下的子孙元素，
    div>p   : div的子元素，
    div+p   : 紧跟div的首个p元素 , 平级
    [属性=属性值]  ： 属性法 [id='ls_username']
    [属性^=属性值] ： [href^="https"]	以https开头的href
    [属性*=属性值] ： [herf*="https"] 包含https"的href
    [属性$=属性值] ： [href$="https"] 以https结尾的href
    
    #div2>input:ntd-child(2) ： 父元素div2下的 位置在第二的input元素
    #div2>p:first-child:    父元素div2下的 位置排第一的元素（p）
    #div2>:first-child:     父元素div2下的 位置排第一的元素
    div2>:last-child:       父元素div2下的 ，最后一个元素
    div2>:nth-last-child(2) : 父元素div2下的 倒数第二个元素
    p:nth-child(2)	:   p标签下的第二个元素
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https:www.baidu.com")
driver.implicitly_wait(1)
driver.find_element_by_css_selector(".s-top-right.s-isindex-wrap").click()
time.sleep(1)
driver.find_element_by_css_selector("[id^='TANGRAM__PSP']").send_keys('123')
time.sleep(2)
driver.find_element_by_css_selector("[id$='11__password']").send_keys('沈芮晴')
time.sleep(2)
driver.find_element_by_css_selector(".pass-button.pass-button-submit").click()
time.sleep(2)
driver.quit()
