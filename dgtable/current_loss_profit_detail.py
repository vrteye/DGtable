"""
当期非经常性损益明细 current_loss_profit_detail json ok
"""
import requests
import numpy as np
from basic import *


def Currentlossprofitdetail(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '、当期非经常性损益明细表', '、净资产收益率及每股收益')
        df = df.fillna('')
        df = df.replace(np.nan, '')
        df = df.replace('--', '')
        # df.drop(0, inplace=True)
        # df.drop(df.tail(1).index, inplace=True)  # 删除最后一行数据
        df.reset_index(inplace=True, drop=True)
        # print(df)
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
            amount = round(float(item[1][1]), 2)  # 初期余额
            enterpriseMergelAddAmount = item[1][2]  # 企业合并本期增加金额

            # print('itemName:', itemName, 'firstSurplusAmount:',
            #       firstSurplusAmount, 'exchangerateAddAmount:', enterpriseMergelAddAmount, 'otherAddAmount:',
            #       otherAddAmount,
            #       'handleDecrAmount:', handleDecrAmount, 'otherDecrAmount:', otherDecrAmount, 'lastSurplusAmount:',
            #       lastSurplusAmount)

            jsonText['DG'].append(
                {'itemName': itemName,
                 'amount': amount,
                 'explains': enterpriseMergelAddAmount,
                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/currentLossProfitDetail/add', json=data)
        print(Success)
    except Exception as e:
        print(e)
        pass

