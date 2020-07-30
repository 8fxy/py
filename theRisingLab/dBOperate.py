# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:03:41 2020

@author: Fu Xingyu
"""

import connectDB
import pandas as pd
import numpy as np


def sql2df(DBcur, filedName, tabName, filterfield, likeWord):
    # 获取表内数据
    sql_data = "select " + filedName + " from " + tabName + " WHERE " + filterfield + " LIKE " + likeWord + ";"
    print(">>>>>---------------------")
    print(sql_data)
    DBcur.execute(sql_data)
    data = DBcur.fetchall()
    # 获取列名
    cols = [i[0] for i in DBcur.description]
    # sql内表转换pandas的DF
    df = pd.DataFrame(np.array(data), columns=cols)
    print(df)
    return df


db = connectDB.oldRisingDatabase().loginMysql()
cursor = db.cursor()
# select * from TabName WHERE field LIKE likeWord
# "'%%'"
df1 = sql2df(cursor,
             # SELECT
             "year, name_int, city_id, city_name, value_int",
             # FROM
             "du_platform_index_data_int",
             # WHERE
             "name",
             # LIKE
             "'%抖音夜间打卡量%'")
df2 = sql2df(cursor,             # SELECT
             "year, name_int, city_id, city_name, value_int",
             # FROM
             "du_platform_index_data_int",
             # WHERE
             "name",
             # LIKE
             "'%淘票票夜场电影%'")
df3 = sql2df(cursor,
             # SELECT
             "year, name_int, city_id, city_name, value_int",
             # FROM
             "du_platform_index_data_int",
             # WHERE
             "name",
             # LIKE
             "'%TalkingData夜间%'")
df4 = sql2df(cursor,
             # SELECT
             "year, name_int, city_id, city_name, value_int",
             # FROM
             "du_platform_index_data_int",
             # WHERE
             "name",
             # LIKE
             "'%酒吧数量%'")
df5 = sql2df(cursor,
             # SELECT
             "publish_year, name, city_id, city_name, value_int",
             # FROM
             "du_platform_index_data",
             # WHERE
             "name",
             # LIKE
             "'%地铁平均末班车时间%'")
df6 = sql2df(cursor,
             # SELECT
             "publish_year, name, city_id, city_name, value_int",
             # FROM
             "du_platform_index_data",
             # WHERE
             "name",
             # LIKE
             "'%nasa%'")