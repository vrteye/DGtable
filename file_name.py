from method import *
import os
import re
import json
import time
from basic import *
import requests
from tqdm import tqdm
from dg_class import *

path_txt = r'D:\Users\Desktop\run\剩余表测试数据.txt'
data = File_List(path_txt)
dir = r'\\192.168.1.200\root\深交所2018-2021年报_new\html\\'
for i in range(len(data)):
    if data[i].endswith(".html"):
        path = dir + data[i]
        print(path)
        tradeKeyall = tradekey(path)
        tradeKey = tradeKeyall[0]
        reportName = tradeKeyall[1]
        year = tradeKeyall[2]

