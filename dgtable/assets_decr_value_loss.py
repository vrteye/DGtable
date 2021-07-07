import requests
from basic import *

"""
资产减值损失（assets_decr_value_loss）
"""


def Assetsdecrvalueloss(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '、资产减值损失', '、资产处置收益')
        df = df.fillna(0)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        print(Listkeys)
        print(tableIndex)
        print('&' * 100)
        jsonText = {'DG': []}
        for item in df.iterrows():
            # print('获取行索引:', item[1])
            # print('本期发生额', item[1][2])  # 本期发生额
            va = item[1][1]
            va1 = float(va.strip('%')) / 100

            va2 = item[1][2]
            va2 = float(va2.strip('%')) / 100
            jsonText['DG'].append(
                {'itemName': item[1][0], 'currentOccurAmount': va, 'lastOccurAmount': va2,
                 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        print(data)
        Success = requests.post('http://192.168.1.200:9008/assetsDecrValueLoss/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass
