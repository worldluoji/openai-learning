
list_records = [
 ('Financial', '张三', 6000),
 ('IT', '丁一', 8000),
 ('Marketing', '李四', 8000),
 ('IT', '王二', 7000)
]

# 先基于department排序，然后再在部门内按照salary排序, reverse=True表示降序排列
list_records.sort(
 key = lambda l: (l[0], l[2]),
 reverse=True
)

print(list_records)
print('*' * 20)


dictionary_age = {
   '张三': 30,
   '丁一': 35,
   '李四': 18,
   '王二': 25,
}

# 先基于department排序, 再基于dictionary_age按照年龄排
list_records.sort(
 key = lambda l:( l[0], dictionary_age[l[1]] )
)

print(list_records)