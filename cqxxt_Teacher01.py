# -*-coding:utf-8 -*-
# !user/bin/python

# coding=utf-8
import os
from selenium import webdriver
import time
import start_stop_Appium
import keyword

appium1 = start_stop_Appium.Appium()
#appium1.start_Appium('127.0.0.1', '4723', '5LMBGM6SBYIRINRS')  # 启动appium
time.sleep(8)
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.4', 'deviceName': '5LMBGM6SBYIRINRS',
                'appPackage': 'com.aspirecn.xiaoxuntongTeacher.cq', 'appActivity': '.MicroschoolTeacher',
                "unicodeKeyboard": "True", "resetKeyboard": "True"}
driver = webdriver.Remote('http://127.0.0.1:4494/wd/hub', desired_caps)  # 启动app
time.sleep(15)
try:
   # driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/home_sign_iv').click()  # 签到
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/notice_ll').click()  # 发通知
    time.sleep(3)
    driver.find_element_by_class_name('android.widget.TextView').click()  # 点击搜索框
    driver.find_element_by_class_name('android.widget.EditText').send_keys(u'李')
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/contact_search_rl').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/btn_confirm').click()  # 确认提交
    # 写通知编辑页面
    # location = appium_location
    # location1 = location.AppLocation
    # location1.By_id_click('com.aspirecn.xiaoxuntongTeacher.cq:id/title_ed')
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/title_ed').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/title_ed').send_keys(u'测试标题')  # 添加标题
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/content_ed').send_keys(u'测试正文测试正文测试正文测试正文测试正文测试正文测试正文测试正文测试正文测试正文测试正文测试正文测试正文')  # 添加正文
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/thumbnailIv').click() #添加图片
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photos_btn').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/group_title').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/child_checkbox').click()
    time.sleep(3)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photo_sel_ok').click()# 点击确认按钮
    time.sleep(3)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/tip_message_tv').click()  # 发布
    time.sleep(3)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/homework_ll').click()  # 布置作业
    time.sleep(2)
    driver.find_element_by_class_name('android.widget.TextView').click()  # 点击搜索框
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/receiver_search_bar').send_keys(u'李')
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/contact_search_rl').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/btn_confirm').click()  # 确认提交
    time.sleep(2)
    # 布置作业编辑页面
    driver.find_element_by_class_name('android.widget.EditText').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/content_ed').send_keys(u'布置作业')
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/thumbnailIv').click() #添加图片
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photos_btn').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/group_title_ll').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/child_checkbox').click()#添加图片
    time.sleep(3)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photo_sel_ok').click()#提交图片
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/tip_message_tv').click()  # 发布
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/evaluate_rl').click()  # 评价学生
    driver.find_element_by_class_name('android.widget.TextView').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/receiver_search_bar').send_keys(u'李')
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/contact_search_rl').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/btn_confirm').click()  # 确定
    # 发评价编辑页面
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_item_pic').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/tip_message_tv').click()  # 发布评价
    time.sleep(2)
    # 通过通讯录发送私聊
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/home_address_book_rl').click()
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/contact_search_bar').click()  # 搜索联系人
    driver.find_element_by_class_name('android.widget.EditText').send_keys(u'李')
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/list_body').click()  # 选择联系人
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_rl').click()
    # 进入与选择联系人的个人聊天界面
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_send_edit').click()
    driver.find_element_by_class_name('android.widget.EditText').send_keys(u'测试私聊信息1')  # 私聊文字发送
    time.sleep(1)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_send_btn').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_action_btn').click()  # 私聊图片发送
    time.sleep(1)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_item_pic').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/group_title_ll').click()  # 选择相册
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/child_checkbox').click()  # 选择相册图片
    time.sleep(3)
    # driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/child_image').click()  # 选择相册图片
    # time.sleep(5)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photo_sel_ok').click()  # 提交所选择的图片
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/emoji_action_btn').click()
    appium1.ABD(209.8, 1489.1)  # 添加表情
    time.sleep(2)
    appium1.ABD(334.7, 1483.1)  # 添加表情
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_send_btn').click()#发送表情
    appium1.ABD(74.9, 1195.4)
    time.sleep(5)
    appium1.ABD_Move(312.7,1830.0,730.2,1824.0,1000)#添加录音
    time.sleep(2)
    appium1.ABD(699.4,1236.4)#发送录音
    time.sleep(3)
    # 返回首页
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/left_btn').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/left_btn').click()
    # 班级-班级动态
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/class_address_rl').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/class_item_rl').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/class_forum_rl').click()
    time.sleep(3)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/pop_menu_item_like_tv').click()  # 班级动态点赞
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/right_btn').click()  # 编辑
    # 发布动态编辑页面
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/content_ed').click()  # 发布文字动态
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/content_ed').send_keys(u'发布班级动态文字测试')
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/tip_message_tv').click()  # 发布
    time.sleep(5)
    # 班级-班级群聊
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/left_btn').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/class_multi_rl').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_send_edit').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_send_edit').send_keys(u'群聊测试文字')
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_send_btn').click()  # 群聊发送文字
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_action_btn').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/msg_item_pic').click()  # 选择相册
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/group_title_ll').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/child_image').click()
    #driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/child_checkbox').click()
    time.sleep(3)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photo_sel_ok').click()  # 发送图片
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/left_btn').click()
    time.sleep(2)
    # 班级-班级相册
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/class_album_rl').click()
    time.sleep(1)
    #com.aspirecn.xiaoxuntongTeacher.cq:id/right_btn
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/right_btn').click()
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photos_btn').click()
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/group_title_ll').click()
    time.sleep(2)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/child_checkbox').click()#添加图片
   # time.sleep(4)
  #  driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/child_checkbox').click()  # 添加图片
    time.sleep(4)
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/photo_sel_ok').click()#确定图片
    time.sleep(4)
    driver.find_element_by_class_name('android.widget.EditText').send_keys(u'相册名称一个')  # 添加相册名
    driver.find_element_by_id('com.aspirecn.xiaoxuntongTeacher.cq:id/tip_message_tv').click()  # 上传相册
   # appium1.stop_Appium('4723')  # 关闭appium服务
    driver.quit()
    os.system('start/b stopAppiumServer.BAT')
except:
    #print '报错了'
    driver.quit()
    appium1.stop_Appium('4723')
    os.system('start/b stopAppiumServer.BAT')
