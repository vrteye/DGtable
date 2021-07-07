import requests
from basic import *

"""
供应商资料（supplier_data）
"""


def Supplierdata(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '名供应商资料', '主要供应商其他情况说明')
        df = df.fillna(0)
        df = df.head(5)
        print(df)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(Listkeys)
        # print(tableIndex)
        # print('&' * 100)
        jsonText = {'DG': []}
        for item in df.iterrows():
            # print('@'*100)
            # print(item[1][2])
            # print('&'*100)
            va = item[1][2]
            va1 = float(va.strip('%')) / 100
            va2 = item[1][3]
            va2 = float(va2.strip('%')) / 100
            # print('获取行索引:', item[1])
            # print('本期发生额', item[1][2])  # 本期发生额
            jsonText['DG'].append(
                {'supplierName': item[1][1], 'procurementAmount': va1, 'totalPercentage': va2,
                 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/supplierData/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass
