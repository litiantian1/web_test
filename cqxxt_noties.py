# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import os
from selenium import webdriver
import time
import start_stop_Appium
import keyword

appium1 = start_stop_Appium.Appium()
appium1.start_Appium('127.0.0.1', '4723', '5LMBGM6SBYIRINRS')  # 启动appium
time.sleep(8)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '5LMBGM6SBYIRINRS',
                'appPackage': 'com.aspirecn.xiaoxuntongTeacher.cq', 'appActivity': '.MicroschoolTeacher',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
time.sleep(10)
try:
   # driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/home_sign_iv').click()  # 签到
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/notice_ll').click()  # 发通知
    time.sleep(3)
    driver.find_element_by_class_name('android.widget.TextView').click()  # 点击搜索框
    driver.find_element_by_class_name('android.widget.EditText').send_keys(u'李')
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/contact_search_rl').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/btn_confirm').click()  # 确认提交
    # 写通知编辑页面
    # location = appium_location
    # location1 = location.AppLocation
    # location1.By_id_click('com.aspirecn.xiaoxuntongTeacher.cq:id/title_ed')
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/title_ed').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/title_ed').send_keys(u'测试标题')  # 添加标题
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/content_ed').send_keys(u'测试正文')  # 添加正文
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/thumbnailIv').click() #添加图片
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photos_btn').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/group_title').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/child_checkbox').click()
    time.sleep(3)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photo_sel_ok').click()# 点击确认按钮
    time.sleep(3)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/tip_message_tv').click()  # 发布
    time.sleep(3)
except:
    print("报错了")
finally:
    appium1.stop_Appium('4723')
    os.system('start/b stopAppiumServer.BAT')