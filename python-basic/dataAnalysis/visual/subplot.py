
import matplotlib.pyplot as plt
import seaborn as sns
# 保障中文正常显示
plt.rc('font',family='Heiti TC')
plt.title('2024年手机银行城市服务专区需求情况')

# 数据准备
x = ['已上线需求数','实施分析中需求数', '今年预期剩余需求数']
nums = [36, 5, 70]

colors = ['lightgreen', 'pink', 'lightgray']

fig, axes = plt.subplots(1, 2)

# 用Matplotlib画条形图
bars = axes[0].bar(x, nums, color=colors)
axes[0].bar_label(bars, label_type='center')
axes[1].pie(x = nums, labels=x, autopct='%1.1f%%', colors=colors)
plt.show()

# # 用Seaborn画条形图
# sns.barplot(x, y)
# plt.show()