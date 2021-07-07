# - * - coding: utf - 8 -*-
# from public import *
from basic import *
import requests

"""
员工数量、专业构成及教育程度表
"""
# path = r'D:/Users/Desktop/html2/d41e601f-7484-4432-a3eb-3810ff453c67.html'


def Comstaffstate(Path, tradekey):
    try:
        f = open(Path, "r", encoding="utf-8").read()
        df = CutOutM(f, '、员工数量、专业构成及教育程度', '、薪酬政策')
        df.columns.values[0] = 'DATA'
        df.set_index(df.DATA, inplace=True)
        dfx = df.iloc[:, 0:2]
        col_name = dfx.columns.tolist()[1]  # 列名
        x0 = col_name
        x1 = df.loc['主要子公司在职员工的数量（人）', col_name]
        x2 = df.loc['在职员工的数量合计（人）', col_name]
        x3 = df.loc['母公司及主要子公司需承担费用的离退休职工人数（人）', col_name]
        x4 = df.loc['生产人员', col_name]
        x5 = df.loc['销售人员', col_name]
        x6 = df.loc['技术人员', col_name]
        x7 = df.loc['财务人员', col_name]
        x8 = df.loc['行政人员', col_name]
        try:
            x9 = df.loc['硕士', col_name]
        except:
            x9 = ''
            pass
        try:
            x10 = df.loc['本科', col_name]
        except:
            x10 = ''
            pass
        try:
            x11 = df.loc['大专', col_name]
        except:
            x11 = ''
            pass
        try:
            x12 = df.loc['大专以下', col_name]
        except:
            x12 = ''
            pass
        x_list = ['母公司在职员工的数量', '主要子公司在职员工的数量', '在职员工的数量合计',
                  '母公司及主要子公司需承担费用的离退休职工人数', '生产人员', '销售人员', '技术人员',
                  '财务人员', '行政人员', '硕士', '本科', '大专', '大专以下']
        y_list = ['1', '2', '3']
        jsondata = [{"itemName": str(x_list[0]),
                     "itemType": y_list[0],
                     "incomeAmount": x0,
                     "tradeKey": tradekey
                     },
                    {"itemName": str(x_list[1]),
                     "itemType": y_list[0],
                     "incomeAmount": x1,
                     "tradeKey": tradekey
                     },
                    {"itemName": str(x_list[2]),
                     "itemType": y_list[0],
                     "incomeAmount": x2,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[3],
                     "itemType": y_list[0],
                     "incomeAmount": x3,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[4],
                     "itemType": y_list[1],
                     "incomeAmount": x4,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[5],
                     "itemType": y_list[1],
                     "incomeAmount": x5,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[6],
                     "itemType": y_list[1],
                     "incomeAmount": x6,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[7],
                     "itemType": y_list[1],
                     "incomeAmount": x7,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[8],
                     "itemType": y_list[1],
                     "incomeAmount": x8,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[9],
                     "itemType": y_list[2],
                     "incomeAmount": x9,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[10],
                     "itemType": y_list[2],
                     "incomeAmount": x10,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[11],
                     "itemType": y_list[2],
                     "incomeAmount": x11,
                     "tradeKey": tradekey
                     },
                    {"itemName": x_list[12],
                     "itemType": y_list[2],
                     "incomeAmount": x12,
                     "tradeKey": tradekey
                     }, ]
        jsonData = json.dumps(jsondata, indent=4, separators=(',', ': '), ensure_ascii=False)
        data = json.loads(jsonData)
        print(data)
        Success = requests.post('http://192.168.1.200:9008/comStaffState/add', json=data)
        print(Success)

    except Exception as e:
        print(e)



# tradekey = tradekey(path)[0]
# df = NumberOfEmploy(path, tradekey)
# print(df)



# df.columns = ['项目', '数量']
# print(df)
# col_name = df.columns.tolist()  # columns所有列名
# col_name[0] = '项目名'  # 重新赋予第一个列名，索引为0的列名
# df.columns = col_name  # 更新表格列名
# df.reset_index(inplace=True, drop=True)  # 重置索引，因为可能存在合并表格索引形式1，2，3，1，2，3，4
# df.drop(0, inplace=True)  # 去掉名为项目的第一行数据
# df.reset_index(inplace=True, drop=True)  # 再一次重置索引，删掉了第一行数据，需要重置
# df.set_index(df.项目名, inplace=True)  # 设置项目为索引
# df.drop('项目名', axis=1, inplace=True)  # 删除项目本身列
# df = df.drop(labels=['专业构成', '专业构成类别', '教育程度类别'], axis=0)
# print(df)
