# -*-coding:utf-8 -*-
#!/usr/bin/python
#重庆和教育-家校共育

import base64
import os
import time

from selenium import webdriver

import baiduORC
from lib import emil_test2

Url='http://www.cqhejiaoyu.com/'

#设置允许flash
option = webdriver.FirefoxProfile()
option.set_preference("plugin.state.flash", 2)

# 打开浏览器
driver = webdriver.Firefox(option)
time.sleep(2)
driver.maximize_window()
driver.get(url=Url)

prj_path = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(prj_path, 'img')  # 图片目录
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[1]/a').click()
time.sleep(2)
driver.find_element_by_xpath('.//*[@id="mobile"]').send_keys('13983132059')
time.sleep(2)
driver.find_element_by_xpath('.//*[@id="passwd"]').send_keys('hkBB123456~')
time.sleep(2)
def web_login():
    #获取验证码图片
    get_img=image_cj()
    time.sleep(3)
    #图片处理
    image1=baiduORC.Recognise(get_img)
    #图片识别
    #获取验证码
    word =baiduORC.RecogniseForm(access_token=token, image=image1)
    emil_test2.config1.logging.info("识别结果")
    print("识别结果")
    print(word.encode('utf-8'))
    if len(word)==6:
    #请输入验证码
        time.sleep(2)
        driver.find_element_by_xpath('.//*[@id="verify"]').send_keys(word)
        time.sleep(2)
        driver.find_element_by_xpath('.//*[@id="loginForm"]/li[4]/button').click()
        time.sleep(2)
        #判断验证码是否正确
        try:
            driver.find_element_by_xpath("/html/body/div[3]/div/div/form/ul/li/p[1]/span[1]/input").click()
            driver.find_element_by_xpath('.//*[@id="loginForm"]/p/input').click()
            time.sleep(4)
            emil_test2.config1.logging.info("登陆成功")
            print('登录成功')
        except:
            time.sleep(2)
            driver.find_element_by_class_name('layui-layer-btn0').click()
            #driver.find_element_by_xpath("/html/body/div[6]/div[3]/a").click()
            #driver.find_element_by_xpath("/html/body/div[7]/div[3]/a").clear()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="verifyimg"]').click()
            time.sleep(1)
            driver.maximize_window()
            driver.find_element_by_xpath('.//*[@id="verify"]').clear()
            time.sleep(2)
            web_login()
    else:
        driver.find_element_by_xpath('//*[@id="verifyimg"]').click()
        print("点击刷新")
        time.sleep(2)
        emil_test2.config1.logging.info("重新处理验证码")
        print("重新处理验证码")
        web_login()

#登陆验证码截图，裁剪图片并返回图片验证码名称
#_save_url 保存路径；yuansu 验证码元素标识
def image_cj():
    try:
        file_name_wz='code.png'
        captchaElem = driver.find_element_by_xpath('//*[@id="verifyimg"]')  # 获取图片元素
        img_url = captchaElem.get_attribute('src')
        #使用JS，将img标签转化为canvas，再将canvas转化为base64，并保存成文件。不用重新请求网络。
        JS = 'image=document.getElementById("verifyimg"); canvas=document.createElement("canvas");canvas.id="mcode"; canvas.width=image.width;canvas.height=image.height;canvas.getContext("2d").drawImage(image,0,0);return canvas.toDataURL("image/png");'
        # 执行 JS 代码并拿到图片 base64 数据
        im_info = driver.execute_script(JS)  # 执行js文件得到带图片信息的图片数据
        im_base64 = im_info.split(',')[1]  # 拿到base64编码的图片信息
        im_bytes = base64.b64decode(im_base64)  # 转为bytes类型
        with open(img_path+"/"+file_name_wz, 'wb') as f:  # 保存图片到本地
            f.write(im_bytes)
        return img_path+"/"+file_name_wz
    except Exception as e:
        print('处理验证码保存错误：', e)

if __name__=='__main__':
    # 获取token
    AK = "N2Rzea28gzaqQ0xG4bmwR6xO"
    SK = "h6RNF7btM6Q03ZP9ukXWc8461XmZzkTd"
    token = baiduORC.GetAccessToken(AK, SK)
    web_login()
    # 点击家校互动
    driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul/li[2]/a").click()
    time.sleep(4)
    print('进入家校互动模块')