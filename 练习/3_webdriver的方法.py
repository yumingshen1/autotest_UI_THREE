# -*- coding:utf-8 -*-
# @Time : 2023/8/12 22:52
# Auther : shenyuming
# @File : 3_webdriver的方法.py
# @Software : PyCharm

'''
    webdriver的方法查询
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()

#webdriver的方法 ,开头非_的方法 ，  dir:得到对象的所有属性和方法
for _ in dir(driver):
    if _[0] != '_':
        print(_)

print('----'*10)
#查看开头是 find的方法
for _ in dir(driver):
    if _[:4] == 'find':
        print(_)
driver.quit()

'''
add_cookie
application_cache
back  ------------>后退，返回
capabilities
close  ----------> 关闭当前tab页，不退出浏览器
command_executor
create_options
create_web_element
current_url   ------------> 当前url
current_window_handle
delete_all_cookies
delete_cookie
desired_capabilities
error_handler
execute
execute_async_script
execute_cdp_cmd
execute_script
file_detector
file_detector_context
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
forward   -----------------> 前进
fullscreen_window
get
get_cookie
get_cookies
get_log
get_network_conditions
get_screenshot_as_base64
get_screenshot_as_file
get_screenshot_as_png
get_window_position
get_window_rect
get_window_size
implicitly_wait
launch_app
log_types
maximize_window
minimize_window
mobile
name ----------->浏览器的名字
orientation
page_source
quit ----------->会退出浏览器进程
refresh   ---------->刷新
save_screenshot ----------> png格式的截图 ， driver.save_screenshot(xx.png)
service
session_id
set_network_conditions
set_page_load_timeout
set_script_timeout
set_window_position
set_window_rect
set_window_size
start_client
start_session
stop_client
switch_to
switch_to_active_element
switch_to_alert
switch_to_default_content
switch_to_frame
switch_to_window
title  ----------------> 网页名
w3c
window_handles
'''