# -*-coding:utf-8 -*-
#!/usr/bin/python
#重庆和教育-家校共育

import base64
import os
import time

from selenium import webdriver

import baiduORC
from lib import emil_test2

Url='http://www.cqhejiaoyu.com/'

#设置允许flash
option = webdriver.FirefoxProfile()
option.set_preference("plugin.state.flash", 2)

# 打开浏览器
driver = webdriver.Firefox(option)
time.sleep(2)
driver.maximize_window()
driver.get(url=Url)