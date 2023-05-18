# class A(object): python2 必须显示地继承object
class A:
    # __init__方法可以用来做一些初始化工作，比如给实例对象的状态进行初始化
    def __init__(self):
        print("__init__ ", self)
        # python3 中 推荐使用 super()，代替之前的super(classname, cls）写法
        super().__init__() 

    def __new__(cls):
        print("__new__ ")
        self =  super().__new__(cls)
        print(self)
        # __new__ 方法的返回值就是类的实例对象，这个实例对象会传递给 __init__ 方法中定义的 self 参数，以便实例对象可以被正确地初始化。
        return self

    def __call__(self):  # 可以定义任意参数
        print('__call__ ')

#  __new__方法先被调用，返回一个实例对象，接着 __init__ 被调用
A()

'''
如果 __new__ 方法不返回值（或者说返回 None）那么 __init__ 将不会得到调用，这个也说得通，
因为实例对象都没创建出来，调用 init 也没什么意义。
此外，Python 还规定，__init__ 只能返回 None 值，否则报错。
'''