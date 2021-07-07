# - * - coding: utf - 8 -*-
from public import *
from basic import *
import requests


def companyInfo(Path, tradeKey, srcFileName):
    try:
        f = open(Path, "r", encoding="utf-8").read()
        df = CutOut(f, '、公司信息', '、联系人和联系方式')
        col = df.columns.tolist()
        stockCode = col[3]
        ChineseNameofCompany = col[1]
        df.columns.values[0] = 'DATA'
        df.set_index(df.DATA, inplace=True)
        col = df.columns.tolist()
        dfx = df.iloc[:, 0:2]
        col_name = dfx.columns.tolist()[1]  # 列名

        companyName = dfx.loc['公司的中文名称', col_name]

        companyForshort = ChineseNameofCompany
        companyZhName = dfx.loc['公司的中文名称', col_name]
        companyZhForshort = dfx.loc['公司的中文简称', col_name]
        legalPerson = dfx.loc['公司的法定代表人', col_name]
        registerAddress = dfx.loc['注册地址', col_name]
        registerZipcode = dfx.loc['注册地址的邮政编码', col_name]
        officeAddress = dfx.loc['办公地址', col_name]
        officeZipcode = dfx.loc['办公地址的邮政编码', col_name]
        email = dfx.loc['电子信箱', col_name]
        # company_id = stockCode
        try:
            companyEnName = dfx.loc['公司的外文名称（如有）', col_name]
        except Exception as e:
            companyEnName = ''
            pass

        try:
            websiteUrl = dfx.loc['公司网址', col_name]
        except Exception as e:
            websiteUrl = dfx.loc['公司国际互联网网址', col_name]
            pass

        try:
            companyEnForshort = dfx.loc['公司的外文名称缩写（如有）', col_name]
        except Exception as e:
            companyEnForshort = ''
            pass

        # col_name = df.columns.tolist()  # 列名

        company_info_data = {
            'companyName': companyName,  # 公司名称
            'companyForshort': companyForshort,  # 公司简称
            'companyZhName': companyZhName,  # 公司中文名称
            'companyZhForshort': companyZhForshort,  # 公司中文简称
            'stockCode': stockCode,  # 股票代码
            'companyEnName': companyEnName,  # 公司外文名称
            'companyEnForshort': companyEnForshort,  # 公司外文简称
            'legalPerson': legalPerson,  # 公司法人代表
            'registerAddress': registerAddress,  # 公司注册地址
            'registerZipcode': registerZipcode,  # 注册地址邮编
            'officeAddress': officeAddress,  # 公司办公地址
            'officeZipcode': officeZipcode,  # 办公地址邮编
            'websiteUrl': websiteUrl,  # 公司网址
            'email': email,  # 公司邮箱
            'tradeKey': tradeKey,  # 报告id
            'srcFileName': srcFileName
        }
        jsonData = json.dumps(company_info_data, indent=4, separators=(',', ': '), ensure_ascii=False)
        data = json.loads(jsonData)
        companyInfo_url = "http://192.168.1.200:9008/companyInfo/add"
        Success = requests.post(companyInfo_url, json=data)
        print(Success)
    except Exception as e:
        print(e)
        pass


# path = r'D:\Users\Desktop\html\阜新德尔汽车部件股份有限公司.html'
# tradekey = tradekey(path)[0]
# ss = companyInfo(path, tradekey)
# companyInfos = requests.post('https://192.168.1.200:9008/companyInfo/add', json=ss)
#
# print(companyInfos)
