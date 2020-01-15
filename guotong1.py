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
def handle(phone):
    #验证码登录
    time.sleep(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_quick_login_al']").click()
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_account_flq']").send_keys(phone)
    get_phone(phone)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_flq']").click()
    time.sleep(50)
    result = get_code(phone)
    result = result.split('|')
    if result[0] == 'success':  # 判断变量否为'python'
        code = re.search('\d{6}', result[1]).group(0)
    else:
        invite_phones.remove(phone)
        print 'error2'
        return 0
    print('please input code')
    print(code)
    #source = open("D:\\abc\\code.txt", "r")  # 密码文件
    #code = source.read()  # 读取验证码
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_verify_code_flq']").send_keys(code)
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.gt.app.gtecard:id/btn_login_flq']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_4']").click()
    appium1.ABD_Move(555.5, 1585.1, 600.4, 1070.4, 800)
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_setting']").click()
    # 设定支付密码
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_change_pay_pwd']").click()
    get_phone(phone)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_get_sms']").click()
    time.sleep(50)
    result = get_code(phone)
    result = result.split('|')
    if result[0] == 'success':  # 判断变量否为'python'
        code = re.search('\d{6}', result[1]).group(0)
    else:
        invite_phones.remove(phone)
        print 'error2'
        return 0
    print('please input code')
    print(code)
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
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_get_sms']").click()
    time.sleep(50)
    result = get_code(phone)
    result = result.split('|')
    if result[0] == 'success':  # 判断变量否为'python'
        code = re.search('\d{6}', result[1]).group(0)
    else:
        invite_phones.remove(phone)
        print 'error2'
        return 0
    print('please input code')
    print(code)
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
    return 1
invite_phones =['18227110014','13288476421','18728429542 ','15183812134 ','15883622749','18702864836']
count = 0
index = 0
while (count < 6):
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
    count = count + 1
driver.quit()



