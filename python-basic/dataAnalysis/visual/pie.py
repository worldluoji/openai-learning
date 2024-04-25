
import matplotlib.pyplot as plt

# 数据准备
nums = [25, 37, 33, 37, 6]
labels = ['High-school','Bachelor','Master','Ph.d', 'Others']

# 用Matplotlib画饼图, autopct='%1.1f%%' 是关键部分，它指定了每个扇区上方显示的百分比标签应保留一位小数，并以百分号（%）结尾。这里的 %1.1f 是格式化字符串，其中 1 表示保留的小数位数，f 表示浮点数。%% 在字符串中代表一个实际的百分号字符。
plt.pie(x = nums, labels=labels, autopct='%1.1f%%')
plt.show()