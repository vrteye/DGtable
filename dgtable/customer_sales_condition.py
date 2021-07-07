"""
销售客户情况（customer_sales_condition）
"""
import requests
import numpy as np
from basic import *


def Customersalescondition(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '公司主要销售客户情况', '公司前 5 大客户资料')[0]
        df = df.fillna('')
        df = df.replace(np.nan, '')
        df = df.replace('--', '')
        # df.drop(0, inplace=True)
        # df.drop(df.tail(1).index, inplace=True)  # 删除最后一行数据
        df.reset_index(inplace=True, drop=True)
        df.columns = ['情况', '数据']
        # print(df)
        # df.reset_index(inplace=True, drop=True)
        df = df.fillna(0)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(Listkeys)
        # print(tableIndex)
        # print('&' * 100)
        jsonText = {'DG': []}
        for item in df.iterrows():
            # print('获取行索引:', item[1])
            # print('本期发生额', item[1][2])  # 本期发生额
            va = item[1][1]
            va = float(va.strip('%')) / 100
            jsonText['DG'].append(
                {'itemName': item[1][0], 'itemValue': va, 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        Success = requests.post('http://192.168.1.200:9008/customerSalesCondition/add', json=data)
    except Exception as e:
        print(e)
        pass

