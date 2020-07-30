# -*- coding: UTF-8 -*-
import tushare as ts
import time
import pandas as pd
# 初始化tushare
ts.set_token('5f35142b3c5a875fceda0d60282e9d138730a0966d91d4cda218a893')
pro = ts.pro_api()

data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,industry')
writer = pd.ExcelWriter('stockcodelist.xlsx')
data.to_excel(writer,index=False)

print(data.head())