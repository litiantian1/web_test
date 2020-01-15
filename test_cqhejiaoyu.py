# -*-coding:utf-8 -*-
#!/usr/bin/python
#重庆和教育-家校共育
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium import webdriver
from datetime import datetime
Url='http://www.cqhejiaoyu.com/'
driver=webdriver.Firefox()
#driver = webdriver.Chrome()
driver.maximize_window()
starttime=datetime.now()
driver.get(Url)
endtime=datetime.now()
print (endtime-starttime).seconds