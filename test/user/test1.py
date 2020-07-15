# coding=utf-8
import unittest
import sys
sys.path.append("../..")
import os
from config.config1 import *
def collect(test): #由于使用discover()组装的TestSuite是按文件夹目录多级嵌套的，我们把所有的用例取出来，放在一个无嵌套的TesetSunit中方便使用
    suit=unittest.TestSuite()
    def _collect(tests): #递归,如果下级元素还是TestSuite则继续往下找
        if isinstance(tests,unittest.TestSuite()):
            if tests.countTestCases() !=0:
                for i in tests:
                    _collect(i)
                    print(1)
        else:
            suit.addTest(tests)# 如果下级元素是TestCase，则添加到TestSuite中
            print(3)

    # _collect(discover())
    return suit
if __name__ == "__main__":
    n=os.path.join(prj_path,'test','user')
    discover=unittest.defaultTestLoader.discover(n,pattern="test_user*.py",top_level_dir=None)
    #suit=unittest.TestSuite() # suit == discover
    print(discover.methods())
    #runner=unittest.TextTestRunner()
    #runner.run(discover)
