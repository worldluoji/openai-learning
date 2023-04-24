#coding:utf-8
import matplotlib.pyplot as plt

#解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示方块
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# 数据准备
nums = [12,12,12,12,12,35,5]
labels = ['科创50指数','纳斯达克指数','德国30指数','恒生指数','沪深300指数','债券基金','黄金']

# 用Matplotlib画饼图
plt.pie(x = nums, labels=labels, autopct="%1.2f%%")
plt.title("一种指数基金理财配置方案示例")
plt.show()
