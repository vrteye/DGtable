"""
应收票据项目 receivable_bill_item
"""
import requests
import numpy as np
from basic import *


def Receivablebillitem(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        f = get_str_btw(f, '、应收票据', '、应收账款')
        df = CutOutM(f, '）应收票据分类列示', '）本期计提、收回或转回的坏账准备情况')[0]
        df = df.fillna(0)
        df = df.replace(np.nan, 0)
        df.drop(0, inplace=True)
        # df.drop(1, inplace=True)
        # df.drop(2, inplace=True)
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
            firstSurplusAmount = round(float(item[1][1]), 2)  # 初期余额
            lastSurplusAmount = round(float(item[1][2]), 2)  # 企业合并本期增加金额

            jsonText['DG'].append(
                {'itemName': itemName,
                 'firstSurplusAmount': firstSurplusAmount,
                 'lastSurplusAmount': lastSurplusAmount,

                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/receivableBillItem/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass
