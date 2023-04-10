# The differences among pip pip3 pip3.7.md
Python3.7 安装后pip pip3 pip3.7的区别
在安装完Python3.7后，会在Python37\Scripts目录下发现有三个pip开头的exe，分别是：
1. pip
2. pip3
3. pip3.7

那么为什么会有三个呢？明明不是只有一个pip就可以吗？

原因是为了兼容。

比如Linux或Mac系统下本来已经预装了Python2.7的版本，后来我们自己又装了3.7的版本。

而因为系统其它组件或程序需要依赖2.7版本，并不希望我们把它给替换掉。

那么只能折衷做兼容处理，给它们加上后缀，以示区分：

如果同时装有 python2 和 python3

pip 默认给 python2 用。

pip3 指定给 python3 用。

如果同时安装多个3的版本的话，比如3.5 3.6 3.7。则用pip3明显不合适，这个时候就可以用pip+版本后缀来明确指出具体版本的pip了。

如果只装有 python3

则pip和pip3、pip3.7是等价的。