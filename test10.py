# coding=utf-8
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time
url = 'http://www.cqhejiaoyu.com/'

#option = webdriver.FirefoxProfile()
#option.set_preference("plugin.state.flash", 2)
#driver = webdriver.Firefox(option)
# 设置chrome为无界面浏览器
options = Options()
options.add_argument('--headless')

# 打开浏览器
#driver = webdriver.Firefox(options=options)

#设置允许flash
option = webdriver.FirefoxProfile()
option.set_preference("plugin.state.flash", 2)

# 打开浏览器
driver = webdriver.Firefox(option,options=options)

# 利用get请求请求浏览器的一个网页
driver.get(url=url)
# 现在firefox会运行在一个虚拟屏幕中
# 你看不到它
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[1]/a').click()
time.sleep(2)
driver.find_element_by_xpath('.//*[@id="mobile"]').send_keys('13983132059')
time.sleep(2)
driver.find_element_by_xpath('.//*[@id="passwd"]').send_keys('Dc123456~')

# 打印输出这个网页的源代码
print(driver.find_element_by_xpath(".//*[@id='thismy2_Tab']/ul/li[1]").text)
#driver.close()
driver.quit()
# 杀死chrome浏览器的连接桥(chromedriver)的进程
#driver.quit()