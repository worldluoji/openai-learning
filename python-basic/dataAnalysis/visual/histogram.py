
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 数据准备
a = np.random.randn(100)
print(a)
s = pd.Series(a)
print(s)

# 用Matplotlib画直方图
plt.hist(s)
plt.show()

'''
在 Matplotlib 中，我们使用 plt.hist(x, bins=10) 函数，
其中参数 x 是一维数组，bins 代表直方图中的箱子数量，默认是 10。
上面代码就表示，把数据x轴分成10个桶，y轴统计每个区间段的数量
'''

# 用Seaborn画直方图
sns.distplot(s, kde=False)
plt.show()
sns.distplot(s, kde=True)
plt.show()