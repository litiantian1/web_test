# coding=utf-8
from test.base.basecase import BaseCase
import unittest
import sys
'''引入BsseCase简化后的登陆用例'''
sys.path.append('../..') # 统一将包的搜索路径提升至项目根目录下
from config.config import *
class TestUserReg(unittest.TestCase):
    def test_user_reg_normal(self):
        """level1:正常登陆"""
        case=BaseCase().get_case_data("test_user_data.xlsx","TestUserReg",'test_user_reg_normal')
        BaseCase().send_request(case)
        if not case:
            print("用例数据不存在")

    def test_user_reg_exist(self):
        case = BaseCase().get_case_data("test_user_data.xlsx", "TestUserReg", 'test_user_reg_exist')
        BaseCase().send_request(case)
        if not case:
            print("用例数据不存在")
if __name__=='__main__':
    unittest.main(verbosity=2)
