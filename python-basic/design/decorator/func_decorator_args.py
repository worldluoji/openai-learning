# 1. 通过 **kwargs 注入
def decorate_A(function):
    def wrap_function(*args, **kwargs):
        kwargs['str'] = 'Hello!'
        return function(*args, **kwargs)
    return wrap_function
 
@decorate_A
def print_message_A(*args, **kwargs):
    print(kwargs['str'])
 
print_message_A()


# 2. 约定好参数
def decorate_B(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        return function(str, *args, **kwargs)
    return wrap_function
 
@decorate_B
def print_message_B(str, *args, **kwargs):
    print(str)
 
print_message_B()

# 3. 通过 *args 注入
def decorate_C(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        #args.insert(1, str)
        args = args +(str,)
        return function(*args, **kwargs)
    return wrap_function
 
class Printer:
    @decorate_C
    def print_message(self, str, *args, **kwargs):
        print(str)
 
p = Printer()
p.print_message()