import requests
from basic import *

"""
合并资产负债表
"""


def mergeAssetsDebt(path, tradekey, y_list_ml):
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '、合并资产负债表', '、母公司资产负债表')
        # x = ['、合并资产负债表', '、母公司资产负债表']
        df.reset_index(inplace=True, drop=True)
        df = df.fillna(0)
        Listkeys = df.keys()
        jsonText = {'DG': []}
        for i in range(1, len(Listkeys)):
            for j in range(len(y_list_ml) - 1):
                Amount = df.iloc[j, [i]][0]
                jsonText['DG'].append(
                    {'itemName': y_list_ml[j], 'date': Listkeys[i], 'amount': Amount, 'tradeKey': tradekey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        data = json.loads(jsonData)
        Success = requests.post('http://192.168.1.200:9008/mergeAssetsDebt/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass