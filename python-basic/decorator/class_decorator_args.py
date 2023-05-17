class makeHtmlTagClass(object):
 
    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
                                       if css_class !="" else ""
 
    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class+">"  \
                       + fn(*args, **kwargs) + "</" + self._tag + ">"
        return wrapped


'''
1）如果 decorator 有参数的话，__init__() 成员就不能传入 fn 了，而 fn 是在 __call__ 的时候传入的。
2）这段代码还展示了 wrapped(*args, **kwargs) 这种方式来传递被 decorator 函数的参数
'''
@makeHtmlTagClass(tag="b", css_class="bold_css")
@makeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello, {}".format(name)
 
print(hello("Python3"))