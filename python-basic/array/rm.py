
l = [1,2,3,4]

l.remove(1)

print(l)
print(l.index(2))

try:
    print(l.index(1))
except ValueError as e:
    print("not found")
finally:
    print("always implement")


l = [1,1,2,2]
l.remove(1)
print(l)