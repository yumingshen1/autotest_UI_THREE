# -*- coding:utf-8 -*-
# @Time : 2023/9/3 18:12
# Auther : shenyuming
# @File : 16_keys键盘操作.py
# @Software : PyCharm
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
# option.add_argument('--headless')
option.add_argument('--incognito') #无痕模式
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(1)
print('窗口大小：',driver.get_window_size())
driver.get(r'http://192.168.23.202:8777/fund/handle')
time.sleep(2)
#登录
driver.find_element_by_id('creditNo').clear()
driver.find_element_by_css_selector('input#creditNo').send_keys('18515607030')  #输入
driver.find_element_by_css_selector('input#creditNo').send_keys(Keys.CONTROL,'A')  # 全选
time.sleep(2)
driver.find_element_by_css_selector('input#creditNo').send_keys(Keys.CONTROL,'C') #复制
driver.find_element_by_css_selector('input#loanNo').send_keys(Keys.CONTROL,'v') # 粘贴
time.sleep(2)
driver.find_element_by_css_selector('input#loanNo').send_keys(Keys.BACKSPACE) # 删除一下
time.sleep(1)
driver.find_element_by_css_selector('input#loanNo').send_keys(Keys.BACK_SPACE*3) #删除两下
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'放款成功')]").click()

time.sleep(2)
driver.quit()
