from tqdm import tqdm
from setting import *
from dg_class import *


dir = r'\\192.168.1.200\root\深交所2018-2021年报\pdf\html\\'
# path = r'D:\Users\Desktop\h1\\'
fpath = File_Eli(dir)

with tqdm(total=len(fpath)) as bar:        # 进度条
    for i in range(len(fpath)):
        # time.sleep(0.1)
        bar.update(i)
        srcDir = fpath[i]
        path = dir + fpath[i]
        if path.endswith(".html"):
            tradeKeyall = tradekey(path)
            tradeKey = tradeKeyall[0]       # 年报唯一id
            reportName = tradeKeyall[1]     # xx年度报告
            year = tradeKeyall[2]       # 年度
# 各表函数
            companyInfo(path, tradeKey, srcDir)
            companyYearReport(tradeKey, reportName, year)
            Acceptlabourstate(path, tradeKey)
            Supplierdata(path, tradeKey)
            Accountingfinancialdata(path, tradeKey)
            Assetsdecrvalueloss(path, tradeKey)
            Baddebtpreparestate(path, tradeKey)
            Comstaffstate(path, tradekey)
            Currencycapital(path, tradeKey)
            Currentbaddebtpreparestate(path, tradeKey)
            Currentlossprofitdetail(path, tradeKey)
            Customerdata(path, tradeKey)
            Customersalescondition(path, tradeKey)
            Developputinto(path, tradeKey)
            Doingproject(path, tradeKey)
            Doingprojectchangestate(path, tradeKey)
            Doingprojectstate(path, tradeKey)
            FallpriceImpairmentprepare(path, tradeKey)
            FinancereportitemFinance(path, tradeKey)
            Firstsurplusreceivablestate(path, tradeKey)
            Fixedassetsstate(path, tradeKey, fixed)
            Goodslabourservicerelationtrade(path, tradeKey)
            Goodsstockclassify(path, tradeKey)
            Goodwillaccountvalue(path, tradeKey)
            Goodwilldecrvalprepare(path, tradeKey)
            Itemperformstate(path, tradeKey)
            MergeCashFlow(path, tradeKey, y_list_kb)
            MergeProfit(path, tradeKey, y_list_pf)
            mergeAssetsDebt(path, tradekey, y_list_ml)
            Nonpropertyrightassetstate(path, tradeKey)
            Nonpropertyrightlanduserightstate(path, tradeKey)
            Operatingprofit(path, tradeKey)
            Otherreceivableaccountagereveal(path, tradeKey)
            ParentCompanyAssetsDebt(path, tradeKey, y_list_mzf)
            ParentCompanyProfit(path, tradeKey, y_list_mlr)
            Preparepaymentitem(path, tradeKey)
            Profittaxadjustproces(path, tradeKey)
            Providelabourstate(path, tradeKey)
            Receivableaccountagereveal(path, tradeKey)
            Receivablebillcategory(path, tradeKey)
            Receivablebillitem(path, tradeKey)
            Revenueaccountreveal(path, tradeKey)
            Revenueitem(path, tradeKey)
            Suppliersalescondition(path, tradeKey)


