
import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print('*' * 8 + '计算最大值与最小值' + '*' * 8 )
print(np.amin(a))
print(np.amin(a,0))
print(np.amin(a,1))
print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))

'''
amin(a,0) 是延着 axis=0 轴的最小值，axis=0 轴是把元素看成了[1,4,7], [2,5,8], [3,6,9]三个元素，所以最小值为[1,2,3]，
amin(a,1) 是延着 axis=1 轴的最小值，axis=1 轴是把元素看成了[1,2,3], [4,5,6], [7,8,9]三个元素，所以最小值为[1,4,7]。
同理 amax() 是计算数组中元素沿指定轴的最大值。
'''

print('*' * 8 + '计算最大值与最小值之差' + '*' * 8 )
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))

print('*' * 8 + '统计数组的百分位数' + '*' * 8 )
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))

'''
同样，percentile() 代表着第 p 个百分位数，这里 p 的取值范围是 0-100，
如果 p=0，那么就是求最小值，如果 p=50 就是求平均值，如果 p=100 就是求最大值。
同样你也可以求得在 axis=0 和 axis=1 两个轴上的 p% 的百分位数。
(9 - 1) * 50% + 1 = 5
'''

print('*' * 8 + '统计数组中的中位数' + '*' * 8 )
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
#求中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
#求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))


print('*' * 8 + '统计数组中的加权平均值' + '*' * 8 )
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print(np.average(a))
print(np.average(a,weights=wts))

print('*' * 8 + '方差、标准差' + '*' * 8 )
a = np.array([1,2,3,4])
print(np.std(a))
print(np.var(a))

print('*' * 8 + '排序' + '*' * 8 )
a = np.array([[4,3,2],[2,4,1]])
print(np.sort(a))
print('*' * 13)
print(np.sort(a, axis=None))
print('*' * 13)
print(np.sort(a, axis=0))
print('*' * 13)  
print(np.sort(a, axis=1))  