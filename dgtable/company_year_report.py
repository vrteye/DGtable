# - * - coding: utf - 8 -*-
from basic import *
import requests


def companyYearReport(tradeKey, reportName, year):
    # f = open(Path, "r", encoding="utf-8").read()
    try:
        company_year_report_url = "http://192.168.1.200:9008/companyYearReport/add"
        company_year_report_data = {
            'tradeKey': tradeKey,  # 报告id
            'reportName': reportName,
            'quarter': '',
            'year': year
        }
        # print(company_year_report_data)
        Success = requests.post(company_year_report_url, json=company_year_report_data)
        print(Success)
    except Exception as e:
        print(e)
        pass


# path = r'D:\Users\Desktop\html2\\'

# fpath = File_Eli(path)
#
# for i in range(len(fpath)):
#     Path = path + fpath[i]
#     # print(Path)
#     tradeKeyall = tradekey(Path)
#     tradeKey = tradeKeyall[0]
#     reportName = tradeKeyall[1]
#     year = tradeKeyall[2]
#     # company_info = companyInfo(Path,tradeKey)
#     company_year_report = companyYearReport(tradeKey, reportName, year)
#     print(company_year_report)
