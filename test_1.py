# -*-coding:utf-8 -*-
# !user/bin/python

import csv
#csv写入
import re

my_file = 'D:\\abc\\wabiPW.csv'
'''
#csv_file=csv.reader(open(my_file,'r'))
#for stu in csv_file:
#    print(stu)
phone='1563737'
pw='6789'
stu1=[phone,pw]
with open(my_file,'a',) as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(stu1)
'''
my_file = 'D:\\abc\\wabi.csv'
my_file_PW = 'D:\\abc\\wabiPW.csv'
data = csv.reader(file(my_file, 'rb'))
# 循环输出每一行信息：
a = []
for user in data:
   a.append(user[0][0:11])
print(a)
#for index in range(len(a)):
    #print(a[index])