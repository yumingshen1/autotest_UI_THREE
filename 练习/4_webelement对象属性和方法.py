# -*- coding:utf-8 -*-
# @Time : 2023/8/12 22:57
# Auther : shenyuming
# @File : 4_webelement对象属性和方法.py
# @Software : PyCharm

'''
webelement对象属性和方法
'''
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get(r'file://'+'/Users/shenyuming/PycharmProjects/autotest_UI_THREE/html/test_min.html')
# time.sleep(3)
# webelement = driver.find_element_by_id('alert')
# webelement.click()
# time.sleep(3)
#
# #获得webelement的所有方法和属性
# for i in dir(webelement):
#     if i[0] != '_':
#         print(i)
#
# driver.quit()
#
#
# #location_once_scrolled_into_view  移动到某个元素
# driver.get('https://www.runoob.com/')
# element = "//*[contains(text(),'网站建设指南')]"
# driver.find_element_by_xpath(element).location_once_scrolled_into_view
# driver.find_element_by_xpath(element).click()
# time.sleep(2)
# driver.quit()

def ShiBieErWeiMa():
    # screenshot_as_png 保存图片,识别验证码，登录
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import ddddocr
    driver = webdriver.Chrome()
    driver.get('https://dym.shurongdai.cn/gbs/src/p/login/index.html#/login')
    time.sleep(1)
    driver.find_element(By.ID,"username").clear()
    driver.find_element(By.ID,"username").send_keys('yuming.shen')
    time.sleep(1)
    driver.find_element(By.ID,"password").clear()
    driver.find_element(By.ID,"password").send_keys('Sym123@bairong')
    time.sleep(1)
    #获得图片验证
    ele = driver.find_element(By.XPATH,'//*[@id="imageCaptcha"]/div[2]/div/div/img')
    ocr = ddddocr.DdddOcr()
    text = ocr.classification(ele.screenshot_as_png)
    print('验证码：',text)
    driver.find_element(By.XPATH,"//*[@placeholder='请输入图片验证码']").send_keys(text)
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@type='submit']").click()
    time.sleep(2)
    driver.quit()

if __name__ == '__main__':
    ShiBieErWeiMa()


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