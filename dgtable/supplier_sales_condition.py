import requests
from basic import *

"""
供应商情况（supplier_sales_condition）
"""


def Suppliersalescondition(path, tradeKey):
    # print(tradeKey)
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '公司主要销售客户情况', '公司前 5 大客户资料')[0]
        df.columns = ['情况', '数据']
        # df.reset_index(inplace=True, drop=True)
        df = df.fillna(0)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(Listkeys)
        # print(tableIndex)
        jsonText = {'DG': []}
        for item in df.iterrows():
            # print('获取行索引:', item[1])
            # print('本期发生额', item[1][2])  # 本期发生额
            va = item[1][1]
            va = float(va.strip('%')) / 100
            jsonText['DG'].append(
                {'itemName': item[1][0], 'itemValue': va, 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/supplierSalesCondition/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass

