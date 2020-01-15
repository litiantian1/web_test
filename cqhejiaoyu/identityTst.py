# author：李迪
# 20180404
# Python3,调用百度云网络文字识别技术，识别验证码

from PIL import Image
from aip import AipOcr


def img_for_str():

    # 注册一个百度云账号，这些信息是注册后就可以会生成的
    # 调用百度云文字识别接口，可参考这篇文章：https://www.jianshu.com/p/bab126354436
    APP_ID = '个人的APP_ID'
    API_KEY = '个人的API_KEY'
    SECRET_KEY = '个人的SECRET_KEY'

    img = open('./tst1.png', 'rb').read()
    result = AipOcr(APP_ID, API_KEY, SECRET_KEY).webImage(img)  # 调用百度云文字识别接口

    # print(result)
    if 'words_result' in result.keys():
        print('原始字符串：', result)
        result_list = str(result['words_result'])
        result_str = result_list[12:20]
        print((result_str.replace(' ', '')).replace('-', ''))   # 去除空格和‘-’，这个实际应用得调整
    else:
        pass


j = 1   # 重复10次识别测试
while True:

    if j <= 10:
        img_for_str()
        j += 1
    else:
        break


