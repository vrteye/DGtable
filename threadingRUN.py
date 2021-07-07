from tqdm import tqdm

# from public import *

"""
rtable
"""
from dgtable.develop_putinto import *        # 研发投入（develop_putinto）

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


            # Acceptlabourstate(Path, tradeKey)
            # Accountingfinancialdata(Path, tradeKey)
            # Assetsdecrvalueloss(Path, tradeKey)
            # Comstaffstate(Path, tradekey)
            # Doingprojectchangestate(Path, tradeKey)
            # FallpriceImpairmentprepare(Path, tradeKey)
            # Goodsstockclassify(Path, tradeKey)
            # Goodwilldecrvalprepare(Path, tradeKey)
            # MergeProfit(Path, tradeKey, y_list_pf)
            # MergeCashFlow(Path, tradeKey, y_list_kb)
            # Nonpropertyrightassetstate(Path, tradeKey)
            # Operatingprofit(Path, tradeKey)
            # ParentCompanyAssetsDebt(Path, tradeKey, y_list_mzf)
            # Profittaxadjustproces(Path, tradeKey)
            # Providelabourstate(Path, tradeKey)

            Developputinto(Path, tradeKey)
            # Comstaffstate(Path, tradeKey)

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

