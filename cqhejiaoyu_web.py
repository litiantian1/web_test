# -*-coding:utf-8 -*-
#!/usr/bin/python
#重庆和教育-家校共育
from selenium import webdriver
import baiduORC
import base64
from lib.emil_test2 import *
from selenium.webdriver.firefox.options import Options


Url='http://www.cqhejiaoyu.com/'

# 设置无界面浏览器
options = Options()
options.add_argument('--headless')

#设置允许flash
option = webdriver.FirefoxProfile()
option.set_preference("plugin.state.flash", 2)

# 打开浏览器
driver = webdriver.Firefox(option,options=options)
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
driver.find_element_by_xpath('.//*[@id="passwd"]').send_keys('Dc123456~')
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
    logging.info("识别结果")
    print("识别结果")
    print(word)
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
            logging.info("登陆成功")
            print '登陆成功'
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
        logging.info("重新处理验证码")
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
def School_message():
    # 点击家校短信 模块
    driver.find_element_by_xpath(".//*[@id='tab2']/a").click()
    time.sleep(4)
    print '选择联系人'
    #选择发送人-初四五班
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[4]/div[3]/div[1]/div[1]/select/option[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[4]/div[3]/div[1]/div[3]/input[5]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[4]/div[3]/div[5]/input[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[4]/div[3]/div[5]/input[4]").click()
    #添加发送主题和内容
    driver.find_element_by_xpath('//*[@id="title"]').send_keys(u'web测试发送作业主题')
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="content"]').send_keys(u'web测试发送作业正文web测试发送作业正文web测试发送作业正文')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sendButton"]').click()
    print '留言发送成功'
    time.sleep(4)
def School_notice():
    #通知
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='notice']").click()
    time.sleep(4)
    #选择年级
    try:
        driver.find_element_by_xpath(".//*[@id='gradeId']/option[3]").click()
    except:
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='notice']").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='gradeId']/option[3]").click()
    time.sleep(2)
    #driver.find_element_by_xpath(".//*[@id='receiverListDiv']/ul/li[1]").click()#选择班级
    #全选与确定
    #//*[@id="receiverListDiv"]/div/input[2]
    driver.find_element_by_xpath('//*[@id="receiverListDiv"]/div/input[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="receiverListDiv"]/div/input[4]').click()
    time.sleep(2)
    #driver.find_element_by_xpath(".//*[@id='receiverListDiv']/div/input[4]").click()
    driver.find_element_by_xpath(".//*[@id='title']").send_keys(u"通知测试主题添加")
    time.sleep(4)
    driver.find_element_by_xpath(".//*[@id='content']").send_keys(u"测试通知正文添加通知正文添加")
    driver.find_element_by_xpath(".//*[@id='sendButtom']").click()
    print '通知发送成功'
    time.sleep(8)
def School_homework():
    #作业
    driver.find_element_by_xpath(".//*[@id='homework']").click()
    time.sleep(4)
    driver.find_element_by_xpath(".//*[@id='classId']/option[3]").click()#选择班级
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='receiverListDiv']/div[5]/input[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='receiverListDiv']/div[5]/input[4]").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='subjectId']/option[2]").click()#选择科目
    driver.find_element_by_xpath(".//*[@id='title']").send_keys(u"家庭作业添加主题")
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='content']").send_keys(u"家庭作业正文添加")
    driver.find_element_by_xpath(".//*[@id='sendButton']").click()
    print '作业发送成功'
    time.sleep(6)
def School_comment():
    #评语
    driver.find_element_by_xpath(".//*[@id='comment']").click()
    time.sleep(4)
    driver.find_element_by_xpath(".//*[@id='classId']/option[3]").click()  # 选择班级
    time.sleep(4)
    driver.find_element_by_xpath(".//*[@id='receiverListDiv']/div[5]/input[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='receiverListDiv']/div[5]/input[4]").click()
    time.sleep(2)
    #文本添加
    driver.find_element_by_xpath(".//*[@id='title']").send_keys(u"评语添加主题")
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='content']").send_keys(u"评语正文添加")
    driver.find_element_by_xpath(".//*[@id='sendButton']").click()
    print '评语发送成功'
    time.sleep(6)
def School_Score():
    #成绩
    driver.find_element_by_xpath(".//*[@id='examScore']").click()
    time.sleep(4)
    #iframe 定位
    #考试名称
    driver.switch_to.frame("rightFrame3")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]/option[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='clazzId']/option[3]").click()
    # 科目选择
    time.sleep(2)
    driver.maximize_window()
    print '选择科目'
    time.sleep(5)
    #driver.find_element_by_xpath(".//*[@id='subjectQuiz4028828D471125F5014718EF56057916']").click()
    #time.sleep(18)
    m=driver.find_element_by_id("switchExamMessageSubject")
    time.sleep(2)
    input=m.find_element_by_tag_name('input')
    time.sleep(2)
    #//*[@id="subjectQuiz4028828D471125F5014718EF56057916"]
    if input.get_attribute('type')=='checkbox':
        input.click()
        print '科目选择成功'
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/form/div/table/tbody/tr[16]/td[2]/input[1]").click()
    time.sleep(2)
    driver.switch_to.default_content()
    print '成绩发送成功'
    time.sleep(6)
def School_Communication():
    #校园通信-个人
    driver.find_element_by_xpath(".//*[@id='tab3']/a").click()
    time.sleep(4)
    #选择组//*[@id="menu1"]/a
    driver.find_element_by_xpath(".//*[@id='groupId']/option[6]").click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="receiverList"]/div[6]/input[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="receiverList"]/div[6]/input[4]').click()
    time.sleep(2)
    #文本添加
    driver.find_element_by_xpath(".//*[@id='title']").send_keys(u"个人短信主题")
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='content']").send_keys(u"个人短信正文添加")
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='sendButton']").click()
    time.sleep(4)
    # 校园通信-分组
    driver.find_element_by_xpath(".//*[@id='menu2']/a").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='show_all']").click()
    time.sleep(4)
    #分组选择
    driver.find_element_by_xpath('//*[@id="receiverList"]/div[2]/input[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="receiverList"]/div[2]/input[4]').click()
    #分组文本添加
    driver.find_element_by_xpath(".//*[@id='title']").send_keys(u"分组短信主题")
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='content']").send_keys(u"分组短信正文添加")
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='sendButton']").click()
    time.sleep(2)
    driver.find_element_by_xpath("html/body/form/div/table/tbody/tr[16]/td[2]/input[1]").click()
    print '成绩发送成功'
    time.sleep(4)
if __name__=='__main__':
    try:
        # 获取token
        AK = "N2Rzea28gzaqQ0xG4bmwR6xO"
        SK = "h6RNF7btM6Q03ZP9ukXWc8461XmZzkTd"
        token = baiduORC.GetAccessToken(AK, SK)
        web_login()
        #点击家校互动
        driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul/li[2]/a").click()
        time.sleep(4)
        print '进入家校互动模块'
        School_message()
        School_notice()
        School_homework()
        School_Score()
        print '拨测执行完成'
        with open('report_{}.html'.format(today),'w') as f:
            f.write(now)
            f.write('pass')
            print now
        #发送邮件
        now_data=now
        print 'report_'+now_data+'.html'
        send_email('report_'+now_data+'.html')
        print 'pass 邮件发送成功'
        #School_Communication()
    except EOFError:
        print EOFError
        #屏幕截图
        driver.save_screenshot('screenshot.png')
        #生成测试报告-错误信息
        with open('report_{}.html'.format(today),'w') as f:
            f.write(EOFError)
            print now
        #发送邮件
        error_now=now
        print 'report_'+error_now+'.html'
        send_email('report_'+error_now+'.html')
        print EOFError
        print 'error 邮件发送成功'
    finally:
        driver.quit()