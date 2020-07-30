# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from csv import reader


def getInvInfo():
    browser = webdriver.Chrome()
    url = 'https://pro.tianyancha.com/'
    browser.get(url)

    # 启动输入账号密码时间在此修改
    time.sleep(30)

    print('Starting...')
    listFailed = []
    listCompCode = []
    cdCounter = 1
    inputNamelist = openNameList()
    for compName in inputNamelist:
        try:
            coolDown(1)
            print('企业名称:' + str(compName) + '  采集中...')
            browser.get(url)
            # 搜索框输入
            searchBox = browser.find_element(By.ID, 'home-main-search')
            coolDown(1)
            searchBox.send_keys(compName)
            coolDown(1)
            searchBox.send_keys(Keys.ENTER)
            coolDown(1)
            # 选择第1个结果
            companyLink = browser.find_element_by_css_selector(
                'div.stdResult-list > div:nth-child(1) > \
                    div.content > div.header > a')
            Link2 = companyLink.get_attribute('href')
            # 获取企业代码
            companyCode = Link2.split('/')[-1]
            # coolDown(2)
            coolDown(1)
            listCompCode.append(companyCode)
            print('成功√')
        except Exception:
            print('采集失败!')
            listCompCode.append('fail')
            listFailed.append(compName)
            totallistFaied = sum(listFailed, [])
            pdFailed = pd.DataFrame({'failed_company': totallistFaied})
            pdFailed.to_csv('CompCodeFailList.csv', encoding='utf-8-sig')
        print('——————————————————————————————')
        if cdCounter % 500 == 0:
            coolDown(3)
            cdCounter += 1
        else:
            coolDown(1)
            cdCounter += 1
    finalNamelist = sum(inputNamelist, [])
    resultTab = pd.DataFrame({'company_name': finalNamelist,
                              'company_code': listCompCode})
    resultTab.to_csv('CompCode.csv', encoding='utf-8-sig')


def openNameList():
    listCompName = list(reader(open('CompName.csv', encoding='utf-8-sig')))
    return listCompName


def coolDown(t):
    if t == 1:
        cdTime = np.random.randint(15, 30, 1)
    if t == 2:
        cdTime = np.random.randint(60, 180, 1)
    if t == 3:
        cdTime = np.random.randint(600, 700, 1)
        print('大CD，休息' + str(cdTime) + '秒...')
    if t == 4:
        cdTime = np.random.randint(1200, 1300, 1)
    time.sleep(cdTime)


if __name__ == '__main__':
    getInvInfo()
    print("完结撒花(~▽~)o∠※PAN!=.:*:'☆.:*:'★':*'")
