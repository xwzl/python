# Python 提供了“%”对各种类型的数据进行格式化输出
price = 108
print("the book's price is %s" % price)

# 上面程序中的 print 函数包含以下三个部分，第一部分是格式化字符串（相当于字符串模板），该格式化字符串中包含一个“%s”占位符，它会被第三部分
# 的变量或表达式的值代替；第二部分固定使用“%”作为分隔符
#
# 格式化字符串中的“%s”被称为转换说明符（Conversion Specifier），其作用相当于一个占位符，它会被后面的变量或表达式的值代替。“%s”指定将变量或
# 值使用 str() 函数转换为字符串。
#
# 如果格式化字符串中包含多个“%s”占位符，第三部分也应该对应地提供多个变量，并且使用圆括号将这些变量括起来。
user = "Jack"
age = 8
# 格式化字符串有两个占位符，第三部分提供2个变量
print("%s is a %s years old boy" % (user, age))

# 有点不习惯多个字符变量的替换
macBook = "MackBook Pro"
price = 19_999
print("The apple of %s is %s 元 " % (macBook, price))

# python 提供的转换符说明
# 转换说明符	        说明
# %d，%i	转换为带符号的十进制形式的整数
# %o	    转换为带符号的八进制形式的整数
# %x，%X	转换为带符号的十六进制形式的整数
# %e	    转化为科学计数法表示的浮点数（e 小写）
# %E	    转化为科学计数法表示的浮点数（E 大写）
# %f，%F	转化为十进制形式的浮点数
# %g	    智能选择使用 %f 或 %e 格式
# %G	    智能选择使用 %F 或 %E 格式
# %c	    格式化字符及其 ASCII 码
# %r	    使用 repr() 将变量或表达式转换为字符串
# %s	    使用 str() 将变量或表达式转换为字符串

# 当使用上面的转换说明符时，可指定转换后的最小宽度
num = -28
print("num is: %6i" % num)
print("num is: %6d" % num)
print("num is: %6o" % num)
print("num is: %6x" % num)
print("num is: %6X" % num)
print("num is: %6s" % num)

# 在默认情况下，转换出来的字符串总是右对齐的，不够宽度时左边补充空格。Python 也允许在最小宽度之前添加一个标志来改变这种行为，Python 支持如下标志：
# -：指定左对齐。
# +：表示数值总要带着符号（正数带“+”，负数带“-”）。
# 0：表示不补充空格，而是补充 0#

# 提示：这三个标志可以同时存在。
num2 = 30
# 最小宽度为0，左边补0
print("num2 is: %06d" % num2)
# 最小宽度为6，左边补0，总带上符号
print("num2 is: %+06d" % num2)
# 最小宽度为6，右对齐
print("num2 is: %-6d" % num2)

# 对于转换浮点数，Python 还允许指定小数点后的数字位数：如果转换的是字符串，Python 允许指定转换后的字符串的最大字符数。这个标志被称为精度值，该精度
# 值被放在最小宽度之后，中间用点 ( . ) 隔开。

my_value = 3.001415926535
# 最小宽度为8，小数点后保留3位
print("my_value is: %8.3f" % my_value)
# 最小宽度为8，小数点后保留3位，左边补0
print("my_value is: %08.3f" % my_value)
# 最小宽度为8，小数点后保留3位，左边补0，始终带符号
print("my_value is: %+08.3f" % my_value)
the_name = "Charlie"
# 只保留3个字符
print("the name is: %.3s" % the_name)  # 输出Cha
# 只保留2个字符，最小宽度10
print("the name is: %10.2s" % the_name)

value = "欢迎来到字符格式测试"

print("设置十个宽度，限制四个字符串:%10.4s" % value)
