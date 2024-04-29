# exceptions
Python 3 中有许多内建的异常类型，它们对应于各种编程错误和异常情况。以下列举了一些常见的异常类型：

1. **`BaseException`**：所有异常的基类。

2. **`Exception`**：大多数标准异常的基类，直接继承自 `BaseException`。通常捕获的异常都是 `Exception` 的子类。

3. **`KeyboardInterrupt`**：用户按下 Ctrl+C 或类似组合键触发的中断信号。

4. **`GeneratorExit`**：当 `generator.close()` 方法被调用或生成器的迭代器被垃圾回收时引发。

5. **`StopIteration`**：迭代器耗尽时引发，通常由 `for` 循环自动处理。

6. **`ArithmeticError`**：算术运算相关的错误的基类。

   - **`OverflowError`**：数值运算超出有效范围。
   - **`ZeroDivisionError`**：除数为零。

7. **`LookupError`**：索引或键查找失败的基类。

   - **`IndexError`**：序列索引超出范围。
   - **`KeyError`**：字典中查找不存在的键。

8.  **`AttributeError`**：尝试访问不存在的对象属性或方法时引发。

9.  **`TypeError`**：不同类型的操作或函数参数不匹配时引发。

10. **`ValueError`**：合法操作但传入了无效值时引发。

11. **`RuntimeError`**：一般性的运行时错误，用于表示其他异常类型不足以描述的错误。

12. **`NotImplementedError`**：某个方法或函数尚未实现时引发。

13. **`OSError`**：操作系统相关错误的基类，涵盖 I/O 错误、文件权限问题、资源不足等。

14. **`FileNotFoundError`**：试图打开不存在的文件时引发，它是 `OSError` 的子类。

15. **`RecursionError`**：递归深度超过限制时引发。

16. **`FloatingPointError`**：浮点数计算中发生的不可恢复错误，如溢出、下溢或被零除。

17. **`BufferError`**：与缓冲区操作相关的错误。

这些只是 Python 内建异常的一部分，实际上还有其他特定场景下可能遇到的异常。在编写代码时，可以根据需要捕获并处理这些异常，以确保程序具有良好的错误处理机制和健壮性。
如果不确定某个操作可能引发何种异常，可以查阅相关模块或函数的官方文档以获取更准确的信息。

<br>

## ValueError
`ValueError` 是 Python 中的一个内置异常类型，它属于 `Exception` 类的子类。`ValueError` 通常在以下几种情况下被引发：

1. **给定的值不适合其预期用途**：
   当一个函数、方法或操作接收到一个在逻辑上有效的值，但该值不符合其特定要求或上下文中的期望时，就会抛出 `ValueError`。例如，如果一个函数要求接收一个正整数作为参数，而传入了一个负数或非整数值，那么就可能会触发 `ValueError`。

2. **格式错误或数据类型不匹配**：
   在对字符串、列表、元组等数据结构进行解析或格式化时，如果提供的数据格式不正确，或者不符合特定的格式规范，也可能导致 `ValueError`。例如，尝试将一个非日期字符串解析成日期对象，或者向一个期望固定长度的列表中添加过多或过少的元素。

3. **数学或数值计算中的不合理值**：
   在进行数学计算、统计分析或其他涉及数值处理的场合，如果提供的数值虽然合法，但不符合算法或模型的要求，可能会触发 `ValueError`。例如，计算平均数时传入了一个包含负数的非负数列表，或者在对数据进行标准化时遇到了非正态分布的数据。

4. **参数验证失败**：
   在函数或方法内部进行参数验证时，如果发现某个参数的值不符合预设的约束条件，如范围检查、特定模式匹配等，也会抛出 `ValueError`。这通常发生在库函数或框架中，用来确保传入的参数符合预期，防止程序因无效输入而出现意外行为。

示例代码：

```python
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return number ** 0.5

try:
    result = calculate_square_root(-9)
except ValueError as e:
    print(f"An error occurred: {e}")
```

在这个例子中，当尝试计算负数的平方根时，函数会主动引发 `ValueError` 并附带一条说明消息。外部代码通过 `try-except` 块捕获这个异常，并打印出相应的错误信息。

总之，`ValueError` 是用来指示程序接收到的值在逻辑上是有效的，但不符合特定上下文的期望或要求。通过妥善地捕获和处理 `ValueError`，程序员可以确保程序在遇到这类问题时能够给出有意义的反馈，而不是崩溃或产生难以理解的结果。


## StopIteration
在 Python 中，迭代器是一种对象，实现了 `__iter__` 和 `__next__` 方法。`__iter__`方法返回迭代器自身（通常是 self），
而 `__next__ `方法在每次调用时返回下一个元素。当没有更多元素时，`__next__` 方法应抛出 StopIteration 异常。

[demo](./it.py)


<br>

## GeneratorExit
生成器是 Python 中一种特殊的迭代器，由包含 `yield` 表达式的函数定义。生成器函数在被调用时不执行任何代码，而是返回一个生成器对象。当对这个生成器对象进行迭代或调用其 `__next__` 方法时，函数体才会开始执行，直到遇到 `yield` 表达式暂停并返回值。下一次迭代时，从上次暂停的地方继续执行。

以下是生成器的一个简单示例：

```python
def count_to(n):
    for i in range(1, n+1):
        yield i

gen = count_to(5)

for num in gen:
    print(num)
```

`GeneratorExit` 是 Python 中的一个特殊异常类型，它用于通知生成器（generator）其生命周期即将结束，通常发生在以下几种情况：

1. **`generator.close()` 方法被调用**：当程序明确要求关闭一个生成器时，可以调用其 `close()` 方法。这会导致 Python 解释器向生成器发送一个 `GeneratorExit` 异常。生成器内部应当捕获并处理这个异常，执行任何必要的清理操作，然后退出。

   ```python
   gen = (i for i in range(10))
   gen.close()  # 调用 close() 触发 GeneratorExit
   ```

2. **生成器对象被垃圾回收**：如果一个生成器对象不再被引用，它可能会在某个时间点被垃圾回收。在回收过程中，Python 也会向生成器发送 `GeneratorExit` 异常，以确保即使在没有显式关闭的情况下，生成器也能有机会清理资源。


下面是一个简单的示例，展示了如何在生成器中处理 `GeneratorExit`：

```python
def my_generator():
    try:
        while True:
            yield 1
    except GeneratorExit:
        print("Generator is being closed.")
        # 执行清理工作，如关闭文件、释放锁等
        return  # 或 raise StopIteration

gen = my_generator()
next(gen)  # 使用生成器
gen.close()  # 触发 GeneratorExit，打印消息并清理
```

总结来说，`GeneratorExit` 是用来通知生成器其生命周期即将结束的一种异常类型，主要在生成器被显式关闭或即将被垃圾回收时出现。
生成器应当妥善处理此异常以确保资源得到恰当的清理。