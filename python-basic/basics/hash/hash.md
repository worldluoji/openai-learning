# hash
在Python中，求一个对象的哈希值可以使用内置的`hash()`函数。这个函数适用于大多数Python的基本数据类型和一些可哈希的对象，如字符串、整数、浮点数、元组等。
需要注意的是，像列表和字典这样的可变类型是不可哈希的，因此不能直接对它们调用`hash()`函数。

### 基本用法

对于基本数据类型，如字符串和整数，可以直接这样求哈希值：

```python
# 求字符串的哈希值
string = "Hello, World!"
hash_value = hash(string)
print(f"The hash value of the string is: {hash_value}")

# 求整数的哈希值
number = 12345
hash_number = hash(number)
print(f"The hash value of the number is: {hash_number}")
```

### 使用`hashlib`模块

对于更复杂的哈希需求，比如计算文件的MD5、SHA-1、SHA-256等哈希值，可以使用Python的`hashlib`模块。这里以计算字符串的MD5哈希为例：

```python
import hashlib

# 计算字符串的MD5哈希值
text = "Sample Text"
hasher = hashlib.md5()
hasher.update(text.encode('utf-8'))  # 需要将字符串编码为字节串
md5_hash = hasher.hexdigest()
print(f"The MD5 hash of the text is: {md5_hash}")
```

### 国密算法（如SM3）

对于特定场景，如果需要使用国密算法（如SM3），可以使用第三方库如`gmssl`。以下是一个使用`gmssl`计算SM3哈希值的示例：

```python
from gmssl import sm3

# 计算字符串的SM3哈希值
message = b"Sample Text"  # 注意这里直接使用字节串
sm3_hash = sm3.sm3_hash(message)
print(f"The SM3 hash of the message is: {sm3_hash.hex()}")
```

请注意，使用`gmssl`或其他第三方库之前，需要先通过pip安装相应的库。例如，安装`gmssl`可以使用命令`pip install gmssl`。

在实际应用中选择合适的哈希函数时，应考虑安全性、性能和具体应用场景的需求。