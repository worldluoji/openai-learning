def count_to(n):
    for i in range(1, n+1):
        yield i

gen = count_to(5)

for num in gen:
    print(num)