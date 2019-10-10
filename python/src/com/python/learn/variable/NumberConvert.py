# 虽然 Python 是弱类型编程语言，不需要像 Java 或 C 语言那样还要在使用变量前声明变量的类型，但在一些特定场景中，仍然需要用到类型转换。
#
# Python 中字符串后面不能直接添加数字，需要显示把浮点类型转换成字符串
price = 10.3
print("2019 年新款 iphone pro max 的价格：" + str(price))

# 庆幸的是，Python 已经为我们提供了多种可实现数据类型转换的函数
#    函 数	                       作 用
#   int(x)	                将 x 转换成整数类型
#   float(x)	            将 x 转换成浮点数类型
#   complex(real，[,imag])	创建一个复数
#   str(x)	                将 x 转换为字符串
#   repr(x)	                将 x 转换为表达式字符串
#   eval(str)	            计算在字符串中的有效 Python 表达式，并返回一个对象
#   chr(x)	                将整数 x 转换为一个字符
#   ord(x)	                将一个字符 x 转换为它对应的整数值
#   hex(x)	                将一个整数 x 转换为一个十六进制字符串
#   oct(x)	                将一个整数 x 转换为一个八进制的字符串
print(hex(100))
