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

# for...else语句:当循环里的break没有被执行的时候，就会执行else
# 素数也叫质数，除了1和它本身以外，不能再被其他的任何数整除
# 求2到100的合数(1既不是质数，也不是合数;2是质数)
for i in range(2, 101):  # i=105
    for j in range(2, int(i ** 0.5) + 1):  # range(2,105)  从2取到104  2  3
        if i % j == 0:  # i 除以某一个数字，除尽了,i是合数
            # print(i, '是合数')
            break  # break放在内循环里，用来结束内循环
    else:
        # for...else语句:当循环里的break没有被执行的时候，就会执行else
        print(i, '是质数')

# 在字符串的前面添加 r 在Python里表示的是原生字符串
# 转义无效
x3 = r'hello \teacher'
print(x3)
