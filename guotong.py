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
def get_phone():
    url="http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token=00500924da31643dc9567e3e7beaa5e4c8da9085&itemid=12865"
    r = requests.get(url)
    result = r.content
    return result
def get_code(phone):
    url = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=00500924da31643dc9567e3e7beaa5e4c8da9085&itemid=12865&mobile="+phone+"&release=1"
    r = requests.get(url)
    result = r.content
    return result
def remove_code(phone):
    url = "http://api.fxhyd.cn/UserInterface.aspx?action=release&token=00500924da31643dc9567e3e7beaa5e4c8da9085&itemid=12865&mobile="+phone
    r = requests.get(url)
    result = r.content
    return result

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
#打开国通APP
desired_caps = {'platformName': 'Android', 'platformVersion': '5.1.1', 'deviceName': '127.0.0.1:21503',
                'appPackage': 'com.gt.app.gtecard', 'appActivity': 'com.account.setting.ui.WelComeActivity',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app


def handle(invite_phone):
    time.sleep(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_user_register_fln']").click()
    result = get_phone()
    result = result.split('|')
    if result[0] == 'success':
        phone = result[1]
    else:
        remove_code(invite_phone)
        print 'error1'
        return 0
    # phone = '13512367542'
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_phone_num_ar']").send_keys(phone)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_send_sms_code_ar']").click()
    time.sleep(50)
    result = get_code(phone)
    result = result.split('|')
    if result[0] == 'success':  # 判断变量否为'python'
        code = re.search('\d{6}', result[1]).group(0)
    else:
        remove_code(invite_phone)
        print 'error2'
        return 0
    print code
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_sms_code_ar']").send_keys(code)
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_next_step_ar']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_input_password']").send_keys('abc123456')
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_re_input_password']").send_keys('abc123456')
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/txw_referrer_phone']").send_keys(invite_phone)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_complete']").click()
    time.sleep(7)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_agree_ara']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_4']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_pay_password']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_login_out']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_confirm']").click()
    #
    # os.system('start/b stopAppiumServer.BAT')
    return 1


invite_phones =['13452662441']
count = 0
index = 0
while (count < 1):
    while (index < len(invite_phones)):
        time.sleep(1)
        result = handle(invite_phones[index])
        if result == 1:
            print 'success' + str(count) + str(index)
            print 'success' + invite_phones[index]
            index = index + 1
        else:
            print 'error' + str(count) + str(index)
            print 'error' + invite_phones[index]
            driver.quit()
            time.sleep(5)
            driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
    index = 0
    count = count + 1
driver.quit()
