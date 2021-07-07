import requests
from basic import *

"""
合并利润表
"""


def MergeProfit(path, tradeKey, y_list_pf):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '、合并利润表', '、母公司利润表')
        df.reset_index(inplace=True, drop=True)
        # print(df)
        df = df.fillna(0)
        Listkeys = df.keys()
        # print(Listkeys)
        jsonText = {'DG': []}
        for i in range(1, len(Listkeys)):
            # print(Listkeys[i])
            for j in range(len(y_list_pf) - 2):
                # print(j)
                Amount = df.iloc[j, [i]][0]
                # print(Listkeys[i],y_list_pf[j],Amount)
                jsonText['DG'].append(
                    {'itemName': y_list_pf[j], 'date': Listkeys[i], 'amount': Amount, 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/mergeProfit/add', json=data)
        print(Success)

    except Exception as e:
        print(e)

