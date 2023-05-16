# pythonic

## 1. 变量交换
Bad
```
tmp = a
a = b
b = tmp
```
Pythonic
```
a,b = b,a
```

## 2.  列表推导
Bad
```
my_list = []
for i in range(10):
    my_list.append(i*2)
Pythonic
```
```
my_list = [i*2 for i in range(10)]
```

## 3.  单行表达式
虽然列表推导式由于其简洁性及表达性，被广受推崇。

但是有许多可以写成单行的表达式，并不是好的做法。

Bad
```
print('one'); print('two')

if x == 1: print('one')

if <complex comparison> and <other complex comparison>:
    # do something
```

Pythonic
```
print('one')
print('two')

if x == 1:
    print('one')

cond1 = <complex comparison>
cond2 = <other complex comparison>
if cond1 and cond2:
    # do something
```

## 4. 带索引遍历
Bad
```
for i in range(len(my_list)):
    print(i, "-->", my_list[i])
```

Pythonic
```
for i,item in enumerate(my_list):
    print(i, "-->", item)
```

## 5. 序列解包
Pythonic
```
a, *rest = [1, 2, 3]
# a = 1, rest = [2, 3]

a, *middle, c = [1, 2, 3, 4]
# a = 1, middle = [2, 3], c = 4
```

## 6. 字符串拼接
Bad
```
letters = ['s', 'p', 'a', 'm']
s=""
for let in letters:
    s += let
```

Pythonic
```
letters = ['s', 'p', 'a', 'm']
word = ''.join(letters)
```

## 7. 真假判断
Bad
```
if attr == True:
    print('True!')

if attr == None:
    print('attr is None!')
```

Pythonic
```
if attr:
    print('attr is truthy!')

if not attr:
    print('attr is falsey!')

if attr is None:
    print('attr is None!')
```

## 8. 访问字典元素
Bad
```
d = {'hello': 'world'}
if d.has_key('hello'):
    print(d['hello'])    # prints 'world'
else:
    print('default_value')
```

Pythonic
```
d = {'hello': 'world'}

print(d.get('hello', 'default_value')) # prints 'world'
print(d.get('thingy', 'default_value')) # prints 'default_value'
```
Or:
```
if 'hello' in d:
    print d['hello']
```

## 9. 操作列表
Bad
```
a = [3, 4, 5]
b = []
for i in a:
    if i > 4:
        b.append(i)
```
Pythonic
```
a = [3, 4, 5]
b = [i for i in a if i > 4]
```
Or:
```
b = filter(lambda x: x > 4, a)
```

Bad
```
a = [3, 4, 5]
for i in range(len(a)):
    a[i] += 3
```
Pythonic
```
a = [3, 4, 5]
a = [i + 3 for i in a]
```
Or:
```
a = map(lambda i: i + 3, a)
```

## 10. 文件读取
Bad
```
f = open('file.txt')
a = f.read()
print a
f.close()
```
Pythonic
```
with open('file.txt') as f:
    for line in f:
        print line
```

## 11. 代码续行
Bad
```
my_very_big_string = """For a long time I used to go to bed early. Sometimes, \
    when I had put out my candle, my eyes would close so quickly that I had not even \
    time to say “I’m going to sleep.”"""

from some.deep.module.inside.a.module import a_nice_function, another_nice_function, \
    yet_another_nice_function
```

Pythonic
```
my_very_big_string = (
    "For a long time I used to go to bed early. Sometimes, "
    "when I had put out my candle, my eyes would close so quickly "
    "that I had not even time to say “I’m going to sleep.”"
)

from some.deep.module.inside.a.module import (
    a_nice_function, another_nice_function, yet_another_nice_function)
```

## 12. 显式代码
Bad
```
def make_complex(*args):
    x, y = args
    return dict(**locals())
```
Pythonic
```
def make_complex(x, y):
    return {'x': x, 'y': y}
```

## 13. 使用占位符
Pythonic
```
filename = 'foobar.txt'
basename, _, ext = filename.rpartition('.')
```

## 14. 链式比较
Bad
```
if age > 18 and age < 60:
    print("young man")
```
Pythonic
```
if 18 < age < 60:
    print("young man")
```
理解了链式比较操作，那么你应该知道为什么下面这行代码输出的结果是 False
```
>>> False == False == True 
False
```

## 15. 三目运算
这个保留意见。随使用习惯就好。
Bad
```
if a > 2:
    b = 2
else:
    b = 1
#b = 2
```
Pythonic
```
a = 3   
b = 2 if a > 2 else 1
#b = 2
```