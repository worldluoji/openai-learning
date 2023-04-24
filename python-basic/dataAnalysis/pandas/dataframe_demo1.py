import pandas as pd
#DataFrame就是一张表，由多个Series列组成，还包括标题columns

pd.set_option('display.unicode.east_asian_width', True)

data = [[80,70,69],[90,80,77],[65,59,69]]
index = [0,1,2]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print('*' * 16)
for col in df.columns:
    series = df[col]
    print(series)

print('*' * 8 + '通过字典创建' + '*' * 8)
df2 = pd.DataFrame({
    '语文':[50,60,70],
    '数学':[30,40,50],
    '英语':[20,30,40]
}, index=['a','b','c'])
print(df2)
#合理建立索引index，如果索引唯一，那么底层数据结构是哈希，效率最高；如果索引不唯一，但有序，会使用二分查找。
print('*' * 8 + '重新建立行索引' + '*' * 8)
print(df2.reindex(index=['b','a','c'], columns=['数学','语文','英语']))

#设置第一列为索引
df3 = df2.set_index(['数学'])
print(df3)