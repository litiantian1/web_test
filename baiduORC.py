# !/user/bin/env Python3
# -*- coding:utf-8 -*-

"""
file：baidu_api.py
create time:2019/4/10 15:14
author:Loong Xu
desc: 调用百度OCRapi实现文本识别
"""
import base64
from lib2to3.pgen2 import parse
import os
import requests
import parser
import json


def GetAccessToken(ak, sk):
    '''
    获取access_token代码
    :param ak:控制台应用API Key
    :param sk:控制台应用Secret Key
    :return:返回接口调用的access_token参数以及token的有效期（单位为秒）
    '''
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    #AK="N2Rzea28gzaqQ0xG4bmwR6xO"
   # SK="h6RNF7btM6Q03ZP9ukXWc8461XmZzkTd"
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(ak,sk)
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    rs=requests.get(host)
    #response = rs.urlopen(req)
    if (rs.status_code== 200):
        data = json.loads(rs.content)
        access_token = data['access_token']
        expires_in = data['expires_in']
        return access_token


def RecogniseForm(access_token, image, templateSign=None, classifierId=None):
    """
    自定义模板文字识别
    :param access_token:
    :param image:图像数据（string），base64编码，注意大小不超过4M，最短边至少15px，最长边最大4096px，支持jpg/png/bmp格式
    :param templateSign:模板ID（string）
    :param classifierId:分类器ID（int），这个参数与templateSign至少存在一个，优先使用templateSign，存在templateSign时，使用指定模板；如果没有templateSign而有classifierld，表示使用分类器去判断使用模板
    :return:返回识别结果
    """
    try:
        url='https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise'
        url2='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        formdata = {'image': image,
                    'access_token':access_token}
        if templateSign is not None:
            formdata['templateSign'] = templateSign
        if classifierId is not None:
            formdata['classifierId'] = classifierId
        #data = parse.urlencode(formdata).encode('utf8')
        rs=requests.post(url2,data=formdata)
        #response = request.urlopen(req)
        if (rs.status_code== 200):
            data = json.loads(rs.content)
            print (data)
            results = data['words_result']
            if len(results)!=0:
                word = results[0]['words']
                return word
            else:
                return '1234'
    except:
        return '11'



'''
def RecogniseGeneral(access_token, image=None, url=None, recognize_granularity='big', language_type='CHN_ENG',
                     detect_direction=False, detect_language=False, vertexes_location=False, probability=False):
    
    通用文字识别（含位置信息）
    :param access_token:URL参数，需要拼接到接口URL上
    :param image:图像数据，base64编码，要求base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效
    :param url:图片完整URL，URL长度不超过1024字节，URL对应的图片base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效，不支持https的图片链接
    :param recognize_granularity:是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
    :param language_type:识别语言类型，默认为CHN_ENG。可选值包括：- CHN_ENG：中英文混合；- ENG：英文；- POR：葡萄牙语；- FRE：法语；- GER：德语；- ITA：意大利语；- SPA：西班牙语；- RUS：俄语；- JAP：日语；- KOR：韩语
    :param detect_direction:是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括:- true：检测朝向；- false：不检测朝向。
    :param detect_language:是否检测语言，默认不检测。当前支持（中文、英语、日语、韩语）
    :param vertexes_location:是否返回文字外接多边形顶点位置，不支持单字位置。默认为false
    :param probability:是否返回识别结果中每一行的置信度
    :return:
    
    host = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=%s' % access_token
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    formdata = {'recognize_granularity': recognize_granularity, 'language_type': language_type,
                'detect_direction': detect_direction, 'detect_language': detect_language,
                'vertexes_location': vertexes_location, 'probability': probability}
    if image is not None:
        formdata['image'] = image
    elif url is not None:
        formdata['url'] = url
    data = parse.urlencode(formdata).encode('utf8')
    req = request.Request(method='POST', url=host, headers=headers, data=data)
    response = request.urlopen(req)
    if (response.status == 200):
        jobj = json.loads(response.read().decode())
        datas = jobj['words_result']
        recognise = {}
        for obj in datas:
            recognise[obj['words']] = obj['location']
        return recognise
image = Image.open(r'90.png')
image = image.convert('L')  #转化为灰度图
threshold = 127             #设定的二值化阈值
table = []                  #table是设定的一个表，下面的for循环可以理解为一个规则，小于阈值的，就设定为0，大于阈值的，就设定为1
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table,'1')  #对灰度图进行二值化处理，按照table的规则（也就是上面的for循环）

'''
def Recognise(img_path):
   # access_token, expires_in = GetAccessToken(ak, sk)  # 将此ak与sk替换成自己应用的值
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data
    # 调用iOCR自定义模板文字识别接口
    # recognise = RecogniseForm(access_token=access_token, image=base64_data,templateSign=templateSign)    # 将此templateSign替换成自己设置的模板值
    #recognise = RecogniseGeneral(access_token=access_token, image=base64_data)
    #for k, v in recognise.items():
       # print(k, v)


if __name__=='__main__':

    list=['75.png','27.png','86.png','15.png','96.png','44.png','54.png','43.png']
    #image='28.png'
    #for img in list:
    prj_path = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(prj_path, 'img') # 图片目录
    a=img_path+"/"+'code.png'
    image1 = Recognise(img_path+"/"+'code.png')
    #print image1
    AK = "N2Rzea28gzaqQ0xG4bmwR6xO"
    SK = "h6RNF7btM6Q03ZP9ukXWc8461XmZzkTd"
    token = GetAccessToken(AK, SK)
    word = RecogniseForm(access_token=token, image=image1)
    print(word)
