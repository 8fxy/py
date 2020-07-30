# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:29:44 2020

@author: Fu Xingyu
"""

import MySQLdb
import psycopg2


class oldRisingDatabase():
    def loginMysql(self):
        self = MySQLdb.connect(host="",
                               port=3306,
                               user="",
                               password="",
                               db="",
                               charset='utf8mb4')
        print("SQL数据库 连接成功！")
        return self


class newRisingDatabase():
    def loginPgSQL(self):
        self = psycopg2.connect(database="",
                                user="",
                                password="",
                                host="",
                                port="5432")
        print("postgreSQL数据库 连接成功！")
        return self


def sql2df(DBcur, TabName, field, likeWord):
    # 获取表内数据
    sql_data = "select * from " + TabName + " WHERE " + field + " LIKE " + likeWord
    print("___________________________________________")
    print(sql_data)
    DBcur.execute(sql_data)
    data = DBcur.fetchall()
    # 获取列名
    cols = [i[0] for i in DBcur.description]
    # sql内表转换pandas的DF
    df = pd.DataFrame(np.array(data), columns=cols)
    return df

'''
db = oldRisingDatabase().loginMysql()
print(db)
cursor = db.cursor()
sql = "SELECT * FROM du_platform_index_data_int WHERE name_int LIKE '%抖音%'"

# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print(results)
for row in results:
    print(row)


db.close()
'''