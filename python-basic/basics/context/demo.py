
def record_generator(data_source):
    for record in data_source:
        yield record

class ManagedGenerator:
    def __init__(self, generator_func, *args, **kwargs):
        self.generator_func = generator_func
        self.args = args
        self.kwargs = kwargs
        self.generator = None

    def __enter__(self):
        self.generator = self.generator_func(*self.args, **self.kwargs)
        return self.generator

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.generator is not None:
            try:
                # 尝试关闭生成器，引发 GeneratorExit 异常
                next(self.generator)
            except StopIteration:
                pass  # 正常结束，无需处理
            except Exception as e:
                print(f"Error closing generator: {e}")
                return False  # 传播异常

data_source = [1, 2, 3, 4, 5]  # 假设这是一个实际的数据源

with ManagedGenerator(record_generator, data_source) as gen:
    for record in gen:
        print(record)


'''当 `with` 语句结束时，Python 自动调用 `ManagedGenerator` 类的 `__exit__()` 方法。由于生成器在 `__enter__()` 方法中被创建并返回给 `with` 语句块内使用，当 `with` 语句结束时，生成器已经完成了其预期任务（即迭代完所有数据源项）。此时，生成器自然处于终止状态，无需我们手动关闭。

在 Python 中，生成器的生命周期通常由以下几个阶段组成：

1. **创建**：通过调用一个包含 `yield` 语句的函数或表达式创建生成器对象。
2. **迭代**：通过 `for` 循环、`next()` 函数或其他方式逐次从生成器中获取值。
3. **终止**：当生成器内部没有更多的值可 `yield`（如 `for` 循环结束），或者显式抛出 `StopIteration` 异常时，生成器终止。

在您提供的代码示例中，`record_generator` 函数的生成器在遍历完 `data_source` 列表后会自然引发 `StopIteration` 异常，这标志着生成器的正常结束。`with` 语句结束后，生成器对象会被垃圾回收机制自动清理，无需我们额外进行任何关闭操作。

因此，`ManagedGenerator` 类的 `__exit__()` 方法中原本尝试关闭生成器的逻辑（即 `next(self.generator)`）不仅多余，还可能因为尝试访问已终止的生成器而产生异常。正确的做法是如前所述，简化 `__exit__()` 方法，允许生成器在 `with` 语句结束后自然终止:

class ManagedGenerator:
    def __init__(self, generator_func, *args, **kwargs):
        self.generator_func = generator_func
        self.args = args
        self.kwargs = kwargs
        self.generator = None

    def __enter__(self):
        self.generator = self.generator_func(*self.args, **self.kwargs)
        return self.generator

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # No explicit handling needed; let the generator naturally terminate
'''