# 用户输入数据时，很有可能会无意中输入多余的空格，或者在一些场景中，字符串前后不允许出现空格和特殊字符，此时就需要去除字符串中的空格和特殊字符。
#
# 这里的特殊字符，指的是制表符（\t）、回车符（\r）、换行符（\n）等。
#
# Python 中，字符串变量提供了 3 种方法来删除字符串中多余的空格和特殊字符，它们分别是：
#
#   strip()：删除字符串前后（左右两侧）的空格或特殊字符。
#   lstrip()：删除字符串前面（左边）的空格或特殊字符。
#   rstrip()：删除字符串后面（右边）的空格或特殊字符。
#
# 注意，Python 的 str 是不可变的（不可变的意思是指，字符串一旦形成，它所包含的字符序列就不能发生任何改变），因此这三个方法只是返回字符串前面或后
# 面空白被删除之后的副本，并不会改变字符串本身。
#
# Python strip()方法
#
# strip() 方法用于删除字符串左右两个的空格和特殊字符，该方法的语法格式为：
#
#   str.strip([chars])
#
# 其中，str 表示原字符串，[chars] 用来指定要删除的字符，可以同时指定多个，如果不手动指定，则默认会删除空格以及制表符、回车符、换行符等特殊字符。
hello = " this is trim"
print(hello.strip())
print(hello)
print(hello.strip(" "))

# Python rstrip()方法
#
# rstrip() 方法用于删除字符串右侧的空格和特殊字符，其语法格式为：
#
#   str.rstrip([chars])
#
# str 和 chars 参数的含义和前面 2 种方法语法格式中的参数完全相同。
#
# Python lstrip()方法
#
# lstrip() 方法用于去掉字符串左右的空格和特殊字符。该方法的语法格式如下：
#
#   str.lstrip([chars])
#
# 其中，str 和 chars 参数的含义，分别同 strip() 语法格式中的 str 和 chars 完全相同
str = "  c.biancheng.net \t\n\r"
print(str.rstrip())
