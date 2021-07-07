import requests
from basic import *
from decimal import *
"""
研发投入（develop_putinto）
"""


def Developputinto(path, tradeKey):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        df = CutOutM(f, '、研发投入', '、现金流')
        df = df.fillna(0)
        # print(df)
        col = df.keys()
        row = df.shape[0]

        jsonText = {'DG': []}
        for i in range(1, len(col) - 1):
            # print(col[i])
            for j in range(row):
                itemName = df.iloc[j][0]

                withAddDecrRatio = round(float(str(df.iloc[j][-1]).strip('%')) / 100, 4)
                # Decimal.from_float(withAddDecrRatio)
                # print('withAddDecrRatio:',withAddDecrRatio)
                date = col[i]
                putintoAmount = df.iloc[j][i]

                if '%' in putintoAmount:
                    putintoAmount = round(float(str(df.iloc[j][i]).strip('%')) / 100, 4)
                    jsonText['DG'].append(
                        {
                            'itemName': itemName,
                            'date': date,
                            'putintoAmount': putintoAmount,
                            'withAddDecrRatio': withAddDecrRatio,
                            'tradeKey': tradeKey})  # 键值对设置，添加
                    # print('withAddDecrRatio:',withAddDecrRatio)
                else:
                    putintoAmount = round(float(str(df.iloc[j][i])), 4)
                    jsonText['DG'].append(
                        {
                            'itemName': itemName,
                            'date': date,
                            'putintoAmount': putintoAmount,
                            'withAddDecrRatio': withAddDecrRatio,
                            'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']
        #
        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/developPutinto/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
