# 我们知道，计算机其实是不认识十进制数，它只认识二进制数，也就是说，当我们以十进制数进行运算的时候，计算机需要将各个十进制数转换成二进制数，然后进行二进制间的计算。
#
# 以类似 0.1 这样的浮点数为例，如果手动将其转换成二进制，其结果为：
#
#   0.1(10)=0.00011001100110011...(2)
#
# 可以看到，结果是无限循环的，也就是说，0.1 转换成二进制数后，无法精确到等于十进制数的 0.1。同时，由于计算机存储的位数是有限制的，所以如果要存储的二进制位数超过了计
# 算机存储位数的最大值，其后续位数会被舍弃（舍弃的原则是“0 舍 1 入”）。

# 这种问题不仅在 Python 中存在，在所有支持浮点数运算的编程语言中都会遇到，它不光是 Python 的 Bug。
#
# 明白了问题产生的原因之后，那么该如何解决呢？就 Python 的浮点数运算而言，大多数计算机每次计算误差不会超过 253，这对于大多数任务来说已经足够了。
#
# 如果需要非常精确的结果，可以使用 decimal 模块（其实就是别人开发好的程序，我们可以直接拿来用），它实现的十进制数运算适合会计方面的应用和有高精度要求的应用。
import decimal

x = decimal.Decimal("0.1")
y = decimal.Decimal("0.2")
print(x + y)
