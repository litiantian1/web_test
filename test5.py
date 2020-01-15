# -*-coding:utf-8 -*-
# !user/bin/python

import pandas as pd
import numpy as np

df=pd.read_excel('test.xlsx','Sheet1')
results=df
if results==df:
    print('ok')
else:
    print("Not OK")