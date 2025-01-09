"""
@File    :   forcast.py
@Time    :   2024/10/09 10:33:46
@Author  :   glx 
@Version :   1.0
@Contact :   18095542g@connect.polyu.hk
@Desc    :   None
"""

# here put the import lib
import pandas as pd

data = pd.read_csv("vote.csv", sep="\t", header=None)
print(data.head())
with open("header.txt", "r", encoding="utf-8", errors="ignore") as f:
    header = f.readlines()
    header = [i.strip() for i in header]
data.columns = header
print(data.head())
