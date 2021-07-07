"""
跌价减值准备（fallprice_Impairment_prepare）
"""

import requests
import numpy as np
from basic import *


def FallpriceImpairmentprepare(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '）存货跌价准备和合同履约成本减值准备', '）存货期末余额含有借款费用资本化金额的说明')[0]
        df.drop(0, inplace=True)
        df.drop(1, inplace=True)

        df = df.replace(np.nan, '')
        df.fillna('')
        df.reset_index(inplace=True, drop=True)

        # print(df)

        Listkeys = df.keys()
        # print('col:', Listkeys)
        tableIndex = df[Listkeys[0]]
        # print(tableIndex)
        # print('&' * 100)
        jsonText = {'DG': []}
        for item in df.iterrows():
            # print('获取行索引:', item[1])
            # print('本期发生额', item[1][0])  # 本期发生额
            # relationTradeContent =

            # print(item[1][4])
            jsonText['DG'].append(
                {'itemName': item[1][0],  # 项目名称
                 'firstSurplusAmount': item[1][1],  # 初期余额
                 'accrualAddAmount': item[1][2],  # 计提本期增加金额
                 'backSellDecrAmount': item[1][3],  # 转回或转销减少金额
                 'otherDecrAmount': item[1][4],  # 其他本期减少金额
                 'lastSurplusAmount': item[1][5],  # 期末余额
                 'otherAddAmount': item[1][6],  # 其他本期增加金额
                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/fallpriceImpairmentPrepare/add', json=data)
        print(Success)

    except Exception as e:
        print(e)

