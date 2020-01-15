# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import os
import random
import re

import requests
from selenium import webdriver
import time
import start_stop_Appium

#appium1 = start_stop_Appium.Appium()
#appium1.start_Appium('127.0.0.1', '4723', '127.0.0.1:62001')  # 启动appium
#time.sleep(8)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
#打开国通APP
desired_caps = {'platformName': 'Android', 'platformVersion': '5.1.1', 'deviceName': '127.0.0.1:21503',
                'appPackage': 'com.weikuai.wknews', 'appActivity': 'com.weikuai.wknews.ui.activity.StartActivity',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
def livenew(invite_phone):
    try:
        time.sleep(12)
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.weikuai.wknews:id/iv_close']").click()
        time.sleep(1)
    except:
        #driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.weikuai.wknews:id/iv_close']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.weikuai.wknews:id/tab_rb_mine']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.weikuai.wknews:id/iv_phone']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.weikuai.wknews:id/title_right_text']").click()
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.weikuai.wknews:id/register_phone']").send_keys(phone)
        print(phone)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.weikuai.wknews:id/tv_get_code']").click()
        time.sleep(50)
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.weikuai.wknews:id/et_identify_code']").send_keys(code)
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.weikuai.wknews:id/register_password']").send_keys("dc123456")
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.weikuai.wknews:id/invite_code']").send_keys(invite_phone)
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.weikuai.wknews:id/button_register']").click()
        time.sleep(1)    # os.system('start/b stopAppiumServer.BAT')
        return 1


invite_code =['5068882']
phone=['13452662441']
password=['hkbb123456']
count = 0
index = 0
while (count < 1):
    while (index < len(invite_code)):
        time.sleep(1)
        result = livenew(phone)
        if result == 1:
            print 'success' + str(count) + str(index)
            #print 'success' + invite_phones[index]
            index = index + 1
        else:
            print 'error' + str(count) + str(index)
            #print 'error' + invite_phones[index]
            driver.quit()
            time.sleep(5)
            driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
    index = 0
    count = count + 1
driver.quit()
os.system('start/b stopAppiumServer.BAT')