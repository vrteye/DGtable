"""
应收账款-按账龄披露 receivable_account_age_reveal
"""
import requests
import numpy as np
from basic import *

def Receivableaccountagereveal(path, tradeKey):
    # print(tradeKey)
    # f = open(path, "r", encoding="utf-8").read()
    # f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
    # df = CutOutML(f, '按账龄披露', '其中重要的其他应收款核销情况：')
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        f = get_str_btw(f, '、应收账款', '、预付款项')
        df = CutOutM(f, '按账龄披露', '）本期计提、收回或转回的坏账准备情况')
        df = df.fillna('')
        df = df.replace(np.nan, '')
        # df.drop(0, inplace=True)
        # df.drop(df.tail(1).index, inplace=True)  # 删除最后一行数据
        df.reset_index(inplace=True, drop=True)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(Listkeys)
        # print(tableIndex)
        # print('&' * 100)
        jsonText = {'DG': []}

        for item in df.iterrows():
            # print('item[1]:',item[1][-1])
            itemName = item[1][0]  # 项目名称
            firstSurplusAmount = item[1][1]  # 初期余额
            # enterpriseMergelAddAmount = item[1][2]  # 企业合并本期增加金额
            # otherAddAmount = item[1][3]  # 其他本期增加金额
            # handleDecrAmount = item[1][4]  # 处置本期减少金额
            # otherDecrAmount = item[1][5]  # 其他本期减少金额
            # lastSurplusAmount = item[1][6]  # 期末余额

            # print('itemName:', itemName, 'firstSurplusAmount:',
            #       firstSurplusAmount, 'exchangerateAddAmount:', enterpriseMergelAddAmount, 'otherAddAmount:',
            #       otherAddAmount,
            #       'handleDecrAmount:', handleDecrAmount, 'otherDecrAmount:', otherDecrAmount, 'lastSurplusAmount:',
            #       lastSurplusAmount)

            jsonText['DG'].append(
                {'accountAge': itemName, 'surplusAmount': firstSurplusAmount,
                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/receivableAccountAgeReveal/add', json=data)
        print(Success)
    except Exception as e:
        print(e)
        pass