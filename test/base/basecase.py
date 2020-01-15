# coding=utf-8
import unittest
import requests
import json
import sys
sys.path.append('../..') # 统一将包的搜索路径提升至项目根目录下
from config.config import *
import unittest
from lib.read_execl import *
from lib.case_log import log_case_info

class BaseCase():
    def get_case_data(self,data_file,sheet_name,case_name):
        data_list = execl_to_list(os.path.join(data_path, data_file),sheet_name)
        case_data=get_test_data(data_list,case_name)
        return case_data

    def send_request(self,case_data):
        case_name=case_data.get('case_name').encode('utf-8')
        url=case_data.get('url').encode('utf-8')
        args=case_data.get('args')
        headers=case_data.get('headers')
        expect_res=case_data.get('expect_res').encode('utf-8')
        method=case_data.get('data_type')
        data=case_data.get('data').encode('utf-8')
        data_type=case_data.get('data_type').encode('utf-8')
        #print(type(data_type))
        #print(data_type)
        if method.upper()=='GET': #GET类型请求,upper函数 小写转大写
            res=requests.get(url=url)
            restxt=res.text.encode('utf-8')
            log_case_info(case_name,url,data,expect_res,restxt)
        elif data_type=='Form':
            res=requests.post(url=url,data=json.loads(data),headers=json.loads(headers))
            restxt=res.text.encode('utf-8')
            log_case_info(case_name,url,data,expect_res,restxt)
'''
        else:
            res=requests.post(url=url,json=json.loads(args),headers=json.loads(headers))
            log_case_info(case_data,url,args,json.dumps(json.loads(expect_res),sort_keys=True),
                          json.dumps(res.json(),ensure_ascii=False,sort_keys=True))
            self.assertDictEqual(res.json(),json.loads(expect_res))

if __name__=='__main__':
    base=BaseCase()
    case=base.get_case_data("test_user_data.xlsx","TestUserLogin",'test_user_login_normal')
    #print(1)
    base.send_request(case)



'''