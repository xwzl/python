# count 方法用于检索指定字符串在另一字符串中出现的次数，如果检索的字符串不存在，则返回 0，否则返回出现的次数。
#
# count 方法的语法格式如下：
#
#   str.count(sub[,start[,end]])
#
# 此方法中，各参数的具体含义如下：
#
#   str：表示原字符串；
#   sub：表示要检索的字符串；
#   start：指定检索的起始位置，也就是从什么位置开始检测。如果不指定，默认从头开始检索；
#   end：指定检索的终止位置，如果不指定，则表示一直检索到结尾。
hello = "hello world"
print(hello.count("e"))

jack = "How are you ? I am fine !"
print(jack.count("o"))
print(jack.count("o", 0, 2))  # 开始到结束
print(jack.count("o", 3, 10))
