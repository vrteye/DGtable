from public import *
from method import *
from company_info import *


def tradeKey(f):
    financial = CutOut(f, '、主要会计数据和财务指标', '、分季度主要财务指标')
    year = financial.columns.tolist()[1]
    types = '年度报告'
    df = CutOut(f, '、公司信息', '、联系人和联系方式')
    stockCode = df.iloc[0, 3]
    year_report_id = year + '_' + stockCode + '_' + types
    tradeKey = year_report_id.replace(' ', '')
    company_id = stockCode
    return tradeKey
