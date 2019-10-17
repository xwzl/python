# Python 中，要想知道一个字符串有多少个字符（获得字符串长度），或者一个字符串占用多少个字节，可以使用 len 函数。
#
# len 函数的基本语法格式为：
# len（string）
#
# 其中 string 用于指定要进行长度统计的字符串。
#
# 例如，定义一个字符串，内容为“http://c.biancheng.net”，然后用 len() 函数计算该字符串的长度
var = "Hello World!"
print(len(var))

# 在实际开发中，除了常常要获取字符串的长度外，有时还要获取字符串的字节数。
#
# 在 Python 中，不同的字符所占的字节数不同，数字、英文字母、小数点、下划线以及空格，各占一个字节，而一个汉字可能占 2~4 个字节，具体占多少个，取决于采用的编码方式。
#
# 例如，汉字在 GBK/GB2312 编码中占用 2 个字节，而在 UTF-8 编码中一般占用 3 个字节。
#
# 以 UTF-8 编码为例，字符串“人生苦短，我用Python”所占用的字节数如图 1 所示。
#
# 我们可以通过使用 encode() 方法，将字符串进行编码后再获取它的字节数。例如，采用 UTF-8 编码方式，计算“人生苦短，我用Python”的字节数
str1 = "人生苦短，我用Python"
len(str1.encode())

# 因为汉字加中文标点符号共 7 个，占 21 个字节，而英文字母和英文的标点符号占 6 个字节，一共占用 27 个字节。
#
# 同理，如果要获取采用 GBK 编码的字符串的长度，可以执行如下代码：
str1 = "人生苦短，我用Python"
len(str1.encode('gbk'))


