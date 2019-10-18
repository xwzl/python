# Python 中，为了方便对字符串中的字母进行大小写转换，字符串变量提供了 3 种方法，分别是 title()、lower() 和 upper()。
#
# Python title()方法
#
# title() 方法用于将字符串中每个单词的首字母转为大写，其他字母全部转为小写，转换完成后，此方法会返回转换得到的字符串。
# 如果字符串中没有需要被转换的字符，此方法会将字符串原封不动地返回。
#
# title() 方法的语法格式如下：
#
#   str.title()
#
# 其中，str 表示要进行转换的字符串。
value = "hOW ARE YOU"
print(value.title())  # 注意是每个单词首字母大写

javaReturn = "i am fine"
print("Java :", javaReturn.upper())
print(javaReturn.title())

# Python lower()方法
#
# lower() 方法用于将字符串中的所有大写字母转换为小写字母，转换完成后，该方法会返回新得到的字符串。如果字符串中原本就都是小写字母，则该方法会返回原字符串。
#
# lower() 方法的语法格式如下：
#
#   str.lower()
#
# 其中，str 表示要进行转换的字符串。
lower = "THIS IS UPPER SEQUENCE"
print(lower.lower())

#  需要注意的是，以上 3 个方法都仅限于将转换后的新字符串返回，而不会修改原字符串。
upper = "this is lower sequence"
print(upper.upper())
