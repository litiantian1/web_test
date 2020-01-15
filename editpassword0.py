# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import csv
import os
import re
import sys
import pymysql
import requests
from appium import webdriver
import time
import random
import start_stop_Appium
import keyword

appium1 = start_stop_Appium.Appium()
appium1.start_Appium('127.0.0.1', '4723', '5LMBGM6SBYIRINRS')  # 启动appium
time.sleep(8)
# Returns abs path relative to this file and not cwd
requests.adapters.DEFAULT_RETRIES = 10
reload(sys)
sys.setdefaultencoding('utf8')
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

# 打开数据库连接
#db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='guotong', charset='utf8',cursorclass=pymysql.cursors.DictCursor)

# 使用 cursor() 方法创建一个游标对象 cursor
#cursor = db.cursor()

#打开国通APP
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '5LMBGM6SBYIRINRS',
                'appPackage': 'com.gt.app.gtecard', 'appActivity': 'com.account.setting.ui.WelComeActivity',
                "unicodeKeyboard": "True", "resetKeyboard": "True", "newCommandTimeout": "300"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
def get_phone(phone):
    url = "http://47.106.141.142:9180/service.asmx/sfHmStr?token=E76047593A0DCEA45EB6AB7D8D99207C&hm="+phone
    r = requests.get(url)
    url="http://47.106.141.142:9180/service.asmx/mkHM2Str?token=E76047593A0DCEA45EB6AB7D8D99207C&xmid=13673&hm="+phone+"&op=1&pk=&rj=15783"
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
    password_list = [
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_zero']",
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_one']",
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_two']",
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_three']",
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_four']",
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_five']",
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_six']",
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_seven']",
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_eight']",
        "//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_night']",
    ]
    password_str = str(random.randint(100000, 999999))
    print password_str
    #验证码登录
    driver.implicitly_wait(10)
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
    driver.implicitly_wait(5)
    '''
    element = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_right_element_name']")
    bi_num_str = element.text
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_2']").click()
    time.sleep(2)
    swipeUp(200)
    time.sleep(1)
    eles = driver.find_elements_by_id("com.gt.app.gtecard:id/layout_oil_card")
    print('card_count--'+str(len(eles)))
    img_folder = "D:\PyWork\img\\"
    screen_save_path = img_folder + phone + '.png'
    driver.get_screenshot_as_file(screen_save_path)
    time.sleep(3)
    print(bi_num_str)
    if re.search('20', bi_num_str) == None:
        print(bi_num_str)
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_4']").click()
        time.sleep(2)
        swipeUp(200)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_pay_password']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_login_out']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_confirm']").click()
        return 0
    '''
    try:
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_4']").click()
        driver.implicitly_wait(10)
        time.sleep(2)
        swipeUp(200)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_setting']").click()
    except:
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/layout_4']").click()
        driver.implicitly_wait(10)
        time.sleep(2)
        swipeUp(200)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_setting']").click()
    # 设定支付密码
    driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/ll_change_pay_pwd']").click()
    time.sleep(3)
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
    driver.find_element_by_xpath(password_list[int(password_str[0:1])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[1:2])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[2:3])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[3:4])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[4:5])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[5:6])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[0:1])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[1:2])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[2:3])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[3:4])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[4:5])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[5:6])]).click()
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
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.gt.app.gtecard:id/l_left']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_login_out']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_confirm']").click()
        return 0
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_input_code']").send_keys(code)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_verify_next_step']").click()
    #输入支付密码验证身份
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[0:1])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[1:2])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[2:3])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[3:4])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[4:5])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(password_list[int(password_str[5:6])]).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_input_password']").send_keys('cc'+password_str)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.gt.app.gtecard:id/edx_re_input_password']").send_keys('cc'+password_str)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_complete']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/txw_login_out']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.gt.app.gtecard:id/dialog_confirm']").click()
    stu1 = [phone, password_str]
    with open(my_file_PW, 'a', ) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(stu1)
    print 'success'+phone

    # SQL 插入语句
   # sql = """INSERT INTO `guotong`.`gt_bi_account` (`mobile`, `password`, `pay_password`) VALUES ( '%s', '%s', '%s');""" % (phone,'cc'+password_str,password_str)
   # try:
        # 执行sql语句
        #cursor.execute(sql)
        # 提交到数据库执行
        #db.commit()
   # except:
        # 如果发生错误则回滚
       # db.rollback()
# SQL 查询语句
#sql = "SELECT * FROM `bi_new_account` WHERE `status` = '0' and id >0 order by id limit 100"
# 执行SQL语句
#cursor.execute(sql)
# 获取所有记录列表
#results = cursor.fetchall()
#print results
my_file = 'D:\\abc\\wabi.csv'
my_file_PW = 'D:\\abc\\wabiPW.csv'
data = csv.reader(file(my_file, 'rb'))
# 循环输出每一行信息：
#a = []
#for user in data:
    #a.append(user[0][0:11])
a=['17131743383', '13438061793', '13100410614', '18482033928', '13698198149', '13068852018', '18702820336', '15676092140', '18227111484', '15183842704', '18728480259', '13066351576', '18782037016', '18346686940', '15883812104', '13458499924', '15678540721', '13550659514', '15676082014', '18482300105', '13288634669', '13117694181', '17176741493', '18788461742', '18782069492', '18702823632', '13211373434', '15883625468', '13541706034', '13146925879', '15626167332', '15577127449', '18782053105', '18702899131', '18708100493', '15884278314', '15183853904', '15183828084', '18482316982', '18782001764', '13288641997', '15625115022', '13250482861', '15911707249', '15287103935', '18482391630', '13419046248', '18781937825', '18482371636', '18728411739', '18482302897', '18241448758', '18787098426', '15183813804', '18383854514', '18702878662', '13458557970', '15626187970', '18284220042', '15578274440', '18781924676', '18702861405', '18482361632', '13288612952', '15287133985', '17176835394', '15008347264', '18482388607', '13288808571', '15626189521', '18227107324', '18780045233', '13226621569', '18241440703', '15025169798', '18482305249', '18728441457', '18702867710', '18728499859', '17044336362', '15678455067', '18702822707', '14708016519', '15883610140', '15678567433', '15200586404', '18728480897', '13068820633', '13288658691', '18787461369', '15626189521', '18782066850', '15196321470', '15008394890', '18708183917', '13550665234', '13408046083', '13550660814', '18241440230', '13068850310', '15708412022', '18708117065', '15708472034', '18380644386', '15626182956', '18380644386', '13068868987', '18482306451', '13288467980', '15883630284', '13178660252', '13068853638', '13440148250', '18482352663', '17161237246', '15677560597', '15708402471', '18728412418', '15708400529', '18788400569', '15626170151']
for index in range(len(a)):
    print(a[index])
    handle(a[index])
    #print(a[0])
#handle('17131743383')
driver.quit()




