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