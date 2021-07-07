"""
按欠款方归集的期末余额前五名的应收账款情况	first_surplus_receivable_state df ok
"""
import requests
import numpy as np
from basic import *


def Firstsurplusreceivablestate(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        df = CutOutM(f, '）按欠款方归集的期末余额前五名的应收账款情况', '、其他应收款')[0]
        df = df.fillna('')
        df = df.replace(np.nan, '')
        df.drop(0, inplace=True)
        # df.drop(df.tail(1).index, inplace=True)  # 删除最后一行数据
        df.reset_index(inplace=True, drop=True)
        # print(df)
        # print(df)
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
            enterpriseMergelAddAmount = round(float(str(item[1][3].strip('%')).replace(',', '')) / 100, 4)  # 企业合并本期增加金额
            otherAddAmount = item[1][3]  # 其他本期增加金额

            # print('itemName:', itemName, 'firstSurplusAmount:',
            #       firstSurplusAmount, 'exchangerateAddAmount:', enterpriseMergelAddAmount, 'otherAddAmount:',
            #       otherAddAmount,
            #       'handleDecrAmount:', handleDecrAmount, 'otherDecrAmount:', otherDecrAmount, 'lastSurplusAmount:',
            #       lastSurplusAmount)

            jsonText['DG'].append(
                {'companyName': itemName, 'accountLastSurplusAmount': firstSurplusAmount,
                 'accountLastSurplusRatio': enterpriseMergelAddAmount,
                 'badDebtPrepareLastSurplusAmount': otherAddAmount,
                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/firstSurplusReceivableState/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass

