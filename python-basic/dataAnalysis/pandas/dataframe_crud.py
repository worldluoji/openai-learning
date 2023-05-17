import pandas as pd
#DataFrame就是一张表，由多个Series列组成，还包括标题columns

pd.set_option('display.unicode.east_asian_width', True)

data = [[80,70,69],[90,80,77],[65,59,69]]
index = ['张三','李四','王麻子']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data,index=index,columns=columns)

#增加一列物理
df.loc[:,'物理'] = [88,77,66]
print(df)
print('*' * 16)
#指定位置插入一列
df.insert(1, '生物', [66,77,88])
print(df)
print('*' * 16)

#增加一行
df.loc['钱多多'] = [33,22,44,55,66]
print(df)
#批量增加
df_insert = pd.DataFrame({'语文':[90,80],'数学':[90,88],'英语':[89,99],'物理':[78,88],'生物':[97,88]}
                        ,index=['渣渣灰','渣渣非'])
df1 = df._append(df_insert)
print(df1)
print('*' * 16)

#修改列名,inplace表示直接修改原对象
df.rename(columns={'语文':'语文（三年级）'}, inplace=True)
print(df)
#修改行名
df.rename({'王麻子':'王梅梅'}, axis=0, inplace=True)
print(df)
print('*' * 16)

#修改内容
df.loc['钱多多','生物'] = 99
print(df)
#生物全部改为99
df.loc[:,'生物'] = 99
print('*' * 16)
print(df)
#修改张三成绩
df.loc['张三'] = [88,99,66,77,99]
print('*' * 16)
print(df)
#修改李四成绩
print('*' * 16)
df.iloc[1,:] = [66,88,99,87,98]
print(df)

#删除axis为0为删除行，1为删除列
df.drop(['生物'],axis=1,inplace=True)
print(df)
print('*' * 16)
#删除第一个语文小于70分的行，直接.index就是删除所有语文小于70分的
df.drop(index=df[df['数学'] < 70].index[0],inplace=True)
print(df)
print('*' * 16)