from tqdm import tqdm
from setting import *

# from public import *

from dgtable.accept_labour_state import *        # Acceptlabourstate
from dgtable.accounting_financial_data import *      # Accountingfinancialdata
from dgtable.assets_decr_value_loss import *     # Assetsdecrvalueloss
from dgtable.com_staff_state import *        # Comstaffstate
from dgtable.doing_project_change_state import *     # Doingprojectchangestate
from dgtable.fallprice_Impairment_prepare import *       # FallpriceImpairmentprepare
from dgtable.goods_stock_classify import *       # Goodsstockclassify
from dgtable.goodwill_decrval_prepare import *       # Goodwilldecrvalprepare
from dgtable.merge_profit import *       # MergeProfit
from dgtable.merge_cash_flow import *        # MergeCashFlow
from dgtable.non_property_right_asset_state import *     # Nonpropertyrightassetstate
from dgtable.operating_profit import *       # Operatingprofit
from dgtable.parent_company_assets_debt import *     # ParentCompanyAssetsDebt
from dgtable.profit_tax_adjust_proces import *       # Profittaxadjustproces
from dgtable.provide_labour_state import *       # Providelabourstate






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


            Acceptlabourstate(Path, tradeKey)
            Accountingfinancialdata(Path, tradeKey)
            Assetsdecrvalueloss(Path, tradeKey)
            Comstaffstate(Path, tradekey)
            Doingprojectchangestate(Path, tradeKey)
            FallpriceImpairmentprepare(Path, tradeKey)
            Goodsstockclassify(Path, tradeKey)
            Goodwilldecrvalprepare(Path, tradeKey)
            MergeProfit(Path, tradeKey, y_list_pf)
            MergeCashFlow(Path, tradeKey, y_list_kb)
            Nonpropertyrightassetstate(Path, tradeKey)
            Operatingprofit(Path, tradeKey)
            ParentCompanyAssetsDebt(Path, tradeKey, y_list_mzf)
            Profittaxadjustproces(Path, tradeKey)
            Providelabourstate(Path, tradeKey)


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

