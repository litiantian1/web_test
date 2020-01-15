# coding=utf-8
from test.base.basecase import BaseCase
import unittest

'''简化后的登陆用例'''
class TestUserLogin(unittest.TestCase):

    def test_user_login_normal(self):
        """level1:正常登陆""" #leverl1及是一个标签，放在docstring哪里都可以
        case=BaseCase().get_case_data("test_user_data.xlsx","TestUserLogin",'test_user_login_normal')
        #case.get_case_data("test_user_data.xlsx","TestUserLogin","test_user_login_normal")
        BaseCase().send_request(case)

    def test_user_login_password_wrong(self):
        """密码错误登陆"""
        case = BaseCase().get_case_data("test_user_data.xlsx", "TestUserLogin", 'test_user_login_password_wrong')
        BaseCase().send_request(case)

if __name__=='__main__':
    unittest.main(verbosity=2)