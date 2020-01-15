# -*-coding:utf-8 -*-
# !user/bin/python
import os
import time
from PIL import Image
from telnetlib import EC
from selenium import webdriver
import pytesseract
import start_stop_Appium

appium1 = start_stop_Appium.Appium()
appium1.start_Appium('127.0.0.1', '4723', '5LMBGM6SBYIRINRS')  # 启动appium
time.sleep(8)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
#os.system('start/b startAppiumServer.BAT')
time.sleep(8)
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '5LMBGM6SBYIRINRS',
                'appPackage': 'com.aspirecn.xiaoxuntongParent.cq', 'appActivity': '.MicroschoolParent',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
time.sleep(10)
#输入账号和密码
driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/phone_number_edit_text').clear()
time.sleep(2)
driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/phone_number_edit_text').send_keys('13452662441')
driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/pwd_edit_text').clear()
time.sleep(2)
driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/pwd_edit_text').send_keys('123456dc')
driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/verify_code_tip').click()#点击图片获取验证码
#driver.save_screenshot(u'bdbutton.png')
#bd1=driver.find_element_by_id()
#os.system('start/b stopAppiumServer.BAT')
# 截图page
driver.save_screenshot('page.png')
# 获取元素
verifyimg_ele = driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/verify_code_iv')
# 计算出元素上、下、左、右 位置
left = verifyimg_ele.location['x']
top = verifyimg_ele.location['y']
right = verifyimg_ele.location['x'] + verifyimg_ele.size['width']
bottom = verifyimg_ele.location['y'] + verifyimg_ele.size['height']
img = Image.open('./page.png')
img = img.crop((left, top, right, bottom))#定位区域截图
img.save('./verifyimage.png')
image = Image.open('./verifyimage.png')
code = pytesseract.image_to_string(image)  # code即为识别出的图片数字str类型
print(code)
os.system('start/b stopAppiumServer.BAT')