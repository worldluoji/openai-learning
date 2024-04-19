# 类型注解(Type Annotations)

类型注解是Python 3引入的一项重要特性，旨在增强代码的可读性和可维护性，尤其是在大型项目和团队协作中。
虽然Python是一种动态类型语言，即变量无需事先声明其类型，但在函数定义、变量声明或类属性上使用类型注解，
可以让开发者明确表达预期的数据类型，有利于静态类型检查工具（如mypy）进行类型检查，以及IDE提供更好的代码提示和错误检测。


示例：
```
def add(a: int, b: int) -> int:
    return a + b
```

类似于typescript.


## Bool作为Int的子类
在Python 3中，布尔类型（bool）被视为整数类型（int）的子类。这意味着：

True和False可以直接与整数进行算术运算，因为它们分别对应整数值1和0：
```
assert True + 1 == 2
assert False * 3 == 0
```

isinstance()函数会认为布尔值是整数的一种，而type()则会严格区分布尔值和整数：

```
assert isinstance(True, int)  # True
assert isinstance(False, int)  # True

assert type(True) == bool  # True
assert type(False) == bool  # True
assert type(True) != int  # True
assert type(False) != int  # True
```
 
虽然布尔值可以与整数相等比较，但使用is关键字来判断类型时，布尔值和整数会被视为不同的类型：
```
assert True == 1  # True
assert False == 0  # True

assert True is not 1  # True
assert False is not 0  # True
```