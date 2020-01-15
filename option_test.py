# -*-coding:utf-8 -*-
#!/usr/bin/python
#下拉框定位测试
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

url="file:///C:/Users/issue/Desktop/option.html"
driver=webdriver.Firefox()
driver.get(url)
#先定位到下拉框
time.sleep(2)
#driver.find_element_by_xpath(".//*[@id='ShippingMethod']/option[3]").click()
m=Select(driver.find_element_by_id("ShippingMethod"))
#再点击下拉框的选项
time.sleep(2)
#m.find_element_by_xpath("//option[@value='10.69']").click()
m.select_by_value("10.69")
#m.select_by_visible_text("10.69")
time.sleep(6)
driver.quit()