# coding=utf-8
import xlrd
import requests
from config.config import *
import os
'''封装读取execl文件'''
'''根据文件名、sheet名、用例名case_name获取某条用例的数据'''
def execl_to_list(data_file,sheet):
    data_list=[] #新建空列表，来装所有数据
    wb=xlrd.open_workbook(data_file) #打开excel
    sh=wb.sheet_by_name(sheet) #获取工作表
    header=sh.row_values(0) #获取标题行数据
    for i in range(1,sh.nrows): #跳过标题行，从第二行开始取数据
        d=dict(zip(header,sh.row_values(i)))
        data_list.append(d)
    return data_list #列表嵌套字典格式，每个元素是一个字典

def get_test_data(data_list,name):
    for case_name in data_list:
        if name==case_name['case_name']:#如果字典数据中case_name与参数一样
            return case_name
            #查询不到会返回None

if __name__=='__main__':
    data_list=execl_to_list(os.path.join(data_path,"test_user_data.xlsx"),"TestUserLogin")#读取execl中TestUserLogin sheet的所有数据
    print(data_list)
    case_data=get_test_data(data_list,'test_user_login_normal')
    args = case_data.get('args')
    data = case_data.get('data')
    print type(data)
