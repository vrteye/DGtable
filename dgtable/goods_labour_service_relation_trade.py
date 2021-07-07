"""
购销商品、提供和接受劳务的关联交易（goods_labour_service_relation_trade）
"""

import requests
import numpy as np
from basic import *


def Goodslabourservicerelationtrade(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '）购销商品、提供和接受劳务的关联交易', '出售商品/提供劳务情况表')[0]
        df.drop(0, inplace=True)
        df = df.replace(np.nan, '')
        df.fillna('')
        df.reset_index(inplace=True, drop=True)

        df.是否超过交易额度[df['是否超过交易额度'] == '是'] = 1  # 替换单元格内容
        df.是否超过交易额度[df['是否超过交易额度'] == '否'] = 0
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
                {'itemName': item[1][0],
                 'relationObj': item[1][0],
                 'relationTradeContent': item[1][1],
                 'currentOccurAmount': item[1][2],
                 'approvalTradeAmount': item[1][3],
                 'isExceedTrade': item[1][4],
                 'lastOccurAmount': item[1][5],
                 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/goodsLabourServiceRelationTrade/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass
