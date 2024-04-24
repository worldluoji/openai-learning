'''
如果可迭代元素中的所有元素都为真，则 all 函数返回 True，否则返回 False。
如果迭代器中至少有一个元素为 True，则 any 函数返回 True，否则返回 False。
'''

list1 = [True, True, False, True] 
print(all(list1))  
# False 

list2 = [False, True, False] 
print(any(list2))  
# True