# -*-coding:utf-8 -*-
# !user/bin/python
#from selenium.webdriver.support import expected_conditions as EC
from telnetlib import EC
from time import sleep
from PIL import Image
#from urllib import request
import urllib2
from urllib2 import request_host
import pytesseract
import start_stop_Appium
import os
import time
from selenium import webdriver

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
time.sleep(10)

class Login:

    def img_for_str(self, driver):

        # 注释方法无法实现
        # imgSrc = driver.find_element_by_id('verifyimage').get_attribute('src')
        # request.urlretrieve(imgSrc, './verifyimage.jpg')

        # 截图page
        driver.save_screenshot('page.png')
        # 获取元素
        verifyimg_ele = driver.find_element_by_id('verifyimage')
        # 计算出元素上、下、左、右 位置
        left = verifyimg_ele.location['x']
        top = verifyimg_ele.location['y']
        right = verifyimg_ele.location['x'] + verifyimg_ele.size['width']
        bottom = verifyimg_ele.location['y'] + verifyimg_ele.size['height']
        img = Image.open('./page.png')
        img = img.crop((left, top, right, bottom))
        img.save('./verifyimage.png')
        image = Image.open('./verifyimage.png')
        code = pytesseract.image_to_string(image)  # code即为识别出的图片数字str类型
        return code

    def wait_for_input(self, driver):
        driver.find_element_by_id('verify').clear()
        verify_code = driver.find_element_by_id('verify')
        while True:
            verify_code.send_keys(Login().img_for_str(driver))
            if len(verify_code.get_attribute('value')) < 4:
                sleep(0.1)
            else:
                driver.find_element_by_id('loginBtn').click()
                sleep(0.5)
                # 出现alert关闭，否则跳出，进入下一步
                alert_result = EC.alert_is_present()(driver)
                if alert_result:
                    driver.switch_to.alert.accept()
                    driver.find_element_by_id('verify').clear()
                    driver.find_element_by_id('verifyimage').click()    # 刷新验证码
                    continue
                elif alert_result is False:
                    break

    def user_login(self, driver, username, password):
        # type: (object, object, object) -> object
        # 输入账号/密码
        driver.find_element_by_xpath(".//*[@class = 'x_ynNewNav']/ul/li[2]/a").click()
        driver.find_element_by_id('mobile').clear()
        driver.find_element_by_id('mobile').send_keys(username)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('verify').clear()
        Login().wait_for_input(driver)

        return driver

    def user_identify(self, driver, name, identify, school):

        # 三个列表不能定义在class外面，否则列表数值不会清空
        user_nameNum = []
        user_identifyNum = []
        user_schoolNum = []

        # 登录人员身份选择
        name_element = driver.find_elements_by_xpath(".//*[@id='loginIdentity']/div/p[1]/label/span[1]")
        identify_element = driver.find_elements_by_xpath(".//*[@id='loginIdentity']/div/p[1]/label/span[2]")
        school_element = driver.find_elements_by_xpath(".//*[@id='loginIdentity']/div/p[1]/label/span[3]")
        # 分别在每一组元素中寻找匹配的元素，记录下标值，形成三个列表：user_nameNum、user_identifyNum、user_schoolNum
        for name_element_i in range(len(name_element)):
            if name_element[name_element_i].text == name:
                user_nameNum.append(name_element_i)
            else:
                continue
        for identify_element_i in range(len(identify_element)):
            if identify_element[identify_element_i].text == identify:
                user_identifyNum.append(identify_element_i)
            else:
                continue
        for school_element_i in range(len(school_element)):
            if school_element[school_element_i].text == school:
                user_schoolNum.append(school_element_i)
            else:
                continue
        # 判断三个列表：user_nameNum、user_identifyNum、user_schoolNum，相同的元素，即为name+identify+school匹配的项，+1即得到需要定位的元素
        for user_nameNum_i in user_nameNum:
            for user_identifyNum_i in user_identifyNum:
                for user_schoolNum_i in user_schoolNum:
                    if user_schoolNum_i == user_identifyNum_i == user_nameNum_i:
                        driver.find_element_by_xpath(".//*[@id='loginIdentity']/div/p[1]/label[{}]".format(user_nameNum_i + 1)).click()
                        driver.find_element_by_id('confirmLogin').click()
                        break

                    else:
                        continue
        user_nameNum.clear()
        user_identifyNum.clear()
        user_schoolNum.clear()
        return driver

    def user_logout(self, driver):
        setup = driver.find_element_by_class_name('x_ynSetup')
        while setup.is_displayed() is not True:
            driver.find_element_by_xpath(".//*[@class = 'x_ynNewTop']/a").click()
        setup_element = driver.find_elements_by_xpath(".//*[@class = 'x_ynSetup']/ul/li/a")
        for setup_element_i in setup_element:
            if setup_element_i.text == '退出':
                setup_element_i.click()
                break
        # 退出确认提示
        driver.find_element_by_xpath(".//*[@class = 'x_ynGiveup']/p[2]/a[2]").click()
        return driver

if __name__ == '__main__':
   login1=Login
   login1.user_login(driver,'13452662661','123456dc')
