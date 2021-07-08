

"""
在建工程情况（doing_project_state）
"""

import requests
from basic import *
def Doingprojectstate(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '）在建工程情况', '）重要在建工程项目本期变动情况')  # 取最后一个表数据
        df = df.fillna(0)
        df.drop(0, inplace=True)
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
            firstAccountSurplusAmount = item[1][1]  # 初期余额-账面余额
            firstDecrvaluePrepareSurplusAmount = item[1][2]  # 初期余额-减值准备余额
            firstAccountworthtSurplusAmount = item[1][3]  # 初期余额-账面价值余额
            lastAccountSurplusAmount = item[1][4]  # 期末余额-账面余额余额
            lastDecrvaluePrepareSurplusAmount = item[1][5]  # 期末余额-减值准备余额
            lastAccountworthSurplusAmount = item[1][6]  # 期末余额-账面价值余额

            # print('itemName:', itemName, 'firstSurplusAmount:',
            #       'firstAccountSurplusAmount',firstAccountSurplusAmount,
            #       'firstDecrvaluePrepareSurplusAmount',firstDecrvaluePrepareSurplusAmount,
            #       'lastAccountSurplusAmount',lastAccountSurplusAmount,
            #

            jsonText['DG'].append(
                {'itemName': itemName, 'firstAccountSurplusAmount': firstAccountSurplusAmount,
                 'firstDecrvaluePrepareSurplusAmount': firstDecrvaluePrepareSurplusAmount,
                 'firstAccountworthtSurplusAmount': firstAccountworthtSurplusAmount,
                 'lastAccountSurplusAmount': lastAccountSurplusAmount,
                 'lastDecrvaluePrepareSurplusAmount': lastDecrvaluePrepareSurplusAmount,
                 'lastAccountworthSurplusAmount': lastAccountworthSurplusAmount,
                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/doingProjectState/add', json=data)
        print(Success)
    except Exception as e:
        print(e)
        pass
