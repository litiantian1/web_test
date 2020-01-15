# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import os
import sys
from openpyxl import Workbook
from appium import webdriver
import time
import start_stop_Appium
import numpy as np
import pandas as pd

df=pd.DataFrame(columns=('账号','加油币','卡类型','卡号','余额'))
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
time.sleep(10)
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.5)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)

def handle(phone):
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_account_fln']").clear()
    driver.find_element_by_xpath( "//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_account_fln']").send_keys(phone)
    driver.find_element_by_xpath( "//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_password_fln']").send_keys(pw)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.gt.app.gtecard:id/btn_login_fln']").click()
    time.sleep(5)
    swipeUp(1000)
    time.sleep(2)
    element = driver.find_element_by_xpath( "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_right_element_name']")
    string = element.text
    print (string)
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_2']").click()
    time.sleep(1)
    swipeUp(200)
    time.sleep(2)
    swipeUp(200)
    eles = driver.find_elements_by_id("com.gt.app.gtecard:id/layout_oil_card")
    print(len(eles))
    for i in range(len(eles)):
        element1 = eles[i].find_element_by_id("com.gt.app.gtecard:id/txw_card_name")
        string1 = element1.text
        print(string1)
        element2 = eles[i].find_element_by_id("com.gt.app.gtecard:id/tv_card_num")
        string2 = element2.text
        print(string2)
        element3 = eles[i].find_element_by_id("com.gt.app.gtecard:id/txw_card_value")
        string3 = element3.text
        print(string3)
        try:
            df.loc[i]=[phone,string,string1,string2,string3]
        except:
            print(i + 'error')
            break
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_4']").click()
    time.sleep(4)
    swipeUp(200)
    time.sleep(3)
    driver.find_element_by_xpath( "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_pay_password']").click()
    time.sleep(1)
    driver.find_element_by_xpath( "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_login_out']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_confirm']").click()
    return 1
Account_number=['13452662441']
password=['dc123456']
n = 0
phone = Account_number[n]
pw = password[n]
while (n < 1):
    time.sleep(1)
    result=handle(phone)
    time.sleep(1)
    if result==1:
        print 'success' + str(phone)
        df.to_excel('test3.xlsx','Sheet1')
    else:
        print 'error' + str(phone)
        driver.quit()
        time.sleep(5)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
    n=n+1
driver.quit()
