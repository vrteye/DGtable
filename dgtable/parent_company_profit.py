import requests
from basic import *

"""
母公司利润表
"""


def ParentCompanyProfit(path, tradeKey, y_list_mlr):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '、母公司利润表', '、合并现金流量表')
        df.reset_index(inplace=True, drop=True)
        # print(df)
        df = df.fillna('')
        Listkeys = df.keys()
        # print(df)
        jsonText = {'DG': []}
        for i in range(1, len(Listkeys)):
            # print(Listkeys[i])
            for j in range(len(y_list_mlr) - 2):
                # print(j)
                # Amount = df.iloc[j, [i]][0]
                # print(Listkeys[i],y_list_pf[j],Amount)
                jsonText['DG'].append(
                    {'itemName': y_list_mlr[j],
                     'date': Listkeys[i],
                     # 'putintoAmount': Amount,
                     'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/parentCompanyProfit/add', json=data)
        print(Success)
    except Exception as e:
        print(e)
        pass
