#coding:utf-8
import matplotlib.pyplot as plt

#解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示方块
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# 数据准备
nums = [40,60]
labels = ['股票指数基金','债券基金']

# 用Matplotlib画饼图
plt.pie(x = nums, labels=labels, autopct="%1.2f%%")
plt.title("4-6股债组合")
plt.show()
