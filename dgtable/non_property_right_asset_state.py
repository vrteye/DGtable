"""
未办妥产权证书的固定资产情况（non_property_right_asset_state）
"""
import requests
from basic import *


def Nonpropertyrightassetstate(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '未办妥产权证书的固定资产情况', '、在建工程')
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
                {'itemName': item[1][0], 'accountValue': item[1][1], 'reason': item[1][2],
                 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/nonPropertyRightAssetState/add', json=data)
        print(Success)

    except Exception as e:
        print(e)