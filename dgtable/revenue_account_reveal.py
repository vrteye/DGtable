"""
应收账款分类披露 revenue_account_reveal  API
"""
import requests
import numpy as np
from basic import *

def Revenueaccountreveal(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        df = CutOutM(f, '）应收账款分类披露', '按单项计提坏账准备：')
        df = df.fillna(0)
        df = df.replace(np.nan, 0)
        df.drop(0, inplace=True)
        df.drop(1, inplace=True)
        df.drop(2, inplace=True)
        df.drop(3, inplace=True)
        df.drop(4, inplace=True)
        df.drop(5, inplace=True)
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
            try:
                # print('item[1]:',item[1][-1])
                itemName = item[1][0]  # 项目名称
                firstSurplusAmount = item[1][1]  # 初期余额
                enterpriseMergelAddAmount = round(float(str(item[1][2]).strip('%')) / 100, 4)  # 企业合并本期增加金额
                otherAddAmount = item[1][3]  # 其他本期增加金额
                handleDecrAmount = round(float(str(item[1][4]).strip('%')) / 100, 4)  # 处置本期减少金额
                otherDecrAmount = item[1][5]  # 其他本期减少金额
                lastSurplusAmount = item[1][6]  # 期末余额
                lastBadDebtAmount = round(float(str(item[1][7]).strip('%')) / 100, 4)
                lastBadDebtRate = item[1][8]
                lastAccountValue = round(float(str(item[1][9]).strip('%')) / 100, 4)
                firstAccountValue = item[1][10]

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
                     'lastAccountAmount': otherDecrAmount,
                     'lastAccountRate': lastSurplusAmount,
                     'lastBadDebtAmount': lastBadDebtAmount,
                     'lastBadDebtRate': lastBadDebtRate,
                     'lastAccountValue': lastAccountValue,
                     'firstAccountValue': firstAccountValue,
                     # 'exchangerateAddAmount':exchangerate_add_amount,
                     'tradeKey': tradeKey})  # 键值对设置，添加
            except Exception as e:
                print(e)
                pass
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/revenueAccountReveal/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass
