import requests
from basic import *

"""
会计利润与所得税费用调整过程（profit_tax_adjust_proces）
"""


def Profittaxadjustproces(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '会计利润与所得税费用调整过程', '、其他综合收益')
        # print(df)

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
                {'itemName': item[1][0], 'currentOccurAmount': item[1][1], 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/profitTaxAdjustProces/add', json=data)
        print(Success)

    except Exception as e:
        print(e)

