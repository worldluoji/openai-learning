import numpy as np

x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print(x1)
print(x2)
print('*' * 13)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))

#在取余函数里，你既可以用 np.remainder(x1, x2)，也可以用 np.mod(x1, x2)，结果是一样的。