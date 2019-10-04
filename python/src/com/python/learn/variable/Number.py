# 导入cmath 模块
import cmath

# python 是弱类型语言，变量名称可以被任意类型赋值
index = 10
# int 类型
print(type(index))
index = "赋值为字符串类型"
print(type(index))

# 定义变量a，赋值为56
a = 56
print(a)

# 为a赋值一个大整数，自动转换为高精度的类型
a = 9999999999999999999999
print(a)

# type()函数用于返回变量的类型
print(type(a))

# 以0x或0X开头的整型数值是十六进制形式的整数
hex_value1 = 0x13
hex_value2 = 0xaF
print("hexValue1 的值为：", hex_value1)
print("hexValue2 的值为：", hex_value2)

# 以0b或0B开头的整型数值是二进制形式的整数
bin_val = 0b111
print('bin_val的值为：', bin_val)
bin_val = 0B101
print('bin_val的值为：', bin_val)

# 以0o或0O开头的整型数值是八进制形式的整数
oct_val = 0o54
print('oct_val 的值为：', oct_val)
oct_val = 0O17
print('oct_val 的值为：', oct_val)

# 在数值中使用下画线
one_million = 1000000
print(one_million)
price = 234_234_234  # price 实际的值为234234234
android = 1234_1234  # android 实际的值为12341234

af1 = 3.14159
# 输出 af1 的值
print("af1 的值为：", af1)
af2 = 25.2345
print("af2的类型为：", type(af2))
f1 = 5.12e2
print("f1的值为：", f1)
# 虽然 5e3 的值是 5000，但它依然是浮点型值，而不是整型值，因为 Python 会自动将该数值变为 5000.0
f2 = 5e3
print("f2的值为：", f2)
print("f2的类型为：", type(f2))  # 看到类型为float

rf1 = 0.1
rf2 = 0.2
# 0.30000000000000004
print(abs(rf1 + rf2))

# 模块就是一个 Python 程序，Python 正是通过模块提高了自身的可扩展性的；Python 本身内置了大量模块，此外还有
# 大量第三方模块，导入这些模块即可直接使用这些程序中定义的函数。

ac1 = 3 + 0.2j
print(ac1)
print(type(ac1))  # 输出复数类型
ac2 = 4 - 0.1j
print(ac2)

# 复数运行
print(ac1 + ac2)  # 输出(7+0.1j)

# sqrt()是cmath 模块下的商数，用于计算平方根
ac3 = cmath.sqrt(-1)
print(ac3)  # 输出1j

