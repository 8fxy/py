# -*- coding: UTF-8 -*-
import tushare as ts
import time
import pandas as pd
import csv
# 初始化tushare

#ts.set_token('5f35142b3c5a875fceda0d60282e9d138730a0966d91d4cda218a893')
#pro = ts.pro_api()

api = ts.pro_api('5f35142b3c5a875fceda0d60282e9d138730a0966d91d4cda218a893')
filename = 'hs300.csv'
with open(filename) as f:
    csv_data = pd.read_csv(filename, low_memory=False)  # 防止弹出警告
    df = pd.DataFrame(csv_data)

for code in  df['ts_code']:
    print(code)
    result = ts.pro_bar(pro_api=api,
                        ts_code= code,
                        start_date='20190101',
                        end_date='20190305',
                        adj='qfq',
                        exchange='')
    writer = pd.ExcelWriter('H://quant//svm//data//' + code + '.xlsx')
    result.to_excel(writer, index=False)
    writer.close()

'''

def getstockpool():
    pool = pro.stock_basic(exchange='',list_status='L',adj='qfq',
                           fields='ts_code,symbol,name,area,industry,fullname,list_date, market,exchange,is_hs')
    print('获得上市股票总数：',len(pool)-1)
    return pool

if __name__ == '__main__':
    stockpool = getstockpool()['ts_code']
    j = 1
    for i in stockpool[2922:]:
        print('正在获取第%d家，股票代码%s.'%(j, i))
        time.sleep(0.301)
        j += 1
        df = pro.daily(ts_code=i,start_date='20170304',end_date='20190304',
                       fields='ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount')
        writer = pd.ExcelWriter('H://quant//c//' + i + '.xlsx')
        df.to_excel(writer, sheet_name = i+'',index=False)
'''

'''
['ts_code', 'pro_api', 'start_date', 'end_date', 'asset', 'adj', 'freq', 'ma', 'factors']
['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close', 'change', 'pct_chg', 'vol', 'amount']
'''
