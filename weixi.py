# -*-coding:utf-8 -*-
# !user/bin/python

import os
from threading import Thread

from selenium import webdriver
import time
import start_stop_Appium

appium1 = start_stop_Appium.Appium()
appium1.start_Appium('127.0.0.1', '4723', '5LMBGM6SBYIRINRS')  # 启动appium
time.sleep(5)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
#打开微信
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '5LMBGM6SBYIRINRS',
                'appPackage': 'com.tencent.mm', 'appActivity': 'com.tencent.mm.ui.LauncherUI',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
try:
    driver.find_element_by_name('发现').click()
    time.sleep(1)
    driver.find_element_by_name('附近的人').click()
    time.sleep(6)
    a=driver.find_element_by_id('com.tencent.mm:id/cfw')
    driver.find_element(a).find_element_by_name(a[1]).click()
    print('ok')
except:
    print('出错了')
finally:
    os.system('start/b stopAppiumServer.BAT')