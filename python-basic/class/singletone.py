'''
一般我们不会去重写该方法，除非你确切知道怎么做，什么时候你会去关心它呢，它作为构造函数用于创建对象，是一个工厂函数，专用于生产实例对象。
著名的设计模式之一，单例模式，就可以通过此方法来实现
'''
class BaseController:
    _singleton = None
    def __new__(cls, *a, **k):
        if not cls._singleton:
            cls._singleton = super().__new__(cls)
        return cls._singleton

b1 = BaseController()
b2 = BaseController()

print(b1)
print(b1 == b2)