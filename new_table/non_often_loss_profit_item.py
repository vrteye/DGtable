"""
非经常性损益项目及金额（non_often_loss_profit_item）
"""
import requests
import numpy as np
from basic import *


def Nonoftenlossprofititem(path, tradeKey):
    try:
        f = open(path, "r", encoding="utf-8").read()
        # f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        # f = get_str_btw(f, '、应收账款', '、预付款项')
        df = CutOutM(f, '、非经常性损益项目及金额', '公司业务概要')
        df = df.replace(np.nan, '')
        df = df.replace('--', '')
        # del df['说明']
        print(df)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        last = df[Listkeys[-1]]
        jsonText = {'DG': []}
        # # print(df)
        for i in range(1, len(Listkeys)-1):
            for j in range(len(df[Listkeys[i]])):
                # print(Listkeys[i])
                # print(print(tableIndex[j]))
                Amount = str(df.iloc[j, [i]][0]).replace('%', '')  # 获取值
                # print(Amount)
                Amount = Amount.replace(',', '')
                Amount = Amount.replace('0.0', '0')
                Amount = round(float(Amount), 4)
                explains = df[Listkeys[-1]][j]
                print(explains)
                jsonText['DG'].append(
                    {'itemName': tableIndex[j], 'year': Listkeys[i], 'amount': Amount,'explains':explains,
                     'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/nonOftenLossProfitItem/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass
