# Python process str VS JavaScript

| 功能类别 | Python 3 方法 | 描述 | JavaScript 方法 | 描述 |
| --- | --- | --- | --- | --- |
| **大小写转换** | `title()` | 返回字符串的标题式样（首字母大写，其余小写）。 | `toLocaleUpperCase()` 或 `toUpperCase()` | 返回全大写的字符串。 |
|  | `upper()` | 返回全大写的字符串。 | `toLocaleLowerCase()` 或 `toLowerCase()` | 返回全小写的字符串。 |
|  | `lower()` | 返回全小写的字符串。 | 使用正则表达式和逻辑判断 | 实现类似 `swapcase()` 的功能。 |
|  | `swapcase()` | 返回字符串大小写交换后的结果。 |  |  |
| **字母数字检查** | `isalnum()` | 检查字符串是否只包含字母和数字，返回布尔值。 | 使用正则表达式 `test(/[A-Za-z0-9]/g)` | 检查字符串是否只包含字母和数字。 |
|  | `isalpha()` | 检查字符串是否只包含字母，返回布尔值。 | 使用正则表达式 `test(/[A-Za-z]/g)` | 检查字符串是否只包含字母。 |
|  | `isdigit()` | 检查字符串是否只包含数字，返回布尔值。 | 使用正则表达式 `test(/\d/g)` | 检查字符串是否只包含数字。 |
|  | `islower()` | 检查字符串是否全为小写，返回布尔值。 | `toLowerCase().localeCompare(toUpperCase()) === 0` | 检查字符串是否全为小写或全为大写。 |
|  | `isupper()` | 检查字符串是否全为大写，返回布尔值。 | `charAt(0).toUpperCase() === charAt(0)` 且 `toLowerCase() === this` | 检查字符串是否全为大写。 |
|  | `istitle()` | 检查字符串是否为标题式样（每个单词首字母大写，其余小写），返回布尔值。 |  |  |
| **查找和替换** | `find(sub[, start[, end]])` | 返回子字符串 `sub` 在原字符串中第一次出现的索引，不存在则返回 -1。 | `indexOf(substring[, start])` | 返回子字符串首次出现的索引，不存在则返回 -1。 |
|  | `rfind(sub[, start[, end]])` | 从右向左搜索。 | `lastIndexOf(substring[, start])` | 类似 `indexOf()`，从后向前搜索。 |
|  | `index(sub[, start[, end]])` | 类似 `find()`，但找不到时抛出异常。 | `includes(substring[, start])` | 检查字符串是否包含给定子字符串，返回布尔值。 |
|  | `rindex(sub[, start[, end]])` | 类似 `rfind()`，但找不到时抛出异常。 |  |  |
|  | `replace(old, new[, count])` | 替换字符串中所有（或指定次数）的 `old` 子串为 `new`。 | `replace(pattern, replacement)` | 替换字符串中匹配 `pattern` 的部分（可以是字符串或正则表达式）为 `replacement`。 |
| **分割与连接** | `split(sep=None, maxsplit=-1)` | 根据指定分隔符 `sep` 分割字符串，返回列表。可选参数 `maxsplit` 控制最大分割次数。 | `split(separator[, limit])` | 根据指定分隔符 `separator` 分割字符串，返回数组。可选参数 `limit` 控制最大分割次数。 |
|  | `rsplit(sep=None, maxsplit=-1)` | 类似 `split()`，从右向左分割。 |  |  |
|  | `join(iterable)` | 用字符串作为分隔符，将可迭代对象（如列表）中的元素合并成一个字符串。 | `join(separator)` | 用指定的分隔符将数组元素合并成一个字符串。 |
| **其他常用方法** | `strip([chars])` | 移除字符串两侧的空白字符（默认）或指定字符序列。 | `trim()` | 移除字符串两侧的空白字符。 |
|  | `lstrip([chars])` | 移除左侧空白字符（默认）或指定字符序列。 | `trimStart()` | 移除字符串左侧的空白字符。 |
|  | `rstrip([chars])` | 移除右侧空白字符（默认）或指定字符序列。 | `trimEnd()` | 移除字符串右侧的空白字符。 |

表格清晰地展示了 Python 3 和 JavaScript 字符串操作方法的功能、描述及对应关系，方便比较和查阅。

## 字符串反转
利用Python字符串的切片功能，可以非常简洁地实现倒转。
```
text = "Hello, World!"
reversed_text = text[::-1]
print(reversed_text)
```