"""
未办妥产权证书的土地使用权情况（non_property_right_land_use_right_state）
"""
import requests
from basic import *


def Nonpropertyrightlanduserightstate(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '未办妥产权证书的土地使用权情况', '、商誉')[0]
        df.drop(0, inplace=True)
        df = df.fillna('')
        # print(df)
        Listkeys = df.keys()
        # print('col:', Listkeys)
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(tableIndex)
        # print('&' * 100)
        jsonText = {'DG': []}
        for item in df.iterrows():
            jsonText['DG'].append(
                {'itemName': item[1][0], 'accountValue': item[1][1], 'reason': item[1][2],
                 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/nonPropertyRightLandUseRightState/add', json=data)

    except Exception as e:
        print(e)
        pass

