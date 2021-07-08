"""
无形资产-明细情况（intangible_assets_detail）
"""
import requests
import numpy as np
from basic import *


def Intangibleassetsdetail(path, tradeKey, iad):
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        # f = get_str_btw(f, '、应收账款', '、预付款项')
        df = CutOutM(f, '无形资产情况', '未办妥产权证书的土地使用权情况')
        df = df.replace(np.nan, '')
        df = df.replace('--', '')
        print(df)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(df)
        for i in range(1, len(Listkeys)):
            # print(Listkeys[i])
            for j in range(len(iad)):
                # print(j)
                Amount = df.iloc[j, [i]][0]
                # print(Amount)
                # print(Listkeys[i],y_list_pf[j],Amount)
                jsonText['DG'].append(
                    {'itemName': iad[j], 'itemUnit': Listkeys[i], 'amount': Amount,
                     'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/intangibleAssetsDetail/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass
