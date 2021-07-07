# from public import *
# from company_info import *
# from mergeAssetsDebt import *
# from NumberOfEmployees import *
# from company_year_report import *

# from accounting_financial_data import *
# from accept_labour_state import *       # 接受劳务情况
# from provide_labour_state import *      # 提供劳务情况
# from goods_stock_classify import *      # 存货分类表
# from profit_tax_adjust_proces import *      # 会计利润与所得税费用调整过程（profit_tax_adjust_proces）
# from supplier_sales_condition import *      # 供应商情况（supplier_sales_condition）
# from assets_decr_value_loss import *        # 资产减值损失（assets_decr_value_loss）
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
# paths = r'\\192.168.1.200\root\深交所2018-2021年报\testpdf'

# path = '/Volumes/Samsung/html/h1/'
# path = '/Volumes/Samsung/html/html0/'


fpath = File_Eli(paths)

for i in range(len(fpath)):
    srcDir = fpath[i]
    Path = paths + fpath[i]
    if Path.endswith(".html"):
        print(Path)

    # tradeKeyall = tradekey(Path)
    # tradeKey = tradeKeyall[0]
