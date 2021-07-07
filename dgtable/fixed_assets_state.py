import requests
from basic import *

"""
固定资产情况（fixed_assets_state）
"""


def Fixedassetsstate(path, tradeKey, fixed):
    # print(tradeKey)
    try:
        f = open(path, "r", encoding="utf-8").read()
        f = get_str_btw(f, '、合并财务报表项目注释', '、合并范围的变更')
        df = CutOutM(f, '）固定资产情况', '、在建工程')[:2]

        DfAll = []
        for i in df:
            DfAll.append(i)
        df = pd.concat(DfAll)

        # print(col_name)
        # df = pd.concat(col_name)
        df.drop(0, inplace=True)
        df.reset_index(inplace=True, drop=True)
        df = df.fillna('')
        # print('df:', df)

        Listkeys = df.keys()
        # print(Listkeys)
        jsonText = {'DG': []}
        for i in range(1, len(Listkeys)):
            # print(Listkeys[i])
            for j in range(len(fixed) - 2):
                # print(j)
                Amount = df.iloc[j, [i]][0]
                # print(Amount)
                # print(Listkeys[i],y_list_pf[j],Amount)
                jsonText['DG'].append(
                    {'itemName': fixed[j], 'itemType': Listkeys[i], 'itemAssets': Amount,
                     'tradeKey': tradeKey})  # 键值对设置，添加
        dgdata = jsonText['DG']

        jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)
        data = json.loads(jsonData)
        # print(data)
        Success = requests.post('http://192.168.1.200:9008/fixedAssetsState/add', json=data)
        print(Success)

    except Exception as e:
        print(e)
        pass

