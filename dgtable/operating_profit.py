import requests
from basic import *

"""
营业收入或营业利润（operating_profit）
"""


def Operatingprofit(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '占公司营业收入或营业利润', '公司已签订的重大销售合同截至本报告期的履行情况')[0]
        df = df.fillna(0)
        df.columns = ['项目', '营业收入', '营业成本', '毛利率', '营业收入比上年同期增减', '营业成本比上年同期增减', '毛利率比上年同期增减']

        # df = df[~df['项目'].str.contains('分产品')]
        df.drop(0, inplace=True)
        df.reset_index(inplace=True, drop=True)
        df = df[~df['项目'].isin(['分行业'])]
        df = df[~df['项目'].isin(['分产品'])]
        df = df[~df['项目'].isin(['分地区'])]
        # 按条件删除行
        # df.drop(1, inplace=True)
        # print(df)
        # df.drop(df.tail(1).index, inplace=True)  # 删除最后一行数据
        df.reset_index(inplace=True, drop=True)
        # print(df)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(tableIndex)

        for item in df.iterrows():
            # print('item[1]:',item[1][-1])
            # itemName = tableIndex[i]  # 项目名
            itemName = item[1][0]

            # itemType = '分产品'  # 项目类型
            incomeAmount = round(float(item[1][1]), 4)  # 营业收入额
            costAmount = round(float(item[1][2].strip('%')) / 100, 4)  # 营业成本
            grossProfitRate = round(float(str(item[1][3].strip('%')).replace(',', '')) / 100, 4)  # 毛利率
            incomeIncrDecrRate = round(float(str(item[1][4].strip('%')).replace(',', '')) / 100, 4)  # 营业收入比上年同期增减
            costIncrDecrRate = round(float(str(item[1][5].strip('%')).replace(',', '')) / 100, 4)  # 营业成本比上年同期增减
            grossProfitDecrRate = round(float(str(item[1][6].strip('%')).replace(',', '')) / 100, 4)  # 毛利率比上年同期增减

            # print('itemName:', itemName,
            #       'incomeAmount', incomeAmount,
            #       'grossProfitRate', grossProfitRate,
            #       'incomeIncrDecrRate', incomeIncrDecrRate,
            #       'costAmount', costAmount,
            #       'costIncrDecrRate', costIncrDecrRate,
            #       'grossProfitDecrRate', grossProfitDecrRate)

            jsonText['DG'].append(
                {'itemName': itemName, 'incomeAmount': incomeAmount,
                 'grossProfitRate': grossProfitRate,
                 'incomeIncrDecrRate': incomeIncrDecrRate,
                 'costAmount': costAmount,
                 'costIncrDecrRate': costIncrDecrRate,
                 'grossProfitDecrRate': grossProfitDecrRate,
                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/operatingProfit/add', json=data)
        print(Success)

    except Exception as e:
        print(e)

