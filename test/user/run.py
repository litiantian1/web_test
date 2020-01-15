# coding=utf-8
import unittest
from config.config import *
from lib.emil_test2 import send_email
from test.suite.test_suites import *
from lib.HTMLTestRunner import HTMLTestRunner
import time
import pickle
def discover():
    return unittest.defaultTestLoader.discover(test_path,pattern="test_*.py",top_level_dir=None)

def run(suite):
    logging.info("=============测试开始=============")
    with open(report_file,'r+') as f:
        result=unittest.TextTestRunner(stream=f,descriptions="测试报告",verbosity=2).run(suite)
    if result.failures: #保存失败用例序列化文件
        save_failures(result,last_fails_file)

    #是否发生邮件
    if send_email_after_run:
        send_email(report_file)
    logging.info("===========测试结束======================")
def run_all(): #运行所有用例
    run(discover())

def run_suite(suite_name):#运行`test/suite/test_suites.py`文件中自定义的TestSuite
    suit=get_suite(suite_name)
    print(suit.countTestCases())
    if suit:
        run(suit)
    else:
        print("TestSuite不存在")

   #runner=unittest.TextTestRunner()
#runner.run(smoke_suite)
'''列出所有用例'''
def collect(): #由于使用discover()组装的TestSuite是按文件夹目录多级嵌套的，我们把所有的用例取出来，放在一个无嵌套的TesetSunit中方便使用
    suit=unittest.TestSuite()
    def _collect(tests): #递归,如果下级元素还是TestSuite则继续往下找
        if isinstance(tests,unittest.TestSuite()):
            if tests.countTestCases() !=0:
                for i in tests:
                    _collect(i)
        else:
            suit.addTest(tests)# 如果下级元素是TestCase，则添加到TestSuite中

    # _collect(discover())
    return suit

def collect_only():#仅列出所用用例
    t0=time.time()
    i=0
    for case in collect():
        i +=1
        print("{}.{}".format(str(i),case.id()))
    print("==========================================")
    print("Collect {} test is {:3f}s".format(str(i),time.time()-t0))

def makesuite_by_testlist(testlist_file):
    with open(testlist_file, 'r+') as f:
        test_case_name = f.readlines()

    testlist=[i.strip() for i in test_case_name if not i.startswith("#")]# 去掉每行结尾的"/n"和 #号开头的行

    #print testlist
    suite=unittest.TestSuite()
    all_cases=collect()
    print all_cases

    for case in all_cases: #从所有用例中匹配用例方法名
        if case._testMethodName in testlist:
            suite.addTest(case)
        print suite
    return suite
def makesuite_by_tag(tag):
    suite=unittest.TestSuite()
    for case in collect():
        if case._testMethodName and tag in case._testMethodDoc:# 如果用例方法存在docstring,并且docstring中包含本标签
            suite.addTest(case)
    return suite

def save_failures(result,file):# file为序列化保存的文件名，配置在config/config.py中
    suite=unittest.TestSuite()
    for case_result in result.failures:  # 组装TestSuite
        suite.addTest(case_result[0]) # case_result是个元祖，第一个元素是用例对象，后面是失败原因等等

        with open(file,'wb') as f:
            pickle.dump(suite,f) #  序列化到指定文件pickle函数的功能：将obj对象序列化存入已经打开的file中

def rerun_fails(): #失败用例重跑的方法
    sys.path.append(test_path) # 需要将用例路径添加到包搜索路径中，不然反序列化TestSuite会找不到用例
    with open(last_fails_file,'rb') as f:
        suite=pickle.load(f)  #反系列化得到TestSuiet
    run(suite)

def main():
    if options.collect_only: #如果指定了--collect-only参数
        collect_only()
    elif options.rerun_fails: #如果指定了--rerun-fails参数
        rerun_fails()
    elif options.testlist: # 如果指定了--testlist参数
        run(makesuite_by_testlist(testlist_file))
    elif options.testsuite: # 如果指定了--testsuite参数
        run_suite(options.testsuite)
    elif options.tag:
        run(makesuite_by_tag(options.tag))
    else:
        run_all() #否则，运行所有用例
if __name__=='__main__':
    run_suite(smoke_suite)
    #collect()
    #makesuite_by_testlist(testlist_file)