# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import os
from selenium import webdriver
import time
import start_stop_Appium

appium1 = start_stop_Appium.Appium()
appium1.start_Appium('127.0.0.1', '4723', '127.0.0.1:62001')  # 启动appium
time.sleep(8)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.2', 'deviceName': '127.0.0.1:62001',
                'appPackage': 'com.aspirecn.xiaoxuntongParent.cq', 'appActivity': '.MicroschoolParent',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
time.sleep(10)
class cqxxt_Parent(object):
    #def __init__(self,desired_caps):
      #  self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
    def Homewrok(self):
        #查看家庭作业
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/wrap_layout').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/ll_content').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()#返回首页
    def Schoolnotice(self):
        #查看学校通知
        appium1.ABD(449.6,698.5)
        time.sleep(3)
        appium1.ABD(567.5,344.7)
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()#返回首页
    def Teachevalua(self):
        #查看教师评语
        appium1.ABD(937,717.5)
        time.sleep(3)
        appium1.ABD(431.6,849.5)
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/title_tv').click()
        #driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/evaluate_rl').click()
        #driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/title_tv').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()#返回首页
    def Message(self):
        #查看/发送个人消息
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/home_message_rl').click()#查看消息列表
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/topic_contact_name').click()#点击第一条消息
        #driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_send_edit').click()#私聊发送消息
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_send_edit').send_keys(u'测试单聊文字消息')
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_send_btn').click()#发送
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/emoji_action_btn').click()#发送表情
        time.sleep(2)
        appium1.ABD(209.8, 1489.1)  # 添加表情
        time.sleep(2)
        appium1.ABD(334.7, 1483.1)  # 添加表情
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_send_btn').click()#发送
        appium1.ABD(74.9, 1195.4)
        time.sleep(5)
        appium1.ABD_Move(312.7, 1830.0, 730.2, 1824.0, 1000)  # 添加录音
        time.sleep(2)
        appium1.ABD(699.4, 1236.4)  # 发送录音
        time.sleep(3)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_switch_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_action_btn').click()#发送图片
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_item_pic').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/group_title_ll').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/child_checkbox').click()
        time.sleep(4)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/photo_sel_ok').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()#返回首页
    def Class1(self):
        appium1.ABD(673.4,712.5)
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/class_item_rl').click()
        #班级群聊
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/class_multi_rl').click()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_send_edit').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_send_edit').send_keys(u'班级群聊文字消息')
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_send_btn').click()#发送
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/emoji_action_btn').click()#发送表情
        appium1.ABD(209.8, 1489.1)  # 添加表情
        time.sleep(2)
        appium1.ABD(334.7, 1483.1)  # 添加表情
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_send_btn').click()#发送表情
        appium1.ABD(74.9, 1195.4)
        time.sleep(5)
        appium1.ABD_Move(312.7, 1830.0, 730.2, 1824.0, 1000)  # 添加录音
        time.sleep(2)
        appium1.ABD(699.4, 1236.4)  # 发送录音
        time.sleep(3)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_switch_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_action_btn').click()#发送图片
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/msg_item_pic').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/group_title_ll').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/child_checkbox').click()
        time.sleep(4)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/photo_sel_ok').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()#返回班级页
        #班级动态
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/class_forum_rl').click()
        time.sleep(4)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/right_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/content_ed').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/content_ed').send_keys(u'班级动态文字/图片测试')
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/thumbnailIv').click()
        time.sleep(2)
        appium1.ABD(530.5,1697.0)
        time.sleep(2)
        #driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/photos_btn').click()
      #  530.5 1697.0
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/group_title_ll').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/child_checkbox').click()
        time.sleep(3)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/photo_sel_ok').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/tip_message_tv').click()
        time.sleep(3)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()
        #班级相册
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/class_album_rl').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/right_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/photos_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/group_title_ll').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/child_checkbox').click()
        time.sleep(3)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/photo_sel_ok').click()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/content_ed').send_keys(u'班级相册1')
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/tip_message_tv').click()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/left_btn').click()
    def EduCircle(self):
        time.sleep(8)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/img_teacher_community').click()
        time.sleep(8)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/community_infor_iv').click()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/input_reply_ed').send_keys(u'点赞')
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/send_reply_btn').click()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/web_back_btn').click()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/img_home')
    def Live(self):
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/img_live').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/iv_image').click()
        time.sleep(10)
        appium1.ABD(979,1300.3)
        time.sleep(8)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/web_back_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/web_back_btn').click()
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/img_home').click()
    def Growup(self):
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/img_grow_up').click()
        appium1.ABD(481.5,447.7)
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/web_back_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/iv_image').click()#打开妙笔作文
        time.sleep(2)
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/web_back_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/img_home').click()
    def Myself(self):
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/img_myself').click()
        #driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/sign_aw_iv').click()#未签到
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/signed_tv').click()#已签到
        time.sleep(5)
        #driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/sigin_close_iv').click()#关闭签到提示框
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/myself_jx_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/web_back_btn').click()
        driver.find_element_by_id('com.aspirecn.xiaoxuntongParent.cq:id/img_home').click()

if __name__=='__main__':
    try:
        Parent1=cqxxt_Parent()
        Parent1.Homewrok()
        time.sleep(3)
        Parent1.Schoolnotice()
        time.sleep(3)
        Parent1.Teachevalua()
        time.sleep(3)
        Parent1.Message()
        time.sleep(3)
        Parent1.Class1()
        Parent1.EduCircle()
        time.sleep(3)
        Parent1.Live()
        time.sleep(2)
        Parent1.Growup()
        time.sleep(2)
        Parent1.Myself()
        os.system('start/b stopAppiumServer.BAT')
    except:
        print ('出错了')
        os.system('start/b stopAppiumServer.BAT')




















