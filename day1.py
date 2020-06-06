# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 00:08:38 2020

@author: JU
"""
#1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
#檔案:會包成檔案提供下載，格式包含常用的標準格式，例如:CSV JSON 等等通用的格式
#API:提供程式化的連接的接口，讓工程師可以選擇資料中要讀取的特定部分，而不需要把整批資料事先完整下載回來
#網頁爬蟲:資料沒有以檔案或API提供，但出現在網頁上，可以利用網頁爬蟲程式，將網頁的資料解析所需的部分


#2.「下載指定檔案到 Data 資料夾，存成檔名 Homework.txt」的檔案網址：https://www.w3.org/TR/PNG/iso_8859-1.txt 或任一個 .txt 的檔案網址
from urllib.request import urlretrieve

import os

try:
    os.makedirs("./data/",exist_ok = True)
    print("資料夾建立成功")

except:
    print("發生錯誤!")
    

urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt","./data/Homework.txt")

#檢查 Data 資料夾是否有 Homework.txt 檔名之檔案

filepath = "./data/Homework.txt"
if os.path.exists(filepath):
    print("檔案存在")
else:
    print("檔案不存在")
    
#將「Hello World」字串覆寫到 Homework.txt 檔案
with open("./data/Homework.txt","w") as f:
    f.write("Hello World")
    
with open("./data/Homework.txt","r") as f:


#檢查 Homework.txt 檔案字數是否符合Hello World字數: 
    if len(f.read()) == len("Hello World"):    
        print("符合")
    
    else:
        print("不符合")
 
f.close()        
    
    





   

    
  