import requests
from basic import *

"""
主要会计数据和财务指标（accounting_financial_data）
"""


def Accountingfinancialdata(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '、主要会计数据和财务指标', '、分季度主要财务指标')
        df.drop(7, inplace=True)
        # print(df)
        df.reset_index(inplace=True, drop=True)
        df = df.fillna(0)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        for i in range(1, len(Listkeys)):
            for j in range(len(df[Listkeys[i]])):
                # print(Listkeys[i])
                # print(print(tableIndex[j]))
                Amount = str(df.iloc[j, [i]][0]).replace('%', '')  # 获取值
                # print(Amount)
                Amount = Amount.replace(',', '')
                Amount = Amount.replace('0.0', '0')
                # Amount = int(Amount)
                jsonText['DG'].append(
                    {'itemName': tableIndex[j], 'year': Listkeys[i], 'incrDecrRate': Amount,
                     'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/accountingFinancialData/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass

