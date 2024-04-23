# decorator
## Decorator 的本质
对于 Python 的这个 @注解语法糖 - Syntactic Sugar 来说，当你在用某个 @decorator 来修饰某个函数 func 时，如下所示:
```
@decorator
def func():
    pass
```
其解释器会解释成下面这样的语句：
```
func = decorator(func)
```
decorator 必需得返回一个函数，这就是所谓的 higher order function 高阶函数。

知道这点本质，当你看到有多个 decorator 或是带参数的 decorator，你也就不会害怕了：
```
@decorator_one
@decorator_two
def func():
    pass
```
相当于
```
func = decorator_one(decorator_two(func))
```

带参数的 decorator：
```
@decorator(arg1, arg2)
def func():
    pass
```
相当于
```
func = decorator(arg1,arg2)(func)
```
被 decorator 的函数其实已经是另外一个函数了，
对于 hello.py 的例子来说，如果你查询一下 foo.__name__ 的话，你会发现其输出的是 “wrapper”，而不是我们期望的 “foo”,这会给我们的程序埋一些坑。
所以，Python 的 functool 包中提供了一个叫 wrap 的 decorator 来消除这样的副作用 -> hello_new.py