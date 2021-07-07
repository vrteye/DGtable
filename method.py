import re
import json
import time
import random
import urllib
import codecs
import hashlib
import os, pprint
import urllib.parse, urllib.request


def File_List(url):
    # 提供全链接，去除文本中的换行符;结果返回一个列表，每个段落装在字符串,整体装在列表，打印出来。
    file = open(url, encoding='utf-8')
    file = list(file)
    file = [x for x in file if x != '\n']
    # 如果要装在字符串中
    # str_file = ''.join(file)
    return file


# F = File_List('/Volumes/U盘/test/2.txt')
# print(F[2])
def Txt_Create(Target_Path, name, msg):
    # 新创建的txt文件的存放路径,需要提供url,生成文本及内容。msg是str。
    full_path = Target_Path + 'SoftLink' + '.txt'  # 也可以创建一个.doc的word文档

    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world
    file.close()
    return file


def File_Eli(path):
    # 剔除隐藏的文件,需要提供被测文件的路径，生成一个剔除隐藏文件后的列表。
    path = os.listdir(path)
    ls = []
    for f in path:
        # print(f)
        if not f.startswith('.'):
            ls.append(f)
    return ls


def Read_File(Path, ls):
    # 提供path(路径)和ls(剔除隐藏文件的的列表)，能打印出列表文本中的内容
    # print("#"+Path,ls)
    file_content = []
    for i in range(len(ls)):
        url = Path + ls[i]
        f = open(url, encoding="utf-8")
        f = list(f)
        file_content.append(f)
    return file_content


# 生成文件夹
def Make_Folers(Target_Path, Dir_Name):
    # all_link = '/Users/lilong/Desktop/in/{}'.format(dir_name)
    # /Users/lilong/Desktop/
    Target_Link = Target_Path + Dir_Name
    Dir = os.makedirs(Target_Link)
    return Dir
