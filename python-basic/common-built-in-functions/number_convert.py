dec = int(input("输入数字："))
 
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))

# 二进制转10进制
print(int('0b1010', 2))


class Solution:
    def grayCode(self, n: int):
        if n == 1:
            return [0, 1]

        res = ['0', '1']
        for i in range(1, n):
            left = list(map(lambda s: '0' + s, res))
            right = list(map(lambda s: '1' + s, res))
            right.reverse() # change right directly, the same as JavaScript
            left.extend(right) # change left directly, the same as left.push(...right) in JavaScript
            res = left
        
        return list(map(lambda s: int('0b' + s, 2), res))