# coding=utf-8
import time
import urllib

from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
import os
from urllib3 import request

while(True):
    Url='http://www.cqhejiaoyu.com/'
    #driver=webdriver.Chrome()
    option=webdriver.FirefoxProfile()
    option.set_preference("plugin.state.flash",2)
    driver=webdriver.Firefox(option)
    time.sleep(2)
    driver.maximize_window()
    driver.get(Url)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[1]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('.//*[@id="mobile"]').send_keys('13452662441')
    time.sleep(2)
    driver.find_element_by_xpath('.//*[@id="passwd"]').send_keys('HKbb352178!')
    # time.sleep(2)
    # print('请输入验证码：')
    # idcode = raw_input()
    # print(idcode)
    savaurl = 'http://www.cqhejiaoyu.com/Index/verify'
    ele = 'verifyimg'
    time.sleep(4)
    #登陆验证码截图，裁剪图片并返回图片验证码名称
    #_save_url 保存路径；yuansu 验证码元素标识
    try:
        #当前项目路径
        #prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        prj_path=os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(prj_path, 'img')  # 图片目录
        file_name = random.randint(1,100)
        file_name_wz = bytes(file_name) + '.png'
        file_url = savaurl + file_name_wz
        driver.get_screenshot_as_file(file_url)  # 截屏并保存
        captchaElem = driver.find_element_by_xpath('//*[@id="verifyimg"]')  # 获取图片元素
        # 获取验证码的绝对坐标
        captchaX = int(captchaElem.location['x'])
        captchaY = int(captchaElem.location['y'])
        # 获取验证码的宽度
        catchaWidth = captchaElem.size['width']
        catchaHeight = captchaElem.size['height']

        capchaRight = captchaX + catchaWidth
        catchaBottom = captchaY + catchaHeight
        driver.maximize_window()

        # 获取截屏的图片
        driver.save_screenshot('screen.png')
        i = Image.open('screen.png')
        #imgobject = Image.open(file_url)
        imgcaptcha = i.crop((capchaRight+10, captchaY, capchaRight+5+catchaWidth, catchaBottom))
        #yanzhangma_file_name = str(file_name) + '副本.png'
        print img_path

        #urllib.urlretrieve(imgcaptcha.save(),img_path+'\\'+file_name_wz)
        #print('ok!')
        imgcaptcha.save(img_path+"/"+file_name_wz)
        driver.quit()
        time.sleep(4)
        print file_name_wz

    except Exception as e:
        print('错误：', e)
