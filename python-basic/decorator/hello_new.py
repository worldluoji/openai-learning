from functools import wraps
def hello(fn):
    @wraps(fn)
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)
    return wrapper
 
@hello
def foo():
    '''foo help doc'''
    print("i am foo")
    pass
 
foo()
print(foo.__name__)
print(foo.__doc__ )