# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import os
import random
import re
import pymysql

import requests
import sql as sql
from selenium import webdriver
from appium import webdriver
import time

id = '0'
requests.adapters.DEFAULT_RETRIES = 10
# Returns abs path relative to this file and not cwd
# 获得机器屏幕大小x,y
config = {
    'host': '47.104.181.16',
    'port': 3306,
    'user': 'niujunfei',
    'passwd': 'Fly900303',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
    }
# 打开数据库连接
db = pymysql.connect(host='47.104.181.16', port=3306, user='niujunfei', passwd='Fly900303', db='guotong', charset='utf8',cursorclass=pymysql.cursors.DictCursor)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
#打开国通APP
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '127.0.0.1:21513',
                'appPackage': 'com.gt.app.gtecard', 'appActivity': 'com.account.setting.ui.WelComeActivity',
                "unicodeKeyboard": "True", "resetKeyboard": "True", "newCommandTimeout": "300"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app

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

def handle(mobile,password):
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_account_fln']").send_keys(mobile)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_password_fln']").send_keys(password)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.gt.app.gtecard:id/btn_login_fln']").click()
    time.sleep(5)
    element = driver.find_element_by_xpath( "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_right_element_name']")
    string = element.text
    print(string)
    # SQL 插入语句
    sql = """UPDATE `guotong`.`gt_account`
    SET 
     `coin` = '%s'
    WHERE
        (`id` = '%s');"""%(string,id)
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
    except:
       # 如果发生错误则回滚
       db.rollback()

    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_2']").click()

    time.sleep(2)
    swipeUp(200)
    eles = driver.find_elements_by_id("com.gt.app.gtecard:id/layout_oil_card")
    print(len(eles))
    for index in range(len(eles)):
        element1 = eles[index].find_element_by_id("com.gt.app.gtecard:id/txw_card_name")
        string1 = element1.text
        print(string1)
        element2 = eles[index].find_element_by_id("com.gt.app.gtecard:id/tv_card_num")
        string2 = element2.text
        print(string2)
        element3 = eles[index].find_element_by_id("com.gt.app.gtecard:id/txw_card_value")
        string3 = element3.text
        print(string3)
        # SQL 插入语句
        sql = """INSERT INTO `guotong`.`gt_card` (`account_id`, `type`, `card_num`, `price`) VALUES ( '%s', '%s', '%s', '%s');"""%(id,string1,string2,string3)
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except:
           # 如果发生错误则回滚
           db.rollback()
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_4']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_pay_password']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_login_out']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_confirm']").click()

# SQL 插入语句
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

sql = "SELECT * FROM `gt_account` where id >= 41"
cursor.execute(sql)
   # 获取所有记录列表
results = cursor.fetchall()
print(results)
for row in results:
    print(row['mobile']+row['password'])
    id = row['id']
    handle(row['mobile'], row['password'])
db.close()
# driver.quit()
exit()