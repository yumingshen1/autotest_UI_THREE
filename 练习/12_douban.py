# -*- coding:utf-8 -*-
# @Time : 2023/8/20 21:53
# Auther : shenyuming
# @File : 12_douban.py
# @Software : PyCharm

print()
'''
    打印豆瓣电影的一周热门电影
    打印多个帖子的标题。
    删除多个帖子
    TODO
'''
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://movie.douban.com/')
hot_movie_css = '.billboard-bd td.title>a'  # class：.billboard-bd , #class下的子孙标签 td ,class:title,  class的儿子：a
for movie in driver.find_elements_by_css_selector(hot_movie_css):
    print(movie.text)
sleep(2)
driver.quit()
