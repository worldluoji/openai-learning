import pandas as pd

#列对齐
pd.set_option('display.unicode.east_asian_width', True)

#一个Series就是对应表的一列，不指定index，就是0,1,2...
s1 = pd.Series([80,60,75])
print(s1)

#index与data数量保持一致
s2 = pd.Series(data=[80,60,75], index=['张三','李四','王麻子'])
print(s2)

print('*' * 8 + '下标取值' + '*' * 8)
print(s2[0], s2[1], s2[2])

print('*' * 8 + 'index取值' + '*' * 8)
print(s2['张三'], s2['李四'], s2['王麻子'])

print('*' * 8 + '切片' + '*' * 8)
print(s2[0:2])
print(s2['张三':'王麻子'])

print('*' * 8 + 'attribues' + '*' * 8)
print(s2.index)
print(s2.values)