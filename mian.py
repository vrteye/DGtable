# from public import *
# from mergeAssetsDebt import *
# from NumberOfEmployees import *
from dgtable.company_year_report import *

# from provide_labour_state import *      # 提供劳务情况
# from goods_stock_classify import *      # 存货分类表
# from profit_tax_adjust_proces import *      # 会计利润与所得税费用调整过程（profit_tax_adjust_proces）
# from supplier_sales_condition import *      # 供应商情况（supplier_sales_condition）
# from supplier_data import *         # 供应商资料（supplier_data） 公司前 5 名供应商资料
# from customer_data import *     # 供应商资料（supplier_data）
# from goodwill_account_value import *    # 商誉账面原值（goodwill_account_value）
# from goodwill_decrval_prepare import *  # 商誉减值准备（goodwill_decrval_prepare）
# from doing_project import *     # 在建工程情况（doing_project_state）
# from doing_project_state import *       # 在建工程情况（doing_project_state）
# from dgtable.revenue_item import *      # 应收项目（revenue_item）
# from operating_profit import *      # 营业收入或营业利润（operating_profit）
# from non_property_right_asset_state import *    # 未办妥产权证书的固定资产情况（non_property_right_asset_state）
# from non_property_right_land_use_right_state import *
# from goods_labour_service_relation_trade import *
# from doing_project_change_state import *
# from fallprice_Impairment_prepare import *  # 按欠款方归集的期末余额前五名的应收账款情况（first_surplus_receivable_state）
# from dgtable.first_surplus_receivable_state import *  # 按欠款方归集的期末余额前五名的应收账款情况（first_surplus_receivable_state）

"""
newtable
"""
from dgtable.prepare_payment_item import *

# path = r'D:\Users\Desktop\html0\\'
# path = r'D:\Users\Desktop\h1\\'
path = r'\\192.168.1.200\root\深交所2018-2021年报\pdf\html\\'
# path = r'\\192.168.1.200\root\深交所2018-2021年报\testpdf\\'

# path = '/Volumes/Samsung/html/h1/'
# path = '/Volumes/Samsung/html/html0/'


fpath = File_Eli(path)

for i in range(len(fpath)):
    srcDir = fpath[i]
    Path = path + fpath[i]
    if Path.endswith(".html"):
        tradeKeyall = tradekey(Path)
        tradeKey = tradeKeyall[0]
        reportName = tradeKeyall[1]
        year = tradeKeyall[2]

        # company_year_report = companyYearReport(tradeKey, reportName, year)
        try:
            # s = Accountingfinancialdata(Path, tradeKey)     # 主要会计数据和财务指标（accounting_financial_data） s =
            # Acceptlabourstate(Path, tradeKey)     # 接受劳务情况（accept_labour_state） s = Providelabourstate(Path,
            # tradeKey)  # 接受劳务情况（accept_labour_state） s = Goodsstockclassify(Path, tradeKey)        # 存货分类表 s =
            # Profittaxadjustproces(Path, tradeKey)       # 会计利润与所得税费用调整过程（profit_tax_adjust_proces） s =
            # Suppliersalescondition(Path, tradeKey)      # 供应商情况（supplier_sales_condition） s = Assetsdecrvalueloss(Path,
            # tradeKey)             # 资产减值损失（assets_decr_value_loss） s = Supplierdata(Path, tradeKey)        #
            # 供应商资料（supplier_data） 公司前 5 名供应商资料 s = Customerdata(Path, tradeKey)        # 供应商资料（supplier_data） s =
            # Goodwillaccountvalue(Path, tradeKey)  # 商誉账面原值（goodwill_account_value） s = Goodwilldecrvalprepare(Path,
            # tradeKey)  # 商誉减值准备（goodwill_decrval_prepare） s = Doingproject(Path, tradeKey)        #
            # 在建工程情况（doing_project_state） s = Doingprojectstate(Path, tradeKey)       # 在建工程情况（doing_project_state） s =
            # s = Revenueitem(Path, tradeKey)       # 应收项目（revenue_item） s = Operatingprofit(Path, tradeKey)     #
            # 营业收入或营业利润（operating_profit） s = Nonpropertyrightassetstate(Path, tradeKey)      #
            # 未办妥产权证书的固定资产情况（non_property_right_asset_state） s = Nonpropertyrightlanduserightstate(Path, tradeKey)
            # 未办妥产权证书的土地使用权情况（non_property_right_land_use_right_state） s = Goodslabourservicerelationtrade(Path,
            # tradeKey) s = Doingprojectchangestate(Path, tradeKey)     # 重要在建工程项目本期变动情况（doing_project_change_state） s =
            # FallpriceImpairmentprepare(Path, tradeKey)      # 跌价减值准备（fallprice_Impairment_prepare）
            # company_info = companyInfo(Path, tradeKey, srcDir)
            # company_year_report = companyYearReport(tradeKey, reportName, year)
            # NumberOfEmployees = NumberOfEmploy(Path, tradeKey)
            # mergeAssetsDebt = mergeAssetsDebt(Path, tradeKey)

            # s = Firstsurplusreceivablestate(Path, tradeKey)  # 按欠款方归集的期末余额前五名的应收账款情况（first_surplus_receivable_state）
            # s = Firstsurplusreceivablestate(Path, tradeKey)

            """newtbale"""
            # s = Baddebtpreparestate(Path, tradeKey)     # 坏账准备计提情况 bad_debt_prepare_state
            # s = Currencycapital(Path, tradeKey)     # 货币资金 currency_capital
            # s = Currentbaddebtpreparestate(Path, tradeKey)      # 本期计提、收回或转回的坏账准备情况	current_bad_debt_prepare_state
            # s = Currentlossprofitdetail(Path, tradeKey)     # 当期非经常性损益明细 current_loss_profit_detail
            # s = Customersalescondition(Path, tradeKey)      # 销售客户情况（customer_sales_condition）
            # s = FinancereportitemFinance(Path, tradeKey)        # 财务报相关项目情况 finance_report_item_Finance
            # s = Firstsurplusreceivablestate(Path, tradeKey)     # 按欠款方归集的期末余额前五名的应收账款情况	first_surplus_receivable_state
            # s = Itemperformstate(Path, tradeKey)        # 承诺事项履行情况 item_perform_state
            # s = Otherreceivableaccountagereveal(Path, tradeKey)     # 其他应收账款-按账龄披露 other_receivable_account_age_reveal
            # s = Receivableaccountagereveal(Path, tradeKey)      # 应收账款-按账龄披露 receivable_account_age_reveal
            # s = Receivablebillcategory(Path, tradeKey)      # 应收票据类别 receivable_bill_category
            # s = Receivablebillitem(Path, tradeKey)      # 应收票据项目 receivable_bill_item
            # s = Revenueaccountreveal(Path, tradeKey)        # 应收账款分类披露 revenue_account_reveal
            # s = ParentCompanyProfit(Path, tradeKey, y_list_mlr)
            # s = Revenueitem(Path, tradeKey)     # 应收项目 revenue_item
            # s = Fixedassetsstate(Path, tradeKey, fixed)  # 固定资产情况（fixed_assets_state）
            # s = Preparepaymentitem(Path, tradeKey)       # 预付款项 prepare_payment_item

            """
            v1 正式注入数据
            """
            # s = companyInfo(Path, tradeKey, srcDir)
            s = companyYearReport(tradeKey, reportName, year)
            # s = Acceptlabourstate(Path, tradeKey)  # 接受劳务情况（accept_labour_state）
            # s =Accountingfinancialdata(Path, tradeKey)
            # s = Assetsdecrvalueloss(Path, tradeKey)
            print(s)

        except Exception as e:
            print(e)
            pass
