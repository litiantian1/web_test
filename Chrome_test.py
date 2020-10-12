# -*-coding:utf-8 -*-
#!/usr/bin/python
#重庆和教育-家校共育

import base64
import os
import time
from pyvirtualdisplay import Display
from selenium import webdriver


display = Display(visible=0, size=(1080,900))
display.start()
driver = webdriver.Chrome()
Url='http://www.cqhejiaoyu.com/'
driver.get(Url)
