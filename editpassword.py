# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import csv
import os
import random
import re

import requests
from selenium import webdriver
import time
import start_stop_Appium
import keyword

appium1 = start_stop_Appium.Appium()
appium1.start_Appium('127.0.0.1', '4723', '5LMBGM6SBYIRINRS')  # 启动appium
time.sleep(8)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
#打开国通APP
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '5LMBGM6SBYIRINRS',
                'appPackage': 'com.gt.app.gtecard', 'appActivity': 'com.account.setting.ui.WelComeActivity',
                "unicodeKeyboard": "True", "resetKeyboard": "True", "newCommandTimeout": "300"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
def get_phone(phone):
    url="http://47.106.141.142:9180/service.asmx/mkHM2Str?token=E76047593A0DCEA45EB6AB7D8D99207C&xmid=13673&hm="+phone+"&op=1&pk=&rj="
    r = requests.get(url)
    result = r.content
    print result
    return result
def get_code(phone):
    url = "http://47.106.141.142:9180/service.asmx/GetYzm2Str?token=E76047593A0DCEA45EB6AB7D8D99207C&xmid=13673&hm="+phone+"&sf=1"
    r = requests.get(url)
    result = r.content
    print result
    return result
def remove_code(phone):
    url = "http://47.106.141.142:9180/service.asmx/sfHmStr?token=E76047593A0DCEA45EB6AB7D8D99207C&hm="+phone
    r = requests.get(url)
    result = r.content
    return result
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
def handle(phone):
    #验证码登录
    time.sleep(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_quick_login_al']").click()
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_account_flq']").send_keys(phone)
    get_phone(phone)
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_flq']").click()
    time.sleep(50)
    result = get_code(phone)
    print len(result)
    if len(result) > 4:  # 判断变量否为'python'
        code = re.search('\d{6}', result).group(0)
    else:
        remove_code(phone)
        print phone+'error2'
        return 0
    print code
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_verify_code_flq']").send_keys(code)
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.gt.app.gtecard:id/btn_login_flq']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_4']").click()
    time.sleep(2)
    swipeUp(300)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_setting']").click()
    # 设定支付密码
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_change_pay_pwd']").click()
    get_phone(phone)
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_get_sms']").click()
    time.sleep(50)
    result = get_code(phone)
    print len(result)
    if len(result)>4:  # 判断变量否为'python'
        code = re.search('\d{6}', result).group(0)
    else:
        remove_code(phone)
        print 'error2'
        return 0
    print code
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_input_code']").send_keys(code)
    driver.find_element_by_xpath( "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_next_step']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_one']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_night']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_one']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_night']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_complete' and @text='完成']").click()
    time.sleep(5)
    #修改登录密码
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_change_account_pwd']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_forget_pwd']").click()
    get_phone(phone)
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_get_sms']").click()
    time.sleep(50)
    result = get_code(phone)
    print len(result)
    if len(result) > 4:  # 判断变量否为'python'
        code = re.search('\d{6}', result).group(0)
    else:
        remove_code(phone)
        print 'error2'
        return 0
    print code
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_input_code']").send_keys(code)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_next_step']").click()
    #输入支付密码验证身份
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_one']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_night']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_input_password']").send_keys('cc123456')
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_re_input_password']").send_keys('cc123456')
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_complete']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_login_out']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_confirm']").click()
    time.sleep(5)
    print 'success'+phone
my_file = 'D:\\abc\\wabi.csv'
data = csv.reader(file(my_file, 'rb'))
# 循环输出每一行信息：
a = []
for user in data:
    a.append(user[0])
for index in range(len(a)):
    handle(a[index])
driver.quit()




