# coding=utf-8
import logging
import os
import optparse
import time
# 项目路径
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# 当前文件决定路径的上一级，__file__当前文件;增加一级

data_path=os.path.join(prj_path,'data') #数据目录，暂时在项目目录下
test_path=os.path.join(prj_path,'test') # 测试用例目录
file=prj_path
last_fails_file=prj_path

'''新增log功能---按天生成log,每次生成新的报告'''
today=time.strftime('%Y%m%d',time.localtime())
now=time.strftime('%Y%m%d_%H%M%S',time.localtime())

log_file=os.path.join(prj_path,'log','log_{}.txt'.format(today)) #更改路径到log目录下
report_file=os.path.join(prj_path,'lib','report_{}.html'.format(today)) #更改路径到report 目录下
testlist_file=os.path.join(prj_path,'data','testlist.txt')
'''新增log功能---按天生成log'''

logging.basicConfig(level=logging.DEBUG, # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s', #log 格式
                    datefmt='%Y-%m-%d %H:%M:%S', #日期格式
                    filename=log_file,
                    filemode='a',
                    StreamHandler=()) #追加格式

'''数据库配置'''
db_host='172.0.9.0' #自己的服务器地址
db_port=3306
db_user='test'
db_password='123456'
da='api_test'

#邮件配置
send_email_after_run=False  #增加send_email（）开关

smtp_server='smtp.qq.com'
smtp_user='1809731547@qq.com'
smtp_password='qfdwelzckzdncjfj' #授权码

sender=smtp_user #发件人
received='lichunhua@aspirecn.com' #收件人
subject='接口测试报告' #邮件主题

'''命令行选项'''
parser= optparse.OptionParser()
parser.add_option('--collect-only',action='store_true',dest='collect_only',help='仅列出所有用例')
parser.add_option('--rerun-fails',action='store_true',dest='rerun_fails',help='运行上次失败的用例')
parser.add_option('--testlist',action='store_true',dest='testlist',help='运行test/testlist.txt列表指定用例')
parser.add_option('--testsuite',action='store',dest='testsuite',help='运行指定的TestSuite')
parser.add_option('--tag',action='store',dest='tag',help='运行指定tag的用例')

(options,args)=parser.parse_args() # 应用选项（便生效）
if __name__ == '__main__':
    logging.info("hello")
    logging.info("test:{}".format('123'))
