# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import os
from selenium import webdriver
import time
import start_stop_Appium
from PIL import Image,ImageEnhance
import pytesseract

appium1 = start_stop_Appium.Appium()
appium1.start_Appium('127.0.0.1', '4723', '5LMBGM6SBYIRINRS')  # 启动appium
time.sleep(8)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '5LMBGM6SBYIRINRS',
                'appPackage': 'com.aspirecn.xiaoxuntongParent.cq', 'appActivity': '.MicroschoolParent',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
n=0
time.sleep(10)
class Login:
    def __init__(self):
        global n
    def login(self,username,password):
        #输入账号和密码
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/phone_number_edit_text').clear()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/phone_number_edit_text').send_keys(username)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/pwd_edit_text').clear()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/pwd_edit_text').send_keys(password)
        time.sleep(2)
        self.wait_for_input()
        #driver.find_element_by_id().send_keys()
    def wait_for_input(self):
        global n
        #print(u"调用")
        # 点击图片获取验证码
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/verify_code_tip').click()
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
        img = img.crop((left, top, right, bottom)) # 定位区域截图并保存
        img.save('./verifyimage.png')
        image = Image.open('./verifyimage.png')
        # 图片加强，二值化
        imgry = image.convert('L')
        sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
        sharp_img = sharpness.enhance(2.0)
        sharp_img.save('./verifyimage.png')#重新保存
        # 打印code观察是否识别正确
        im1 = Image.open('./verifyimage.png')
        #global n
        code= pytesseract.image_to_string(im1)  # code即为识别出的图片数字str类型
        print(code)
        if len(code)==6:
            return code
        else:
            n+=1
            if n>10:
                print(code)
                return code
            else:
                print('else====')
                self.wait_for_input()
if __name__=='__main__':
    login1=Login()
    login1.login('13452662441','hkbb123456')






