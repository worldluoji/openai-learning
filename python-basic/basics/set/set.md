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