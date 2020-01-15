# -*-coding:utf-8 -*-
# !user/bin/python
import os
import time
from PIL import Image, ImageEnhance
from telnetlib import EC
from selenium import webdriver
import pytesseract
import start_stop_Appium

im = Image.open('./verifyimage.png')
#im = Image.open("E:\\image_code.jpg")
imgry = im.convert('L')  # 图像加强，二值化
sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
sharp_img = sharpness.enhance(2.0)
sharp_img.save('./verifyimage.png')
# http://www.cnblogs.com/txw1958/archive/2012/02/21/2361330.html
# imgry.show()#这是分布测试时候用的，整个程序使用需要注释掉
# imgry.save("E:\\image_code.jpg")

#code = pytesser.image_file_to_string("E:\\image_code.jpg")  # code即为识别出的图片数字str类型

# 打印code观察是否识别正确
im1 = Image.open('./verifyimage.png')
code = pytesseract.image_to_string(im1)  # code即为识别出的图片数字str类型
#判断验证码长度是否为6，如果不是则重新获取。
print(code)
#if len(code)==6:
   # print(code)
#else:
   # print('once again')