import pandas as pd
#DataFrame就是一张表，由多个Series列组成，还包括标题columns

pd.set_option('display.unicode.east_asian_width', True)

#读取excel,sheet_name指定excel的第几个sheet页，默认0
df = pd.read_excel('./test.xlsx', sheet_name=1)

print(df.head())

#info()可打印出表的信息，包阔数据类型，有多少非空项等
print(df.info())

#判断数据是否存在缺失
print(df.isnull())

print('*' * 8 + '丢弃存在NA的行——缺失值删除处理:')
df1 = df.dropna()
print(df1)

print('*' * 8 + '指定项缺失删除,通过reset_index重置索引：')
df2 = df[df['BOSS'].notnull()].reset_index(drop=True)
print(df2)

#填充缺失项
df['BOSS'] = df['BOSS'].fillna('UnKnown')
print(df)

df.loc[3] = [2,'国际米兰',20,43,'ZKY']
print(df)
#去重
df3 = df.drop_duplicates()
print(df3)

#列去重
df4 = df.drop_duplicates(['BOSS'])
print(df4)