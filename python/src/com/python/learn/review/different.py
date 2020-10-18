# python 里面区间可以连写
x = 31
if 10 < x < 30:
    print("python 中区间可以连写")

if x:
    print("python 类型都有隐私转换为 bool 值")

# 三元表达式
print(True if x > 30 else False)

# python 里面没有自增自减运算符
# x++
x += 1

# python 中 for 循环指的是 for ... in 循环
# for ele in iterable
# range 内置类用来生成指定区间的整数序列
# iterable：可迭代对象，字符串、元组、数组、列表、range、字典
for x1 in range(1, 3):
    print(x1)

array = [18, 16, 13, 14, 15, 156, 19]
i = 0

while i < 6:
    j = 0
    while j < 6 - i:
        if array[j] > array[j + 1]:
            array[j + 1] ^= array[j]
            array[j] ^= array[j + 1]
            array[j + 1] ^= array[j]
        j += 1
    i += 1
print(array)
