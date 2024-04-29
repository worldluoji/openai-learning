
class MyIterator:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 5:
            raise StopIteration
        self.count += 1
        return self.count

for num in MyIterator():
    print(num)