import pandas as pd
#DataFrame就是一张表，由多个Series列组成，还包括标题columns

pd.set_option('display.unicode.east_asian_width', True)

#读取excel,sheet_name指定excel的第几个sheet页，默认0
df = pd.read_excel('./test.xlsx', sheet_name=1)

print(df.head())

print('*' * 8 + '按积分升序排列' + '*' * 8)
df1 = df.sort_values(by='积分', ascending=True)
print(df1.head())

df2 = df1.sort_values(by=['排名'])
print(df2.head())

print('*' * 8 + '分组' + '*' * 8)
df3 = df2.groupby(['场次'])['积分'].sum().reset_index()
print(df3)

print('*' * 8 + 'rank积分排名' + '*' * 8)
df2['积分排名'] = df2['积分'].rank(method='min', ascending=False)
print(df2)