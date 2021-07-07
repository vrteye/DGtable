"""
应收票据类别 receivable_bill_category     # api效果
"""
import requests
import numpy as np
from basic import *


def Receivablebillcategory(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        f = get_str_btw(f, '、应收票据', '、应收账款')
        df = CutOutM(f, '）应收票据分类列示', '）本期计提、收回或转回的坏账准备情况')[1]
        df = df.fillna(0)
        df = df.replace(np.nan, 0)
        df.drop(0, inplace=True)
        df.drop(1, inplace=True)
        df.drop(2, inplace=True)
        # df.drop(df.tail(1).index, inplace=True)  # 删除最后一行数据
        df.reset_index(inplace=True, drop=True)
        # print(df)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(Listkeys)
        # print(tableIndex)
        # print('&' * 100)
        jsonText = {'DG': []}

        for item in df.iterrows():
            # print('item[1]:',item[1][-1])
            itemName = item[1][0]  # 项目名称
            firstSurplusAmount = item[1][1]  # 初期余额
            enterpriseMergelAddAmount = round(float(str(item[1][2]).strip('%')) / 100, 4)  # 企业合并本期增加金额
            otherAddAmount = item[1][3]  # 其他本期增加金额
            handleDecrAmount = round(float(str(item[1][4]).strip('%')) / 100, 4)  # 处置本期减少金额
            otherDecrAmount = item[1][5]  # 其他本期减少金额
            lastSurplusAmount = item[1][6]  # 期末余额
            lastAccountRate = round(float(str(item[1][7]).strip('%')) / 100, 4)
            lastBadDebtAmount = round(float(str(item[1][8]).strip('%')) / 100, 4)
            lastBadDebtRate = round(float(str(item[1][9]).strip('%')) / 100, 4)
            lastAccountValue = item[1][10]
            # print('itemName:', itemName, 'firstSurplusAmount:',
            #       firstSurplusAmount, 'exchangerateAddAmount:', enterpriseMergelAddAmount, 'otherAddAmount:',
            #       otherAddAmount,
            #       'handleDecrAmount:', handleDecrAmount, 'otherDecrAmount:', otherDecrAmount, 'lastSurplusAmount:',
            #       lastSurplusAmount)

            jsonText['DG'].append(
                {'itemName': itemName,
                 'firstAccountAmount': firstSurplusAmount,
                 'firstAccountRate': enterpriseMergelAddAmount,
                 'firstBadDebtAmount': otherAddAmount,
                 'firstBadDebtRate': handleDecrAmount,
                 'firstAccountValue': otherDecrAmount,
                 'lastAccountAmount': lastSurplusAmount,
                 'lastAccountRate': lastAccountRate,
                 'lastBadDebtAmount': lastBadDebtAmount,
                 'lastBadDebtRate': lastBadDebtRate,
                 'lastAccountValue': lastAccountValue,

                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/receivableBillCategory/add', json=data)

    except Exception as e:
        print(e)
        pass

