# 字符串本质上就是由多个字符组成的，Python 允许通过索引来操作字符，比如获取指定索引处的字符，获取指定字符在字符串中的位置等。
#
# Python 字符串直接在方括号（[]）中使用索引即可获取对应的字符，其基本语法格式为：
# string[index]
#
# 这里的 string 表示要截取的字符串，index 表示索引值。Python 规定，字符串中第一个字符的索引为 0、第二个字符的索引为 1，后面各字符依此类推。此外，Python 也
# 允许从后面开始计算索引，最后一个字符的索引为 -1，倒数第二个字符的索引为 -2，依此类推。
value = "Hello Intercept"
print(value[1])
print(value[-1])

# 除可获取单个字符之外，Python 也可以在方括号中使用范围来获取字符串的中间“一段”（被称为子串），其基本语法格式为：
#
#   string[start : end : step]
#
# 此格式中，各参数的含义如下：
#
#   string：要截取的字符串；
#   start：表示要截取的第一个字符所在的索引（截取时包含该字符）。如果不指定，默认为 0，也就是从字符串的开头截取；
#   end：表示要截取的最后一个字符所在的索引（截取时不包含该字符）。如果不指定，默认为字符串的长度；
#   step：指的是从 start 索引处的字符开始，每 step 个距离获取一个字符，直至 end 索引出的字符。step 默认值为 1，当省略该值时，最后一个冒号也可以省略。
print(value[1:3])
print(value[1:15:2])

s = 'crazyIt.org is very good'
# 获取s中从索引3处到索引5处（不包含）的子串
print(s[3: 5])  # 输出 zy
# 获取s中从索引3处到倒数第5个字符的子串
print(s[3: -5])  # 输出 zyit.org is very
# 获取s中从倒数第6个字符到倒数第3个字符的子串
print(s[-6: -3])  # 输出 y g
# 每隔 1 个，取一个字符
print(s[::2])  # 输出 caytogi eygo

# start、end 以及 step 都可以省略。
# 获取s中从索引5处到结束的子串
print(s[5:])  # 输出it.org is very good
# 获取s中从倒数第6个字符到结束的子串
print(s[-6:])  # 输出y good
# 获取s中从开始到索引5处的子串
print(s[: 5])  # 输出crazy
# 获取s中从开始到倒数第6个字符的子串
print(s[: -6])  # 输出crazyIt.org is ver

# 此外，Python 字符串还支持用 in 运算符判断是否包含某个子串。
# 判断s是否包含'very'子串
print('very' in s)  # True
print('fkit' in s)  # False

# 还可使用全局内置的 min() 和 max() 函数获取字符串中最小字符和最大字符。
# # 输出s字符串中最大的字符
print(max(s))  # z
# # 输出s字符串中最大的字符
print(min(s))  # 空格
