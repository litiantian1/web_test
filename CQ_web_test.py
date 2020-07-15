# -*-coding:utf-8 -*-
#!/usr/bin/python
#重庆和教育-家校共育
from selenium import webdriver
import base64
from selenium.webdriver.firefox.options import Options
import time
import os

import baiduORC

Url='http://www.cqhejiaoyu.com/'
# 打开浏览器
driver = webdriver.Firefox()
driver.get(Url)
print('ok')



