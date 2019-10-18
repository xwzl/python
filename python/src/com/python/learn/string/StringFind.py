# find() 方法用于检索字符串中是否包含目标字符串，如果包含，则返回第一次出现该字符串的索引；反之，则返回 -1。
#
# find() 方法的语法格式如下：
# str.find(sub[,start[,end]])
#
# 此格式中各参数的含义如下：
#
#   str：表示原字符串；
#   sub：表示要检索的目标字符串；
#   start：表示开始检索的起始位置。如果不指定，则默认从头开始检索；
#   end：表示结束检索的结束位置。如果不指定，则默认一直检索到结尾。
#
# 用 find() 方法检索字符串中中首次出现 “.” 的位置索引

mapValue = {
    "name": "jack",
    "table": 1
}

print("name" in mapValue)

findStr = "hello world"
print(findStr.find("e"))
print(findStr.find("o", 2))
print(findStr.find("o", 5))
print(findStr.count("o", 5))

# 注意，Python 还提供了 rfind() 方法，与 find() 方法最大的不同在于，rfind() 是从字符串右边开始检索
print(findStr.rfind("l", 5, 10))

# 同 find() 方法类似，index() 方法也可以用于检索是否包含指定的字符串，不同之处在于，当指定的字符串不存在时，index() 方法会抛出异常。
#
# index() 方法的语法格式如下：
#
#   str.index(sub[,start[,end]])
#
# 此格式中各参数的含义分别是：
#
#   str：表示原字符串；
#   sub：表示要检索的子字符串；
#   start：表示检索开始的起始位置，如果不指定，默认从头开始检索；
#   end：表示检索的结束位置，如果不指定，默认一直检索到结尾。

print(findStr.index("h"))
# print(findStr.index("p"))  # 找不到报错
# 同 find() 和 rfind() 一样，字符串变量还具有 rIndex() 方法，其作用和 index() 方法类似，不同之处在于它是从右边开始检索

# Python str 提供了 3 种可用来进行文本对齐的方法，分别是 lJust()、rJust() 和 center() 方法，本节就来一一介绍它们的用法。
#
# Python lJust()方法
#
# lJust() 方法的功能是向指定字符串的右侧填充指定字符，从而达到左对齐文本的目的。
#
# lJust() 方法的基本格式如下：
#
#   S.lJust(width[, fillChar])
#
# 其中各个参数的含义如下：
#
#   S：表示要进行填充的字符串；
#   width：表示包括 S 本身长度在内，字符串要占的总长度；
#   fillChar：作为可选参数，用来指定填充字符串时所用的字符，默认情况使用空格。
S = 'http://c.biancheng.net/python/'
addr = 'http://c.biancheng.net'
print(S.ljust(35))
print(addr.ljust(35))

# 注意，该输出结果中除了明显可见的网址字符串外，其后还有空格字符存在，每行一共 35 个字符长度。
print(S.ljust(35, "-"))
print(addr.ljust(35, "-"))

# Python rjust()方法
#
# rjust() 和 ljust() 方法类似，唯一的不同在于，rjust() 方法是向字符串的左侧填充指定字符，从而达到右对齐文本的目的。
#
# rjust() 方法的基本格式如下：
#
#   S.rjust(width[, fillchar])
#
# 其中各个参数的含义和 ljust() 完全相同，所以这里不再重复描述。
rightValue = "hello value"
print(rightValue.rjust(25))

# Python center()方法
#
# center() 字符串方法与 ljust() 和 rjust() 的用法类似，但它让文本居中，而不是左对齐或右对齐。
#
# center() 方法的基本格式如下：
#
#   S.center(width[, fillchar])
#
# 其中各个参数的含义和 ljust()、rjust() 方法相同。
S = 'http://c.biancheng.net/python/'
addr = 'http://c.biancheng.net'
print(S.center(35, ))
print(addr.center(35, "-"))

valuePrefix = "hello world"
valueSuffix = "hello world"

# 除了前面介绍的几个方法外，Python 字符串变量还可以使用 startswith() 和endswith() 方法。
#
# startswith()方法
#
# startswith() 方法用于检索字符串是否以指定字符串开头，如果是返回 True；反之返回 False。此方法的语法格式如下：
#
#   str.startswith(sub[,start[,end]])
#
# 此格式中各个参数的具体含义如下：
#
#   str：表示原字符串；
#   sub：要检索的子串；
#   start：指定检索开始的起始位置索引，如果不指定，则默认从头开始检索；
#   end：指定检索的结束位置索引，如果不指定，则默认一直检索在结束。
print(valuePrefix.startswith("world"))
print(valuePrefix.startswith("world1"))
# endswith()方法
#
# endswith() 方法用于检索字符串是否以指定字符串结尾，如果是则返回 True；反之则返回 False。该方法的语法格式如下：
#
#   str.endswith(sub[,start[,end]])
#
# 此格式中各参数的含义如下：
#
#   str：表示原字符串；
#   sub：表示要检索的字符串；
#   start：指定检索开始时的起始位置索引（字符串第一个字符对应的索引值为 0），如果不指定，默认从头开始检索。
#   end：指定检索的结束位置索引，如果不指定，默认一直检索到结束。
print(valueSuffix.endswith("world"))
print(valueSuffix.endswith("world1"))

