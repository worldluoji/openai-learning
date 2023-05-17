import pandas as pd
# pandas依赖openpyxl读取excel，也需要先安装openpyxl pip3 install openpyxl

#列名对齐
pd.set_option('display.unicode.east_asian_width', True)

#设置最大行数和最大列数
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 10)

#读取excel,sheet_name指定excel的第几个sheet页，默认0
df = pd.read_excel('./test.xlsx', sheet_name=0)

#打印表的前5行
print(df.head())
print('*' * 16)

#header=0表示设置第一行为列索引（header=None则为数字，不设默认第一行），indexl_col=0表示设置第一列为行索引（不设则为数字）
df = pd.read_excel('./test.xlsx', header=0, index_col=0, usecols=[0,1,3])
#usecols指定导入哪些列

#打印表的前5行
print(df.head())