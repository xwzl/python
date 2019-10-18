# 前面章节介绍了如何使用 % 操作符对各种类型的数据进行格式化输出，这是早期 Python 提供的方法。自 Python 2.6 版本开始，字符串类型（str）提供了 format() 方法对字符串进行格式化，本节就来学习此方法。
#
# format() 方法的语法格式如下：
# str.format(args)
#
# 此方法中，str 用于指定字符串的显示样式；args 用于指定要进行格式转换的项，如果有多项，之间有逗号进行分割。
#
# 此方法中，str 用于指定字符串的显示样式；args 用于指定要进行格式转换的项，如果有多项，之间有逗号进行分割。
#
# 学习 format() 方法的难点，在于搞清楚 str 显示样式的书写格式。在创建显示样式模板时，需要使用{}和：来指定占位符，其完整的语法格式为：
#
#   { [index][ : [ [fill] align] [sign] [#] [width] [.precision] [type] ] }
#
# 注意，格式中用 [] 括起来的参数都是可选参数，即可以使用，也可以不使用。各个参数的含义如下：
#
#   index：指定：后边设置的格式要作用到 args 中第几个数据，数据的索引值从 0 开始。如果省略此选项，则会根据 args 中数据的先后顺序自动分配。
#   fill：指定空白处填充的字符。注意，当填充字符为逗号(,)且作用于整数或浮点数时，该整数（或浮点数）会以逗号分隔的形式输出，例如（1000000会输出 1,000,000）。
#   align：指定数据的对齐方式，具体的对齐方式如表 1 所示。
#
#   align	    含义
#    <	    数据左对齐。
#    >	    数据右对齐。
#    =	    数据右对齐，同时将符号放置在填充内容的最左侧，该选项只对数字类型有效。
#    ^	    数据居中，此选项需和 width 参数一起使用。
#
# sign：指定有无符号数，此参数的值以及对应的含义
#
#    sign参数	    含义
#       +	    正数前加正号，负数前加负号。
#       -	    正数前不加正号，负数前加负号。
#      空格	    正数前加空格，负数前加负号。
#       #	    对于二进制数、八进制数和十六进制数，使用此参数，各进制数前会分别显示 0b、0o、0x前缀；反之则不显示前缀。
#
# width：指定输出数据时所占的宽度。
# .precision：指定保留的小数位数。
#
#   type：指定输出数据的具体类型
#
#   type类型值	        含义
#       s	        对字符串类型格式化。
#       d	        十进制整数。
#       c	        将十进制整数自动转换成对应的 Unicode 字符。
#       e 或者 E 	转换成科学计数法后，再格式化输出。
#       g 或 G	    自动在 e 和 f（或 E 和 F）中切换。
#       b	        将十进制数自动转换成二进制表示，再格式化输出。
#       o	        将十进制数自动转换成八进制表示，再格式化输出。
#       x 或者 X	将十进制数自动转换成十六进制表示，再格式化输出。
#       f 或者 F	转换为浮点数（默认小数点后保留 6 位），再格式化输出。
#       %	        显示百分比（默认显示小数点后 6 位）。
from builtins import str

strValue = "网站名称：{:>9s}\t网址：{:s}"
print(strValue.format("C语言中文网", "c.biancheng.net"))

hello = "hello  {1:s}"

print(str.format(hello, "111", "222"))

# 在实际开发中，数值类型有多种显示需求，比如货币形式、百分比形式等，使用 format() 方法可以将数值格式化为不同的形式。
# 以货币形式显示
print("货币形式：{:,d}".format(1000000))
# 科学计数法表示
print("科学计数法：{:E}".format(1200.12))
# 以十六进制表示
print("100的十六进制：{:#x}".format(100))
# 输出百分比形式
print("0.01的百分比表示：{:.0%}".format(0.01))

# 不指定位置
print("不指定位置:{}{}".format("hello", "world"))
# 指定位置
print("指定位置:{0}{1}".format("hello", "world"))
# 参数可通用
print("可复用参数位置：{1}{0}{1}".format("o", "s").title())

print("设置参数")
# 设置参数
print("网站名：{name},地址 {url}".format(name="个人博客", url="xuweizhi.gitee.io"))

# 通过字典设置参数
site = {
    "name": "徐伟智",
    "url": "www.github.com"
}

# 必须通过指针的形式吗？
print("网站名：{name},地址 {url}".format(**site))

# 通过列表索引设置参数,索引位置必须设置值
print("list1= index1:{0[0]},index2={0[1]} \nlist2= index1:{1[0]},{1[1]}"
      .format([1, 2], ["hello", "value"]))


# 通过对象赋值
class AssignValue(object):
    def __init__(self, value):
        self.value = value


# 0 是必须的嘛？
my_value = AssignValue("value")
print("AssignValue's value is {0.value} and {0.value}?".format(my_value))

# 数字格式化保留小数点后两位
print("{:.2f}".format(3.14159))

# 带符号保留小数点后两位
print("{:+.2f}".format(12.25))
print("{:+.2f}".format(-12.25))

# 不带小数
print("{:.0f}".format(12.25))
# 数字补零 (填充左边, 宽度为2)
print("{:0>3}".format(2))
# 数字补x (填充右边, 宽度为4)
print("{:x<4}".format(2))
# 以逗号分隔的数字格式
print("{:,}".format(100000000))
print("{:.2%}".format(25))
print("{:.2e}".format(10000))
# 右对齐 (默认, 宽度为10)
print("{:>10d}".format(10))
# 左对齐 (宽度为10)
print("{:<10d}".format(10))
# 中间对齐 (宽度为10)
print("{:^10d}".format(10))

print('{:b}'.format(11))
print('{:d}'.format(11))
print('{:o}'.format(11))
print('{:x}'.format(11))
print('{:#x}'.format(11))
print('{:#X}'.format(11))
# ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
#
# + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
#
# b、d、o、x 分别是二进制、十进制、八进制、十六进制。
#
# 此外我们可以使用大括号 {} 来转义大括号
print("{} 对应的位置是 {{0}}".format("runoob"))
