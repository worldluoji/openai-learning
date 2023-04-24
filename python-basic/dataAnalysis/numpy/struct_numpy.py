
import numpy as np
persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S','i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)
print(peoples)
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))

'''
'b'：布尔值
'i'：符号整数
'u'：无符号整数
'f'：浮点
'c'：复数浮点
'm'：时间间隔
'M'：日期时间
'O'：Python 对象
'S', 'a'：字节串
'U'：Unicode
'V'：原始数据(void)
'''