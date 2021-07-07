import requests
from basic import *

"""
存货分类（goods_stock_classify）
"""


def Goodsstockclassify(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '存货分类', '存货跌价准备和合同履约成本减值准备')
        # df.reset_index(inplace=True, drop=True)
        df.drop(0, inplace=True)
        df.drop(1, inplace=True)
        df.drop(2, inplace=True)
        df.drop(3, inplace=True)
        df.drop(4, inplace=True)
        # df = df.tail(5)
        df.reset_index(inplace=True, drop=True)
        df.columns = ['项目', '账面余额', '存货跌价准备或合同履约成本减值准备', '账面价值', '账面余额', '存货跌价准备或合同履约成本减值准备', '账面价值']
        # print(df.head(2))

        Listkeys = df.keys()
        # print('col:', Listkeys)
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(tableIndex)
        # print('&' * 100)
        jsonText = {'DG': []}
        for item in df.iterrows():
            # print('获取行索引:', item[1])
            # print('本期发生额', item[1][0])  # 本期发生额
            jsonText['DG'].append(
                {'itemName': item[1][0], 'accountFirstSurplusAmount': item[1][1],
                 'fallpriceFirstSurplusAmount': item[1][2],
                 'accountworthFirstSurplusAmount': item[1][3], 'accountLastSurplusAmount': item[1][4],
                 'fallpriceLastSurplusAmount': item[1][5], 'accountworthLastSurplusAmount': item[1][6],
                 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/goodsStockClassify/add', json=data)
        print(Success)

    except Exception as e:
        print(e)

