# coding=utf-8
import unittest
import sys
sys.path.append("../..")
from test.user.test_user_login2 import TestUserLogin
from test.user.test_user_reg2 import TestUserReg

#1 新建TestSuite并添加测试用例
smoke_suite=unittest.TestSuite() # 自定义的TestSuite
smoke_suite.addTests([TestUserLogin('test_user_login_normal'),TestUserReg('test_user_reg_normal')])

def get_suite(suite_name): #获取TestSuite 方法
    return suite_name

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    s=get_suite(smoke_suite)
    runner.run(s)
