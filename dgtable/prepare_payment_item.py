"""
预付款项 prepare_payment_item
"""
import requests
import numpy as np
from basic import *


def Preparepaymentitem(path, tradeKey):
    # print(tradeKey)
    # f = open(path, "r", encoding="utf-8").read()
    # f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
    # df = CutOutML(f, '按账龄披露', '其中重要的其他应收款核销情况：')
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        # f = get_str_btw(f, '、应收账款', '、预付款项')
        df = CutOutM(f, '）预付款项按账龄列示', '）按预付对象归集的期末余额前五名的预付款情况')
        df = df.fillna(0)
        df = df.replace(np.nan, '')
        df = df.replace('--', 0)
        df.drop(0, inplace=True)
        df.drop(1, inplace=True)
        df.drop(2, inplace=True)

        # df.drop(df.tail(1).index, inplace=True)  # 删除最后一行数据
        df.reset_index(inplace=True, drop=True)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(Listkeys)
        # print(tableIndex)
        # print('&' * 100)
        jsonText = {'DG': []}
        # print(df)
        for item in df.iterrows():
            # print('item[1]:',item[1][-1])
            accountAge = item[1][0]  # 账龄
            firstAccountAmount = item[1][1]  # 期初余额-金额
            firstAccountRate = round(float(str(item[1][2]).strip('%')) / 100, 4)  # 期初余额-比例
            lastAccountAmount = item[1][3]  # 期末余额-金额
            lastAccountRate = round(float(str(item[1][4]).strip('%')) / 100, 4)  # 期末余额-比例

            # print('itemName:', itemName, 'firstSurplusAmount:',
            #       firstSurplusAmount, 'exchangerateAddAmount:', enterpriseMergelAddAmount, 'otherAddAmount:',
            #       otherAddAmount,
            #       'handleDecrAmount:', handleDecrAmount, 'otherDecrAmount:', otherDecrAmount, 'lastSurplusAmount:',
            #       lastSurplusAmount)

            jsonText['DG'].append(
                {'accountAge': accountAge,
                 'firstAccountAmount': firstAccountAmount,
                 'firstAccountRate': firstAccountRate,
                 'lastAccountAmount': lastAccountAmount,
                 'lastAccountRate': lastAccountRate,
                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/preparePaymentItem/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass

