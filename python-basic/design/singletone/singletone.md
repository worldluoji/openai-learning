# singletone
在Python中实现单例模式主要有以下几种常见方法：

### 1. **基于类的`__new__`方法**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# 使用示例
singleton_obj = Singleton()
another_singleton_obj = Singleton()

assert singleton_obj is another_singleton_obj  # 两个引用指向同一个实例
```

在这个例子中，我们重写了类的`__new__`方法。当试图创建类的新实例时，`__new__`会被调用。我们在这里检查是否已有实例存在（存储在类变量 `_instance` 中），如果有则直接返回该实例，否则才真正调用父类的 `__new__` 方法创建新实例并保存起来。

### 2. **基于模块**

由于Python模块在程序中只会被导入一次，且导入后会在内存中保留该模块的对象，因此可以利用这一特性实现单例：

```python
# singleton_module.py
class Singleton:
    pass

singleton_instance = Singleton()

# 主程序
from singleton_module import singleton_instance

first_reference = singleton_instance
second_reference = singleton_instance

assert first_reference is second_reference  # 两个引用指向同一个实例
```

这里，我们将单例类和其实例直接放在一个单独的模块文件中。每次导入该模块时，都会得到同一个`Singleton`类的实例。

### 3. **基于装饰器**

通过定义一个装饰器函数，将其应用于需要成为单例的类上：

```python
def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance

@singleton
class SingletonClass:
    pass

# 使用示例
obj1 = SingletonClass()
obj2 = SingletonClass()

assert obj1 is obj2  # 两个引用指向同一个实例
```

在这个例子中，装饰器`singleton`负责管理类的实例。每当尝试创建类的实例时，它首先检查内部字典`instances`中是否存在该类的实例，如果不存在则创建并保存；如果已存在，则直接返回已有的实例。

### 4. **基于元类（Metaclass）**

元类允许你定制类的创建过程，可以用来确保单例的实现：

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

# 使用示例
singleton_a = Singleton()
singleton_b = Singleton()

assert singleton_a is singleton_b  # 两个引用指向同一个实例
```

在这个实现中，我们定义了一个名为`SingletonMeta`的元类，它重写了`__call__`方法。当试图通过类来创建对象时，这个方法会被调用。元类中我们维护了一个字典 `_instances` 用于存储类的实例。当创建新实例时，我们先检查字典中是否已有该类的实例，如有则直接返回，否则创建新实例并保存到字典中。

以上就是Python中实现单例模式的四种常见方法。选择哪种方法取决于具体需求和个人偏好，但通常情况下，使用`__new__`方法或元类实现更为通用且易于理解。模块级别的单例适用于非常简单的场景，而装饰器方式则提供了简洁的使用语法。