from tqdm import tqdm
from setting import *
from dg_class import *


dir = r'D:\Users\Desktop\run\剩余表测试数据.txt'
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
            Authoritylimitassets(path, tradeKey)