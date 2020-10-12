# -*-coding:utf-8 -*-
# !user/bin/python
#测试Selenium2(WebDriver)_如何判断WebElement元素对象是否存在
from selenium import webdriver
from pyvirtualdisplay import Display
import time

display=Display(visible=0,size=(1080,900))
display.start() #打开虚拟界面
Url='https://www.baidu.com/'
driver=webdriver.Chrome()
driver.get(Url)
try:
    driver.find_element_by_xpath(".//*[@id='kw']").send_keys(u'月季')
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='su']").click()
    time.sleep(8)
except:
    print('执行分支语句')
    time.sleep(4)
    driver.find_element_by_xpath(".//*[@id='form']/div/ul/li[4]").click()
finally:
    time.sleep(4)
    driver.quit()