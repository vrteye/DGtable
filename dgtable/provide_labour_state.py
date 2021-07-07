import requests
from basic import *

"""
提供劳务情况  provide_labour_state      # 按索引遍历
"""


def Providelabourstate(path, tradeKey):
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '提供劳务情况表', '购销商品、提供和接受劳务的关联交易说明')
        # print(df)
        df.reset_index(inplace=True, drop=True)
        df = df.fillna(0)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(Listkeys)
        # print(tableIndex)
        print('&' * 100)
        jsonText = {'DG': []}
        for item in df.iterrows():
            # print('获取行索引:', item[1])
            # print('本期发生额', item[1][2])  # 本期发生额
            jsonText['DG'].append(
                {'itemName': item[1][0], 'relationObject': item[1][0], 'relationTradeContent': item[1][1],
                 'currentOccurAmount': item[1][2], 'last_occur_amount': item[1][3], 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        print(data)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/provideLabourState/add', json=data)
        print(Success)

    except Exception as e:
        print(e)

