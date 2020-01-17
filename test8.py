# coding=utf-8
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from cqhejiaoyu_web import *
from pyvirtualdisplay import Display
from selenium import webdriver
Url = 'http://www.cqhejiaoyu.com/'

# 设置为无界面浏览器
options = Options()
options.add_argument('--headless')

# 打开浏览器
#option = webdriver.Firefox(options=options)
# 现在firefox会运行在一个虚拟屏幕中
# 你看不到它
#option = webdriver.FirefoxProfile()
#option.set_preference("plugin.state.flash", 2)
#option.add_extension('--headless--')
#driver = webdriver.Firefox(option)
driver = webdriver.Firefox(options=options)
time.sleep(2)
driver.maximize_window()
driver.get(Url)
time.sleep(2)
try:
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[1]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('.//*[@id="mobile"]').send_keys('13983132059')
    time.sleep(2)
    driver.find_element_by_xpath('.//*[@id="passwd"]').send_keys('Dc123456~')
    print '输入验证码'
    time.sleep(6)
    #driver.find_element_by_xpath('.//*[@id="verify"]').send_keys('1234')
    time.sleep(4)
    driver.find_element_by_xpath(".//*[@id='loginForm']/li[4]/button").click()
    print'点击登陆按钮'
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/form/ul/li/p[1]/span[1]/input").click()
    driver.find_element_by_xpath('.//*[@id="loginForm"]/p/input').click()
    time.sleep(4)
    print '登陆成功'
    # 点击家校互动
    driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul/li[2]/a").click()
    time.sleep(4)
    print '进入家校互动模块'
    # 点击家校短信 模块
    driver.find_element_by_xpath(".//*[@id='tab2']/a").click()
    time.sleep(4)
    '''
    print '选择联系人'
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[4]/div[3]/div[1]/div[1]/select/option[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[4]/div[3]/div[1]/div[3]/input[5]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[4]/div[3]/div[5]/input[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[4]/div[3]/div[5]/input[4]").click()
    # 添加发送主题和内容
    driver.find_element_by_xpath('//*[@id="title"]').send_keys(u'web测试发送作业主题')
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="content"]').send_keys(u'web测试发送作业正文web测试发送作业正文web测试发送作业正文')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sendButton"]').click()
    print '留言发送成功'
    '''
    # 成绩
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='examScore']").click()
    time.sleep(4)
    # iframe 定位
    # 考试名称
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
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/form/div/table/tbody/tr[16]/td[2]/input[1]").click()
    time.sleep(2)
    driver.switch_to.default_content()
    print '成绩发送成功'
    time.sleep(6)
except EOFError:
    print EOFError
finally:
    driver.quit()