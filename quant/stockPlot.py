# -*- coding: UTF-8 -*-
import tushare as ts
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.ticker as ticker

#print(tushare.__version__) #显示版本
ts.set_token('5f35142b3c5a875fceda0d60282e9d138730a0966d91d4cda218a893')
pro = ts.pro_api()
df = pro.daily(ts_code='600104.SH', start_date='20120601', end_date='20190228',fields='ts_code, trade_date, close')
df2 =pro.daily(ts_code='000651.SZ', start_date='20120601', end_date='20190228',fields='ts_code, trade_date, close')
ind = np.arange(len(df))
print(df)

xs = [datetime.strptime(d, '%Y%m%d').date() for d in df.trade_date]
xs2 = [datetime.strptime(d, '%Y%m%d').date() for d in df2.trade_date]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y%m')) #设置时间显示格式
plt.gca().xaxis.set_major_locator(mdates.YearLocator()) #月初标记
plt.plot(xs, df.close,'-',label='000002.SZ')
plt.plot(xs2, df2.close,'-',label='000651.SZ')
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.legend()

#plt.xticks(fontsize=7)
'''
fig, ax = plt.subplots(1, 1)
plt.plot(df.trade_date, df.close, '-')
ax.invert_xaxis()
for label in ax.get_xticklabels():
    label.set_visible(False)
for label in ax.get_xticklabels()[::int(len(df)/5)]:
    label.set_visible(True)
fig.autofmt_xdate()
'''

'''
def format_date(x, pos=None):
    thisind = np.clip(int(x + 0.5), 0, len(df) - 1)
    return df.trade_date[thisind]

fig, axes = plt.subplots()
ax = axes
ax.plot(ind, df.close, '-')
ax.invert_xaxis()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
fig.autofmt_xdate()
'''

plt.show()
