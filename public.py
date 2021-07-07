import re
import json
import pandas as pd
# from MyEncoder import *
from lxml import etree
from xml.dom.minidom import parse
from html.parser import HTMLParser

# path = r'D:/Users/Desktop/阜新德尔汽车部件股份有限公司.html'
# path = r'D:/Users/Desktop/浙江金盾风机股份有限公司.html'
# path = r'D:/Users/Desktop/聚龙股份有限公司.html'
# path = r'D:/Users/Desktop/北京数知科技股份有限公司.html'
# path = r'D:/Users/Desktop/f74fbb5a-78f9-48be-b8b3-7c5153aa7d83.html'
# path = r'D:/Users/Desktop/html/ff759cb0-0ff9-4b5e-8aab-f9e4764844ec.html'
# path = r'D:/Users/Desktop/聚龙股份有限公司.html'
# f = open(path, "r", encoding="utf-8")  # 读取文件
# f = f.read()  # 把文件内容转化为字符串
# from project_table import MyEncoder
# from project_table.MyEncoder import *


def get_str_btw(content, front, back):  # 字符串取值
    """
    :param content: 文本内容
    :param front: 文本中前段句子
    :param back: 文本中后段句子
    :return: 返回缩小范围后的内容
    """
    par = content.partition(front)
    data = (par[2].partition(back))[0][:]
    return data


def GetDataSection(df, X, Y, *args):
    """
    :param df: 初始dataframe
    :param X: row行名1,查找区间范围，后面会删除
    :param Y: row行名2，查找区间范围，后面会删除
    :param args: columns列名1、列名2...
    :return: 返回区间范围dataframe结果
    """
    df.columns.values[0] = 'DATA'
    df.set_index(df.DATA, inplace=True)
    columnsx = [i for i in args]
    rowx = [X, Y]
    dfxx = df.loc[rowx[0]:rowx[1]]
    dfxx = dfxx[columnsx]
    dfxx.drop(rowx, inplace=True)
    return dfxx


def GetDataSections(df, X, Y, *args):
    """
    :param df: 初始dataframe
    :param X: row行名1,查找区间范围，后面会删除
    :param Y: row行名2，查找区间范围，后面会删除
    :param args: columns列名1、列名2...
    :return: 返回区间范围dataframe结果
    """
    df.columns.values[0] = 'DATA'
    df.set_index(df.DATA, inplace=True)
    columnsx = [i for i in args]
    rowx = [X, Y]
    dfxx = df.loc[rowx[0]:rowx[1]]
    dfxx = dfxx[columnsx]
    return dfxx


def GetDataArgs(df, *rowcol):
    """
    :param df: 初始dataframe
    :param rowcol: row行名1、列名2... 行名1、行名2....
    :return: 返回区间范围dataframe结果
    """
    global dfxx
    try:
        rows = rowcol[0]
        columns = rowcol[1]
        df.columns.values[0] = 'DATA'
        df.set_index(df.DATA, inplace=True)
        # columnsx = [A, B]
        columnsx = [i for i in columns]
        rowx = [j for j in rows]
        dfxx = df.loc[rowx, columnsx]
    except Exception as e:
        pass
        # print(e)

    # dfxx = dfxx[columnsx]
    # dfxx.drop(rowx, inplace=True)
    return dfxx


# print('~' * 20 + '占公司营业收入或营业利润表' + '~' * 20)


# def CutOut(f, first, end):
#     global df
#     try:
#         content = get_str_btw(f, first, end)
#         dfx = pd.read_html(content, encoding='utf-8', header=0)[0]
#         col_name = dfx.columns.tolist()  # 列名
#         # print(col_name)
#         df = pd.read_html(content, encoding='utf-8', header=None)
#         # num_dfx = len(dfx)
#         DfAll = []
#         for i in df:
#             i.columns = col_name
#             DfAll.append(i)
#         df = pd.concat(DfAll)
#     except Exception as e:
#         # print(e)
#         pass
#         # print('没有')
#     return df


def CutOut(f, first, end):
    global df
    try:
        content = get_str_btw(f, first, end)
        dfx = pd.read_html(content, encoding='utf-8', header=0)[0]
        col_name = dfx.columns.tolist()  # 列名
        df = pd.read_html(content, encoding='utf-8', header=None)[0]
        DfAll = []
        for i in df:
            i.columns = col_name
            DfAll.append(i)
        df = pd.concat(DfAll)
    except Exception as e:
        pass
    return df








def jsontoapi(df):
    """

    :param df:  df = {"营业总收入":{"2020 年度":"a","2019 年度":"b"},"利息收入":{"2020 年度":"c","2019 年度":"d"},"xxxx":{"2020
    年度":"e","2019 年度":"f"}} :return: [{'itemName': 'xxxx', 'date': '2019 年度', 'amount': 'f'}, {'itemName': 'xxxx',
    'date': '2019 年度', 'amount': 'f'}, {'itemName': 'xxxx', 'date': '2019 年度', 'amount': 'f'}, {'itemName': 'xxxx',
    'date': '2019 年度', 'amount': 'f'}, {'itemName': 'xxxx', 'date': '2019 年度', 'amount': 'f'}, {'itemName': 'xxxx',
    'date': '2019 年度', 'amount': 'f'}]
    """
    jsonText = {'mergeProfit': []}
    Listkeys = df.keys()

    for i in Listkeys:
        col = df[i].keys()
        for j in df[i].keys():
            jsonText['mergeProfit'].append({'itemName': j, 'date': i, 'amount': str(df[i][j])})
    jsondata = json.dumps(jsonText, indent=4, separators=(',', ': '), ensure_ascii=False)
    return jsondata
