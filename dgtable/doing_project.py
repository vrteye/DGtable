import requests
from basic import *

"""
在建工程情况（doing_project_state）
"""


def Doingproject(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutML(f, '>、在建工程', '）在建工程情况')  # 取最后一个表数据
        df = df.fillna('')
        # df.drop(0, inplace=True)
        # df.drop(1, inplace=True)

        # df.drop(df.tail(1).index, inplace=True)  # 删除最后一行数据
        df.reset_index(inplace=True, drop=True)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}

        for item in df.iterrows():
            # print('item[1]:',item[1][-1])
            itemName = item[1][0]  # 项目名称
            firstSurplusAmount = item[1][1]  # 初期余额
            lastSurplusAmount = item[1][2]  # 企业合并本期增加金额

            # print('itemName:', itemName, 'firstSurplusAmount:',
            #       firstSurplusAmount, 'exchangerateAddAmount:', enterpriseMergelAddAmount, 'otherAddAmount:',
            #       otherAddAmount,
            #       'handleDecrAmount:', handleDecrAmount, 'otherDecrAmount:', otherDecrAmount, 'lastSurplusAmount:',
            #       lastSurplusAmount)

            jsonText['DG'].append(
                {'itemName': itemName, 'firstSurplusAmount': firstSurplusAmount,
                 'lastSurplusAmount': lastSurplusAmount, 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        Success = requests.post('http://192.168.1.200:9008/doingProject/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass

