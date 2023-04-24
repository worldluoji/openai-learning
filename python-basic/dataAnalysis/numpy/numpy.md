# numpy
1. 为什么要用 numpy 数组结构而不是 Python 本身的列表 list？
这是因为列表 list 的元素在系统内存中是分散存储的，而 NumPy 数组存储在一个均匀连续的内存块中。
这样数组计算遍历所有的元素，不像列表 list 还需要对内存地址进行查找，从而节省了计算资源。

2. 一个重要的规则就是：避免采用隐式拷贝，而是采用就地操作的方式。
举个例子，如果我想让一个数值 x 是原来的两倍，可以直接写成 x*=2，而不要写成 y=x*2
这样速度能快到 2 倍甚至更多。

3. 在 numpy 里有两个重要的对象
ndarray（N-dimensional array object）解决了多维数组问题
ufunc（universal function object）解决对数组进行处理的函数