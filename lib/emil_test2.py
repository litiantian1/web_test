# coding=utf-8
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.config import *

def send_email(report_file):
    # 1. 编写邮件内容
    with open(report_file) as f:  # 打开html报告
        email_bady = f.read()  # 读取报告内容

    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(email_bady, 'html', 'utf-8'))  # 添加html格式邮件内容

    # 2.组装Email头（发件人、收件人、主题)
    msg['To'] = received  # 收件人
    msg['From'] =sender  # 发件人
    msg['Subject'] = Header('web自动拨测结果', 'utf-8')  # 中文邮件主题

    # 3.构建附件1，传送当前目录下的test.txt文件
    att1 = MIMEImage(open('screen.png', 'rb').read())
    att1['Content-Type'] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment;filename="screen.png"'  # filename 为邮件中的附件名
    msg.attach(att1)  # 添加附件
    try:
    # 4. 连接smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login('1809731547@qq.com', 'qfdwelzckzdncjfj')  # 自己的邮箱地址和密码
        smtp.sendmail(msg.get('From'), msg.get('To'), msg.as_string())  # 接收邮件地址
        print '邮件发送成功'
        logging.info("邮件发送成功2019！")
    except Exception as e:
        print '邮件发送失败'
        print str(e)
        logging.error(str(e))
    finally:
         smtp.quit()

if __name__=='__main__':
    #driver.save_screenshot('screenshot.png')
    # 生成测试报告-错误信息
   # with open('report_{}.html'.format(today), 'w') as f:
       # f.write('test')
    # 发送邮件
    send_email('report_20200121_100200.html')
