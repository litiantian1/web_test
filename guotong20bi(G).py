# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import os
import random
import re
import sys
import pymysql

import requests
from selenium import webdriver
import time
requests.adapters.DEFAULT_RETRIES = 10
reload(sys)
sys.setdefaultencoding('utf8')
# Returns abs path relative to this file and not cwd
# 获得机器屏幕大小x,y

# 打开数据库连接
#db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='guotong', charset='utf8',cursorclass=pymysql.cursors.DictCursor)

# 使用 cursor() 方法创建一个游标对象 cursor
#cursor = db.cursor()



def get_phone():
    url="http://47.106.141.142:9180/service.asmx/GetHM2Str?token=E76047593A0DCEA45EB6AB7D8D99207C&xmid=13673&sl=1&lx=0&a1=&a2=&pk=&ks=0&rj="
    r = requests.get(url)
    result = r.content
    return result
def remove_code(phone):
    url = "http://47.106.141.142:9180/service.asmx/sfHmStr?token=E76047593A0DCEA45EB6AB7D8D99207C&hm="+phone
    r = requests.get(url)
    result = r.content
    return result
def isElementExist(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
#打开国通APP
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '127.0.0.1:21503',
                'appPackage': 'com.gt.app.gtecard', 'appActivity': 'com.account.setting.ui.WelComeActivity',
                "unicodeKeyboard": "True", "resetKeyboard": "True", "newCommandTimeout": "300"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app


def handle():
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_normal_login_al']").click()
    driver.implicitly_wait(5)
    result = get_phone()
    result = result.split('=')
    if result[0] == 'hm':
        phone = result[1]
    else:
        print 'error1'
        return 0
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_account_fln']").send_keys(phone)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_password_fln']").send_keys('gr456erg1re')
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.gt.app.gtecard:id/btn_login_fln']").click()
    time.sleep(3)
    result = isElementExist("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_content']")
    if result == True:
        text = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_content']").text
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_alert']").click()
        if text == "账号或密码错误":
            print phone

        else:
            print 'error1'
    else:
       print 'error2'
    remove_code(phone)
time.sleep(5)
while (1):
    handle()

driver.quit()
