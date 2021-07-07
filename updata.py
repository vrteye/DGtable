from tqdm import tqdm

from dgtable.goodwill_decrval_prepare import Goodwilldecrvalprepare

# from public import *
# from mergeAssetsDebt import *
# from NumberOfEmployees import *

"""
newtable
"""
from dgtable.prepare_payment_item import *

path = r'\\192.168.1.200\root\深交所2018-2021年报\pdf\html\\'
# path = r'D:\Users\Desktop\h1\\'
fpath = File_Eli(path)

with tqdm(total=len(fpath)) as bar:        # 进度条
    for i in range(len(fpath)):
        # time.sleep(0.1)
        bar.update(i)
        srcDir = fpath[i]
        Path = path + fpath[i]

        if Path.endswith(".html"):
            tradeKeyall = tradekey(Path)
            tradeKey = tradeKeyall[0]
            reportName = tradeKeyall[1]
            year = tradeKeyall[2]


            # try:
            #     s = companyInfo(Path, tradeKey, srcDir)  #
            #     print(s)
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     s = companyYearReport(tradeKey, reportName, year)  #
            #     print(s)
            # except Exception as e:
            #     print(e)
            # pass

            """
            630
            """
            # try:
            #     s = Doingprojectchangestate(Path, tradeKey)
            #     print(s)
            # except Exception as e:
            #     pass

            try:
                s = Goodwilldecrvalprepare(Path, tradeKey)
                print(s)
            except Exception as e:
                pass



            """newtbale"""


            #
            # try:
            #     Baddebtpreparestate(Path, tradeKey)     # 坏账准备计提情况 bad_debt_prepare_state
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Currencycapital(Path, tradeKey)     # 货币资金 currency_capital
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Currentbaddebtpreparestate(Path, tradeKey)      # 本期计提、收回或转回的坏账准备情况	current_bad_debt_prepare_state
            # except Exception as e:
            #     print(e)
            # pass
            # try:
            #     Currentlossprofitdetail(Path, tradeKey)     # 当期非经常性损益明细 current_loss_profit_detail
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Customersalescondition(Path, tradeKey)      # 销售客户情况（customer_sales_condition）
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     FinancereportitemFinance(Path, tradeKey)        # 财务报相关项目情况 finance_report_item_Finance
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Firstsurplusreceivablestate(Path, tradeKey)     # 按欠款方归集的期末余额前五名的应收账款情况	first_surplus_receivable_state
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Itemperformstate(Path, tradeKey)        # 承诺事项履行情况 item_perform_state
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Otherreceivableaccountagereveal(Path, tradeKey)     # 其他应收账款-按账龄披露 other_receivable_account_age_reveal
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Receivableaccountagereveal(Path, tradeKey)      # 应收账款-按账龄披露 receivable_account_age_reveal
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Receivablebillcategory(Path, tradeKey)      # 应收票据类别 receivable_bill_category
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Receivablebillitem(Path, tradeKey)      # 应收票据项目 receivable_bill_item
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Receivablebillitem(Path, tradeKey)      # 应收票据项目 receivable_bill_item
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Revenueaccountreveal(Path, tradeKey)        # 应收账款分类披露 revenue_account_reveal
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     ParentCompanyProfit(Path, tradeKey, y_list_mlr)
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Revenueitem(Path, tradeKey)     # 应收项目 revenue_item
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Fixedassetsstate(Path, tradeKey, fixed)  # 固定资产情况（fixed_assets_state）
            # except Exception as e:
            #     print(e)
            # pass
            #
            # try:
            #     Preparepaymentitem(Path, tradeKey)       # 预付款项 prepare_payment_item
            # except Exception as e:
            #     print(e)
            # pass

