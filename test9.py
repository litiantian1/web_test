#!usr/bin/env python
# coding:utf-8

import pytesseract
from PIL import Image

image = Image.open(r'74.png')
image = image.convert('L')  #转化为灰度图
threshold = 200            #设定的二值化阈值
table = []                  #table是设定的一个表，下面的for循环可以理解为一个规则，小于阈值的，就设定为0，大于阈值的，就设定为1
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

ima = image.point(table,'1')  #对灰度图进行二值化处理，按照table的规则（也就是上面
ima.save('4.png')