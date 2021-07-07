"""
重要在建工程项目本期变动情况（doing_project_change_state）
"""
import requests
import numpy as np
from basic import *


def Doingprojectchangestate(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '）重要在建工程项目本期变动情况', '）工程物资')
        df.columns = ['项目名称', '预算数', '期初余额', '本期增加金额', '本期转入固定资产金额', '本期其他减少金额',
                      '期末余额', '工程累计投入占预算比例', '工程进度', '利息资本化累计金额', '本期利息资本化金额',
                      '本期利息资本化率', '资金来源']
        df.drop(0, inplace=True)
        df = df.replace(np.nan, '')
        df.fillna('')
        df.reset_index(inplace=True, drop=True)
        # print(df)

        # df.是否超过交易额度[df['是否超过交易额度'] == '否'] = 0
        # print(df)

        Listkeys = df.keys()
        # print('col:', Listkeys)
        tableIndex = df[Listkeys[0]]
        # print(tableIndex)
        # print('&' * 100)
        jsonText = {'DG': []}
        for item in df.iterrows():
            # print('获取行索引:', item[1])
            # print('本期发生额', item[1][0])  # 本期发生额
            # projectInputRatio = round(float(str(item[1][7].strip('%')).replace(',', '').replace('--', '')) / 100, 4)
            # currentInterestRate = round(float(str(item[1][11].strip('%')).replace(',', '').replace('--','')) / 100, 4)
            projectInputRatio = str(item[1][7]).replace('%', '').replace('--', '')
            projectProgresRatio = str(item[1][8]).replace('--', '')
            currentInterestRate = str(item[1][11]).replace('%', '').replace('--', '')
            # print(item[1][7])
            jsonText['DG'].append(
                {'itemName': item[1][0],  # 项目名称
                 'budgetAmount': item[1][1],  # 预算数
                 'firstSurplusAmount': item[1][2],  # 期初余额
                 'currentAddAmount': item[1][3],  # 本期增加金额
                 'fixedAssetAmount': item[1][4],  # 本期转入固定资产金额
                 'otherDecrAmount': item[1][5],  # 本期其他减少金额
                 'lastSurplusAmount': item[1][6],  # 期末余额
                 'projectInputRatio': projectInputRatio,  # 工程累计投入占预算比例
                 'projectProgresRatio': projectProgresRatio,  # 工程进度
                 'interestCumulativeAmount': item[1][9],  # 利息资本化累计金额
                 'currentInterestAmount': item[1][10],  # 本期利息资本化金额
                 'currentInterestRate': currentInterestRate,  # 本期利息资本化率
                 'fundSource': item[1][12],  # 资本来源
                 'tradeKey': tradeKey}, )  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        print(data)
        Success = requests.post('http://192.168.1.200:9008/doingProjectChangeState/add', json=data)
        print(Success)

    except Exception as e:
        print(e)

