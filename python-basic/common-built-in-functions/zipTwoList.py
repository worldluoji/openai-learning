def zipTwoList(l1, l2):
    return list(zip(l1, l2))

def unzipTwoList(l):
    return zip(*l)

a = [1, 2, 3]
b = [4, 5, 6]
l = zipTwoList(a, b)
c, d = unzipTwoList(l)
print(l)
print(c, a == c, a == list(c))
print(d, b == d, b == list(d))