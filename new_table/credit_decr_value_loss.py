"""
信用减值损失（credit_decr_value_loss）
"""
import requests
import numpy as np
from basic import *


def Creditdecrvalueloss(path, tradeKey):
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        # f = get_str_btw(f, '、应收账款', '、预付款项')
        df = CutOutM(f, '、信用减值损失', '、资产减值损失')


        df = df.replace(np.nan, '')
        df = df.replace('--', '')
        print(df)
        Listkeys = df.keys()
        tableIndex = df[Listkeys[0]]
        jsonText = {'DG': []}
        # print(df)
        for item in df.iterrows():
            # print('item[1]:',item[1][-1])
            itemName = item[1][0]  # 项目
            currentOccurAmount = round(float(str(item[1][1])), 4)  # 期末账面价值
            try:
                previousOccurAmount = round(float(str(item[1][2])), 4)  # 期初余额-比例
            except:
                previousOccurAmount = ''

            # print('itemName:', itemName, 'firstSurplusAmount:',
            #       firstSurplusAmount, 'exchangerateAddAmount:', enterpriseMergelAddAmount, 'otherAddAmount:',
            #       otherAddAmount,
            #       'handleDecrAmount:', handleDecrAmount, 'otherDecrAmount:', otherDecrAmount, 'lastSurplusAmount:',
            #       lastSurplusAmount)

            jsonText['DG'].append(
                {'itemName': itemName,
                 'currentOccurAmount': currentOccurAmount,
                 'previousOccurAmount': previousOccurAmount,
                 'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        # print(jsonData)
        data = json.loads(jsonData)
        print(data)
        Success = requests.post('http://192.168.1.200:9008/creditDecrValueLoss/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass