# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import os
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
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='guotong', charset='utf8',cursorclass=pymysql.cursors.DictCursor)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#打开国通APP
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '127.0.0.1:21523',
                'appPackage': 'com.gt.app.gtecard', 'appActivity': 'com.account.setting.ui.WelComeActivity',
                "unicodeKeyboard": "True", "resetKeyboard": "True", "newCommandTimeout": "300"}
driver = webdriver.Remote('http://127.0.0.1:4727/wd/hub', desired_caps)  # 启动app
def get_phone(phone):
    url = "http://47.106.141.142:9180/service.asmx/sfHmStr?token=E76047593A0DCEA45EB6AB7D8D99207C&hm="+phone
    r = requests.get(url)
    url="http://47.106.141.142:9180/service.asmx/mkHM2Str?token=E76047593A0DCEA45EB6AB7D8D99207C&xmid=13673&hm="+phone+"&op=1&pk=&rj="
    r = requests.get(url)
    result = r.content
    return result
def get_code(phone):
    url = "http://47.106.141.142:9180/service.asmx/GetYzm2Str?token=E76047593A0DCEA45EB6AB7D8D99207C&xmid=13673&hm="+phone+"&sf=1"
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

def handle(phone):
    #验证码登录
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_quick_login_al']").click()
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_account_flq']").send_keys(phone)
    result = get_phone(phone)
    if result == '1':  # 判断变量否为'python'
        print result
    else:
        remove_code(phone)
        print phone+'error1'
        return 0
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_flq']").click()
    time.sleep(60)
    result = get_code(phone)
    if len(result) > 4:  # 判断变量否为'python'
        code = re.search('\d{6}', result).group(0)
    else:
        remove_code(phone)
        print phone + 'error2'
        return 0
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edt_verify_code_flq']").send_keys(code)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.gt.app.gtecard:id/btn_login_flq']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_4']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_setting']").click()
    # 设定支付密码
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_change_pay_pwd']").click()
    result = isElementExist("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_get_sms']")
    if result == False:
        remove_code(phone)
        print phone + 'errorpay'
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.gt.app.gtecard:id/img_close']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_login_out']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath( "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_confirm']").click()
        return 0
    result = get_phone(phone)
    if result == '1':  # 判断变量否为'python'
        print result
    else:
        remove_code(phone)
        print phone + 'error1'
        return 0
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_get_sms']").click()
    time.sleep(60)
    result = get_code(phone)
    if len(result)>4:  # 判断变量否为'python'
        code = re.search('\d{6}', result).group(0)
    else:
        remove_code(phone)
        print phone+'error2'
        return 0
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_input_code']").send_keys(code)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath( "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_next_step']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_one']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_night']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_one']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_night']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_complete' and @text='完成']").click()
    driver.implicitly_wait(5)
    #修改登录密码
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_change_account_pwd']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_forget_pwd']").click()
    result = get_phone(phone)
    if result == '1':  # 判断变量否为'python'
        print result
    else:
        remove_code(phone)
        print phone + 'error1'
        return 0
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_get_sms']").click()
    time.sleep(60)
    result = get_code(phone)
    if len(result) > 4:  # 判断变量否为'python'
        code = re.search('\d{6}', result).group(0)
    else:
        remove_code(phone)
        print phone+'error2'
        return 0
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_input_code']").send_keys(code)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_next_step']").click()
    #输入支付密码验证身份
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_one']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_night']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_input_password']").send_keys('cc123456')
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_re_input_password']").send_keys('cc123456')
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_complete']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_login_out']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_confirm']").click()
    print 'success'+phone
    # SQL 插入语句
    sql = """INSERT INTO `guotong`.`gt_bi_account` ( `mobile`) VALUES ('%s');""" % (phone)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
# SQL 查询语句
sql = "SELECT * FROM `bi_new_account` WHERE `status` = '0'  order by id limit 50"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   print results
   for row in results:
        handle(row['mobile'])
except:
   print "Error: unable to fecth data"

driver.quit()




