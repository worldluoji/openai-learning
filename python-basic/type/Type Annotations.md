# 类型注解(Type Annotations)

类型注解是Python 3引入的一项重要特性，旨在增强代码的可读性和可维护性，尤其是在大型项目和团队协作中。
虽然Python是一种动态类型语言，即变量无需事先声明其类型，但在函数定义、变量声明或类属性上使用类型注解，
可以让开发者明确表达预期的数据类型，有利于静态类型检查工具（如mypy）进行类型检查，以及IDE提供更好的代码提示和错误检测。


示例：
```
def add(a: int, b: int) -> int:
    return a + b

# 二维int数组
def longestLine(mat: List[List[int]]) -> int:
    return mat[0][1] + mat[1][0]

# set
def get_unique_integers(items: List[int]) -> Set[int]:
    """
    Given a list of integers, this function returns a set of unique integers.
    
    :param items: A list of integers that may contain duplicates.
    :return: A set of unique integers from the input list.
    """
    return set(items)
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

<br>

## Optional
在Python中，`Optional`是一个类型提示（type hint），用来指示一个变量、函数参数或返回值可以是某种类型，也可以是`None`。
这在类型注解中非常有用，因为它帮助开发者和阅读代码的人明确了解某个变量是否可能为`None`，从而可以在使用之前做出适当的检查，避免运行时错误。

`Optional`是`typing`模块中的一个类型别名，自Python 3.5引入`typing`模块以来，它就被用来增强代码的可读性和健壮性。使用`Optional`的方式如下：

首先，需要从`typing`模块导入`Optional`：

```python
from typing import Optional
```

然后，你可以在类型注解中使用它：

```python
def find_item(lst: list, value: int) -> Optional[int]:
    """查找列表中指定值的索引，如果找不到则返回None"""
    for index, element in enumerate(lst):
        if element == value:
            return index
    return None
```

在这个例子中，`find_item`函数的返回类型被标记为`Optional[int]`，这意味着它可能返回一个整数（找到了指定值的索引），也可能返回`None`（如果没有找到该值）。

此外，如果你使用的是Python 3.10或更高版本，还可以直接使用类型联合（Union）来达到类似的效果，因为`Optional[T]`本质上等同于`Union[T, NoneType]`：

```python
def find_item_v2(lst: list[int], value: int) -> int | None:  # 使用Python 3.10的类型联合语法
    for index, element in enumerate(lst):
        if element == value:
            return index
    return None
```

两种方式都表达了同样的类型信息，但后者在语法上更加简洁直观，特别是对于熟悉Python较新版本特性的开发者来说。