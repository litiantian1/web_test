# !user/bin/python
# -*-coding:utf-8 -*-
# coding=utf-8
import os
import random
import re

import requests
from selenium import webdriver
import time
import start_stop_Appium

appium1 = start_stop_Appium.Appium()
appium1.start_Appium('127.0.0.1', '4723', '5LMBGM6SBYIRINRS')  # 启动appium
time.sleep(8)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
#打开国通APP
desired_caps = {'platformName': 'Android', 'platformVersion': '5.1.1', 'deviceName': '5LMBGM6SBYIRINRS',
                'appPackage': 'com.gt.app.gtecard', 'appActivity': 'com.account.setting.ui.WelComeActivity',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app

def get_phone(phone):
    url="http://47.106.141.142:9180/service.asmx/mkHM2Str?token=E76047593A0DCEA45EB6AB7D8D99207C&xmid=13673&hm="+phone+"&op=1&pk=&rj="
    r = requests.get(url)
    result = r.content
    return result
def get_code(phone):
    url = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=00500924da31643dc9567e3e7beaa5e4c8da9085&itemid=13673&mobile="+phone+"&release=1"
    r = requests.get(url)
    result = r.content
    return result
phone=['13288476421 ']
time.sleep(5)
driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_account_flq']").send_keys(phone)
#driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_account_flq']").send_keys(phone)
get_phone(phone[0])
driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_flq']").click()
time.sleep(50)
result = get_code(phone[0])
result = result.split('|')
if result[0] == 'success':  # 判断变量否为'python'
    code = re.search('\d{6}', result[1]).group(0)
    print(code)
else:
    print 'error2'
driver.quit()