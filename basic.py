import os
import re
import json
import requests
import pandas as pd
from lxml import etree


def File_Eli(path):
    """
    :param path: 文件路径
    :return: 剔除隐藏的文件,生成一个剔除隐藏文件后的列表。
    """
    path = os.listdir(path)
    ls = []
    for f in path:
        # print(f)
        if not f.startswith('.'):
            ls.append(f)
    return ls


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


def reGetStrBtw(f, first, end):
    """
    :param f: 文本内容
    :param first: 文本中前段句子
    :param end: 文本中后段句子
    :return: 返回缩小范围后的内容
    """
    f = re.sub('\s+style=\"[^"]*\"', '', f, 0, re.I)  # 去掉css样式
    # print(f)
    reSearch = '{}([\s\S]*){}'.format(first, end)
    data = re.search(reSearch, f)[0]
    return data

def CutOut(f, first, end):
    """
    :param f: 读出来的html
    :param first: 需要截取位置前定位句子
    :param end: 需要截取位置末定位句子
    :return: dataframe表格
    """
    global df
    try:
        content = get_str_btw(f, first, end)  # 基于partition
        # content = reGetStrBtw(f, first, end)  # 基于re.Search
        dfx = pd.read_html(content, encoding='utf-8', header=0)[0]
        col_name = dfx.columns.tolist()  # 列名
        # print(col_name)
        df = pd.read_html(content, encoding='utf-8', header=0)[0]
        # num_dfx = len(dfx)
        DfAll = []
        for i in df:
            i.columns = col_name
            DfAll.append(i)
        df = pd.concat(DfAll)

    except Exception as e:
        pass
    return df


def CutOutM(f, first, end):
    """
    针对跨页合并型表格，第二页没有表头的情况；合并表格，以第一页为表头，并重置索引
    :param f: 读出来的html
    :param first: 需要截取位置前定位句子
    :param end: 需要截取位置末定位句子
    :return: dataframe表格
    """
    global df
    try:
        content = get_str_btw(f, first, end)  # 基于partition
        # content = reGetStrBtw(f, first, end)  # 基于re.Search
        dfx = pd.read_html(content, encoding='utf-8', header=0)[0]
        col_name = dfx.columns.tolist()  # 列名
        col_name = [i.replace(' ', '') for i in col_name]
        df = pd.read_html(content, encoding='utf-8', header=None)
        DfAll = []
        for i in df:
            i.columns = col_name
            DfAll.append(i)
        df = pd.concat(DfAll)
        df.reset_index(inplace=True, drop=True)
        df.drop(0, inplace=True)  # 去掉名为项目的第一行数据
        df.reset_index(inplace=True, drop=True)
    except Exception as e:
        pass
    return df

def CutOutML(f, first, end):
    """

    针对跨页合并型表格，第二页没有表头的情况；合并表格，以第一页为表头，并重置索引,适合于混乱情况下，结果为最后一个表
    :param f: 读出来的html
    :param first: 需要截取位置前定位句子
    :param end: 需要截取位置末定位句子
    :return: dataframe表格
    """
    global df
    try:
        content = get_str_btw(f, first, end)  # 基于partition
        # content = reGetStrBtw(f, first, end)  # 基于re.Search
        dfx = pd.read_html(content, encoding='utf-8', header=0)[0]
        print(dfx)
        col_name = dfx.columns.tolist()  # 列名
        col_name = [i.replace(' ', '') for i in col_name]
        df = pd.read_html(content, encoding='utf-8', header=None)
        df = df[-1]
        df.columns = df.iloc[0]
        df.drop(0, inplace=True)  # 去掉名为项目的第一行数据
        df.reset_index(inplace=True, drop=True)

    except Exception as e:
        pass
    return df

def CutOutO(f, first, end):
    """
    :param f: 读出来的html
    :param first: 需要截取位置前定位句子
    :param end: 需要截取位置末定位句子
    :return: dataframe表格
    """
    global df
    try:
        content = get_str_btw(f, first, end)  # 基于partition
        # content = reGetStrBtw(f, first, end)  # 基于re.Search
        dfx = pd.read_html(content, encoding='utf-8', header=0)
        col_name = ['项目', '数量']
        dfx.columns = col_name
        # print(dfx)
        # col_name = dfx.columns.tolist()  # 列名

        # # print(col_name)
        # df = pd.read_html(content, encoding='utf-8', header=0)[0]
        # # num_dfx = len(dfx)
        # DfAll = []
        # for i in df:
        #     i.columns = col_name
        #     DfAll.append(i)
        # df = pd.concat(DfAll)
        # print(df)
    except Exception as e:
        pass
    return dfx


def tradekey(path):
    """
    :param path: 文件完整路径
    :return: 年报id tradeKey
    """
    global tradeKey, reportName, year
    try:
        f = open(path, "r", encoding="utf-8").read()
        # content = get_str_btw(f, '公司实物销售收入是否大于劳务收入', '公司已签订的重大销售合同截至本报告期的履行情况')
        # dfx = pd.read_html(content, encoding='utf-8', header=0)[0]
        # year = dfx.columns.tolist()[3]  # 列名
        content = get_str_btw(f, '有限公司', '年度报告')
        response = etree.HTML(text=content)
        year = response.xpath('string(.)')
        if len(year) < 15:


            # col_name = dfx.columns.tolist()  # 列名
            # df = pd.read_html(content, encoding='utf-8', header=None)[0]
            types = '年度报告'
            html1 = get_str_btw(f, '、公司信息', '、联系人和联系方式')
            dfx = pd.read_html(html1, encoding='utf-8', header=0)[0]
            stockCode11 = dfx.columns.tolist()[3]
            year_report_id11 = year + '_' + stockCode11 + '_' + types
            reportName = year + types
            reportName = reportName.replace(' ', '')
            tradeKey = year_report_id11.replace(' ', '')
            print(tradeKey)
            # print(tradeKey)
            year = year.replace(' 年', '')
    except Exception as e:
        print(e)
        pass
    return tradeKey, reportName, year


def Jsontoapi(df, itemName, date, amount, id, urlPost):
    """
    :param df: dataframe
    :param itemName: 项目，索引
    :param date: 日期项，列名
    :param amount: 金额，值
    :param tradeKey: 每份报告唯一值
    :param urlPost: url path
    :return: succee
    """
    df = df.fillna(0)  # 缺失值用0填充
    Listkeys = df.keys()
    # print(Listkeys)
    # df = df.drop(labels=['专业构成', '专业构成类别'], axis=0)
    jsonText = {'DG': []}
    # Listkeys = df.columns.tolist()
    # Listkeys = df.keys()
    for i in Listkeys:
        for j in df[i].keys():
            # print(j)
            Amount = str(df[i][j]).replace('%', '')
            Amount = Amount.replace(',', '')
            Amount = Amount.replace('0.0', '0')
            # Amount = int(Amount)
            # print('i:',i,'j:',j,'Amount:',Amount)
            # print(tradeKey)
            jsonText['DG'].append({itemName: j, date: i, amount: Amount, 'tradeKey': id})  # 键值对设置，添加
    dgdata = jsonText['DG']
    print('dgdata:', dgdata)
    jsonData = json.dumps(dgdata, indent=4, separators=(',', ': '), ensure_ascii=False)  # json格式
    data = json.loads(jsonData)
    postUrl = 'http://192.168.1.200:9008/{}/add'.format(urlPost)
    succee = requests.post(postUrl, json=data)
    return succee


def htmlToNeatForm(Path, *interceptRange):
    """
    :param Path: 路径
    :param interceptRange: 对html截取，前后定位语句
    :return: 返回一个规整的表格
    """
    global df
    try:
        interceptRange = [i for i in interceptRange]  # 遍历interceptRange到列表中
        f = open(Path, "r", encoding="utf-8").read()  # 读取html文件
        df = CutOut(f, interceptRange[0][0], interceptRange[0][1])  # 截取区间内表格
        col_name = df.columns.tolist()  # columns所有列名
        print(col_name)
        col_name[0] = '项目名'  # 重新赋予第一个列名，索引为0的列名
        df.columns = col_name  # 更新表格列名
        df.reset_index(inplace=True, drop=True)  # 重置索引，因为可能存在合并表格索引形式1，2，3，1，2，3，4
        df.drop(0, inplace=True)  # 去掉名为项目的第一行数据
        df.reset_index(inplace=True, drop=True)  # 再一次重置索引，删掉了第一行数据，需要重置
        df.set_index(df.项目名, inplace=True)  # 设置项目为索引
        df.drop('项目名', axis=1, inplace=True)  # 删除项目本身列
    except Exception as e:
        pass
    return df


def htmlToNeatFormM(Path, *interceptRange):
    """
    :param Path: 路径
    :param interceptRange: 对html截取，前后定位语句
    :return: 返回一个规整的表格
    """
    global df
    try:
        interceptRange = [i for i in interceptRange]  # 遍历interceptRange到列表中
        f = open(Path, "r", encoding="utf-8").read()  # 读取html文件
        df = CutOutM(f, interceptRange[0], interceptRange[1])  # 截取区间内表格
        col_name = df.columns.tolist()  # columns所有列名
        col_name[0] = '项目名'  # 重新赋予第一个列名，索引为0的列名
        df.columns = col_name  # 更新表格列名
        df.reset_index(inplace=True, drop=True)  # 重置索引，因为可能存在合并表格索引形式1，2，3，1，2，3，4
        # df.drop(0, inplace=True)  # 去掉名为项目的第一行数据
        df.reset_index(inplace=True, drop=True)  # 再一次重置索引，删掉了第一行数据，需要重置
        df.set_index(df.项目名, inplace=True)  # 设置项目为索引
        df.drop('项目名', axis=1, inplace=True)  # 删除项目本身列
    except Exception as e:
        pass
    return df
