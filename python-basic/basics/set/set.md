# set
Python中的`set`类型是一种无序且不包含重复元素的集合数据结构。它通过使用花括号`{}`或调用内置的`set()`函数来创建。以下是标识和使用Python `set`类型的一些基本方式：

### 创建set

1. **使用花括号 `{}` 创建**：
   ```python
   # 直接列出元素，注意元素间用逗号分隔，且set中元素不可重复
   my_set = {1, 2, 3}
   ```

   注意：如果尝试用花括号创建一个空集合，这将被解释为字典的定义，因此应该避免这种做法。

2. **使用 `set()` 函数创建**：
   ```python
   # 从一个可迭代对象（如列表、元组）创建set
   my_set_from_list = set([1, 2, 2, 3, 4])  # 结果中自动去除重复项
   ```

   创建空集合时，必须使用 `set()` 函数，因为 `{}` 会被解析为空字典：
   ```python
   empty_set = set()
   ```

### 基本操作

- **添加元素**：使用 `add()` 方法向集合中添加单个元素。
  ```python
  my_set.add(5)
  ```

- **删除元素**：使用 `remove()` 方法删除指定元素，如果元素不存在会抛出异常；或者使用 `discard()` 方法，该方法在元素不存在时不抛出异常。
  ```python
  my_set.remove(2)  # 若2不存在则抛出KeyError
  my_set.discard(2)  # 若2不存在也不报错
  ```

- **集合运算**：支持集合间的交集(`intersection`)、并集(`union`)、差集(`difference`)和对称差集(`symmetric_difference`)等操作。
  ```python
  set_a = {1, 2, 3}
  set_b = {3, 4, 5}

  intersection = set_a.intersection(set_b)          # 交集
  union = set_a.union(set_b)                        # 并集
  difference_ab = set_a.difference(set_b)           # A与B的差集，即属于A但不属于B的元素
  symmetric_difference = set_a.symmetric_difference(set_b)  # 对称差集
  ```

- **成员测试**：使用 `in` 关键字检查元素是否在集合中。
  ```python
  if 3 in my_set:
      print("3 is in the set")
  ```

- **长度**：使用 `len()` 函数获取集合中元素的数量。
  ```python
  print(len(my_set))
  ```

### 特点回顾
- **无序性**：集合中的元素没有特定的顺序，不能通过索引访问。
- **唯一性**：集合中的每个元素都是唯一的，自动去除重复项。
- **可迭代**：尽管没有顺序，集合仍然是可迭代的，可以用于循环遍历。

这些特性使得`set`类型非常适合用于去重、集合运算以及检查成员资格等场景。

<br>

## 注意
```
>>> s.add([1,2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

>>> s.add({1,2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
```
list和set都是不能被hash的，因此加不到set里

由于Python的列表（list）是可变的，它们不是哈希able的，这意味着你不能直接对列表使用内置的`hash()`函数。但是，如果你确实需要获得一个列表内容的哈希值，你可以通过将列表转换为一个可哈希的数据结构，比如元组（tuple）或者将列表的内容连接成一个字符串，然后再求哈希值。

### 转换为元组求哈希

将列表转换为元组，因为元组是不可变的，所以可以被哈希：

```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
hash_value = hash(my_tuple)
print(hash_value)
```

### 列表内容连接成字符串求哈希

将列表的每个元素转换为字符串，并连接起来形成一个单独的字符串，然后求这个字符串的哈希值：

```python
my_list = ['a', 'b', 'c']
str_concatenated = ''.join(map(str, my_list))  # 将列表所有元素转换为字符串并连接
hash_value = hash(str_concatenated)
print(hash_value)
```

或者，如果你想保持元素之间的区分度且列表中包含非字符串类型，可以使用其他分隔符：

```python
my_list = [1, 2, 3]
str_with_separator = '|'.join(map(str, my_list))  # 使用分隔符连接
hash_value = hash(str_with_separator)
print(hash_value)
```

### 注意事项

- 上述方法中，列表的内容或顺序改变会导致最终的哈希值不同。
- 如果列表非常大或包含大量复杂对象，转换和哈希的过程可能会消耗较多资源。
- 当列表中包含不可哈希类型的元素（如列表、字典）时，上述方法同样不适用，需要进一步转换或处理这些元素。