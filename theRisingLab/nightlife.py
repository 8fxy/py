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


def normalize(df1):
    listNewdf1 = []
    for _ in df1:
        newdf1 = (_ - df1.min()) / (df1.max() - df1.min())
        newdf1 = newdf1 * 100
        listNewdf1.append(newdf1)
    df1 = pd.DataFrame(df1)
    df1["value_normal"] = listNewdf1
    df1 = df1.value_normal
    return df1


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
df7 = sql2df(cursor,
             # SELECT
             "year, name, city_id, city_name, value_int",
             # FROM
             "du_platform_index_data_int",
             # WHERE
             "name",
             # LIKE
             "'%公交夜间活跃范围%'")

df8 = sql2df(cursor,
             # SELECT
             "year, name, city_id, city_name, value_int",
             # FROM
             "du_platform_index_data_int",
             # WHERE
             "name",
             # LIKE
             "'%夜间出行活跃度%'")
db.close()

df = pd.DataFrame()

df1 = df1[df1.year == 2019]
df = df1.city_name
df = pd.DataFrame(df)
df.index = df1.city_id
df1.index = df1.city_id
df1 = df1.value_int
df1 = normalize(df1)
df1 = pd.DataFrame(df1)
df1.columns = ["抖音夜间打卡量"]
df = df.join(df1)

df2.index = df2.city_id
df2 = df2.value_int
df2 = normalize(df2)
df2 = pd.DataFrame(df2)
df2.columns = ["淘票票夜场电影次数"]
df = df.join(df2)

df3.index = df3.city_id
df3 = df3.value_int
df3 = normalize(df3)
df3 = pd.DataFrame(df3)
df3.columns = ["TalkingData夜间活跃设备占比"]
df = df.join(df3)

df4 = df4[df4.year == 2020]
df4.index = df4.city_id
df4 = df4.value_int
df4 = normalize(df4)
df4 = pd.DataFrame(df4)
df4.columns = ["酒吧数量"]
df = df.join(df4)

df5 = df5[df5.publish_year == 2020]
df5.index = df5.city_id
df5 = df5.value_int
df5 = pd.DataFrame(df5)
df5.columns = ["地铁平均末班车时间"]
df = df.join(df5)

df6 = df6[df6.publish_year == 2020]
df6.index = df6.city_id
df6 = df6.value_int
df6 = normalize(df6)
df6 = pd.DataFrame(df6)
df6.columns = ["NASA夜间灯光强度"]
df = df.join(df6)

df7 = df7[df7.year == 2020]
df7.index = df7.city_id
df7 = df7.value_int
df7 = normalize(df7)
df7 = pd.DataFrame(df7)
df7.columns = ["城市公交夜间活跃范围占比"]
df = df.join(df7)

df8 = df8[df8.year == 2019]
df8.index = df8.city_id
df8 = df8.value_int
df8 = pd.DataFrame(df8)
df8.columns = ["夜间出行活跃度"]
df = df.join(df8)

# 去重
df = df.drop_duplicates()
df.to_csv("ODS-nightLife(normalized).csv", encoding="GBK")
