import pandas as pd
#DataFrame就是一张表，由多个Series列组成，还包括标题columns

pd.set_option('display.unicode.east_asian_width', True)

data = [[80,70,69],[90,80,77],[65,59,69]]
index = ['张三','李四','王麻子']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data,index=index,columns=columns)

#抽取行使用loc或者iloc
print(df.loc[['张三','王麻子']])
print('*' * 16)
print(df.iloc[[0,2]])
print('*' * 16)
print(df.iloc[1:2])
print('*' * 16)
print(df.loc['李四'::])
print('*' * 16)

#取英语和语文两列，抽取列直接使用列名
print(df[['语文','英语']])

print('*' * 16)

#loc和iloc包含两个参数，第一个代表行，第二个代码表列
print(df.iloc[0:2,0:2])
print('*' * 16)

#抽取第二行第三列
print(df.iloc[[1],[2]])
print('*' * 16)

#筛选处语文>65并且数学>70的
print(df.loc[(df['语文'] > 65) & (df['数学'] > 70)])