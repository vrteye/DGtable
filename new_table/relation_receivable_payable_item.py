"""
关联方应收应付款项（relation_receivable_payable_item）
"""
import requests
from basic import *


def Relationreceivablepayableitem(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、关联方应收应付款项', '、关联方承诺')
        df = CutOutM(f, '应收项目', '应付项目')  # 取最后一个表数据
        df = df.fillna('')

        df.drop(0, inplace=True)
        df.reset_index(inplace=True, drop=True)
        print(df)
        # df.drop(1, inplace=True)

        # df.drop(df.tail(1).index, inplace=True)  # 删除最后一行数据
        df.reset_index(inplace=True, drop=True)
        # print(df)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}

        for item in df.iterrows():
            # print('item[1]:',item[1][-1])
            itemName = item[1][0]  # 项目名称
            relation_obj = item[1][1]  # 初期余额-账面余额
            last_account_amount = item[1][2]  # 初期余额-减值准备余额
            last_bad_debt_amount = item[1][3]  # 初期余额-账面价值余额
            first_account_amount = item[1][4]  # 期末余额-账面余额余额
            first_bad_debt_amount = item[1][5]  # 期末余额-减值准备余额


            # print('itemName:', itemName, 'firstSurplusAmount:',
            #       'firstAccountSurplusAmount',firstAccountSurplusAmount,
            #       'firstDecrvaluePrepareSurplusAmount',firstDecrvaluePrepareSurplusAmount,
            #       'lastAccountSurplusAmount',lastAccountSurplusAmount,
            #

            jsonText['DG'].append(
                {'itemName': itemName,
                 'relation_obj': relation_obj,
                 'lastAccountAmount': last_account_amount,
                 'lastBadDebtAmount': last_bad_debt_amount,
                 'firstAccountAmount': first_account_amount,
                 'firstBadDebtAmount': first_bad_debt_amount,
                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        print(data)
        Success = requests.post('http://192.168.1.200:9008/relationReceivablePayableItem/add', json=data)
        print(Success)
    except Exception as e:
        print(e)
        pass