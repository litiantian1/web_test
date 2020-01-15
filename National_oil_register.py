# -*-coding:utf-8 -*-
# !user/bin/python

import os
from threading import Thread

from selenium import webdriver
import time
import start_stop_Appium

appium1 = start_stop_Appium.Appium()
#appium1.start_Appium('127.0.0.1', '4723', '5LMBGM6SBYIRINRS')  # 启动appium
#time.sleep(8)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
#打开国通APP
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '5LMBGM6SBYIRINRS',
                'appPackage': 'com.gt.app.gtecard', 'appActivity': 'com.account.setting.ui.WelComeActivity',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
time.sleep(5)
phnumber=['13983132059','18745491529']#注册号码
invitnumber=['13452662441','15523706295','15523706295','15523706295','15523706295','15523706295','15523706295','15523706295','15523706295','15523706295','13368315289','13368315289','13368315289','13368315289','13983275469','13983275469','18996105820','18996105820','19923129295','19923129295','19923129295','19923129295','13608372251','13608372251','13608372251','13608372251','13608372251','19942266692','19942266692','19942266692','15523340967','15523340967','15523340967']#邀请号码
psssword='HKbb123456'
#手机号码注册用户
try:
    for i in range(2):
        driver.find_element_by_id('com.gt.app.gtecard:id/txw_user_register_fln').click()
        #输入手机号码：
        driver.find_element_by_id('com.gt.app.gtecard:id/edt_phone_num_ar').send_keys(phnumber[i])
        driver.find_element_by_id('com.gt.app.gtecard:id/txw_send_sms_code_ar').click()
        time.sleep(10)
        print('请输入第'+str(i)+'个账号的短信验证码')
        r=raw_input()
        print(r)
        if r=='1':
            print('等待20s')#等待
            time.sleep(20)
            print('输入重新验证码')
            r=raw_input()
        elif r=='2':
            time.sleep(20)
            driver.find_element_by_id('com.gt.app.gtecard:id/edt_sms_code_ar').send_keys(r)
            time.sleep(20)
            driver.find_element_by_id('com.gt.app.gtecard:id/edt_sms_code_ar').clear()
            time.sleep(30)
            print('重新获取验证码')#重新获取验证码
            driver.find_element_by_id('com.gt.app.gtecard:id/txw_send_sms_code_ar').click()
            r=raw_input()
            time.sleep(10)
        else:
            print(r)
        time.sleep(2)
        driver.find_element_by_id('com.gt.app.gtecard:id/edt_sms_code_ar').send_keys(r)
        time.sleep(2)
        driver.find_element_by_id('com.gt.app.gtecard:id/txw_next_step_ar').click()
        time.sleep(1)
        driver.find_element_by_id('com.gt.app.gtecard:id/edx_input_password').send_keys(psssword)
        time.sleep(1)
        driver.find_element_by_id('com.gt.app.gtecard:id/edx_re_input_password').send_keys(psssword)
        driver.find_element_by_id('com.gt.app.gtecard:id/txw_referrer_phone').send_keys(invitnumber[i])
        time.sleep(2)
        driver.find_element_by_id('com.gt.app.gtecard:id/txw_complete').click()
        time.sleep(6)
        driver.find_element_by_id('com.gt.app.gtecard:id/txw_agree_ara').click()
        time.sleep(1)
        driver.find_element_by_id('com.gt.app.gtecard:id/layout_4').click()
        driver.find_element_by_id('com.gt.app.gtecard:id/txw_pay_password').click()
        driver.find_element_by_id('com.gt.app.gtecard:id/txw_login_out').click()
        time.sleep(2)
        driver.find_element_by_id('com.gt.app.gtecard:id/right_btn').click()
except:
    print ('出错了')
    os.system('start/b stopAppiumServer.BAT')
finally:
    print(str(i)+'finally')
    os.system('start/b stopAppiumServer.BAT')