# 我们知道，最早的字符串编码是 ASCII 编码，它仅仅对 10 个数字、26 个大小写英文字母以及一些特殊字符进行了编码。ASCII 码做多只能表示 256 个符号，每个字符只需要占用 1 个字节。
#
# 随着信息技术的发展，各国的文字都需要进行编码，于是相继出现了 GBK、GB2312、UTF-8 编码等，其中 GBK 和 GB2312 是我国制定的中文编码标准，规定英文字符母占用 1 个字节，中文字符占用 2 个字节；
# 而 UTF-8 是国际通过的编码格式，它包含了全世界所有国家需要用到的字符，其规定英文字符占用 1 个字节，中文字符占用 3 个字节。
#
# Python 3.x 默认采用 UTF-8 编码格式，有效地解决了中文乱码的问题。
#
# 在 Python 中，有 2 种常用的字符串类型，分别为 str 和 bytes 类型，其中 str 用来表示 Unicode 字符，bytes 用来表示二进制数据。str 类型和 bytes 类型之间就需要使用 encode() 和
# decode()方法进行转换。
#
# Python encode()方法
#
# encode() 方法为字符串类型（str）提供的方法，用于将 str 类型转换成 bytes 类型，这个过程也称为“编码”。
#
# encode() 方法的语法格式如下：
# str.encode([encoding="utf-8"][,errors="strict"])
#
# 注意，格式中用 [] 括起来的参数为可选参数，也就是说，在使用此方法时，可以使用 [] 中的参数，也可以不使用。
#
# 该方法各个参数的含义
#
# encoding = "utf-8":指定进行编码时采用的字符编码，该选项默认采用 utf-8 编码。例如，如果想使用简体中文，可以设置 gb2312。当方法中只使用这一个参数时，可以省略前边的“encoding=”，直接写编码
# 格式，例如 str.encode("UTF-8")。
#
# errors = "strict":
#
# 指定错误处理方式，其可选择值可以是：
#
#   strict：遇到非法字符就抛出异常。
#   ignore：忽略非法字符。
#   replace：用“？”替换非法字符。
#   xmlcharrefreplace：使用 xml 的字符引用。
#
# 该参数的默认值为 strict。
#
# 注意，使用 encode() 方法对原字符串进行编码，不会直接修改原字符串，如果想修改原字符串，需要重新赋值。
str = "C语言中文网"
print(str.encode())
print(str.encode('GBK'))

# Python decode()方法
#
# 和 encode() 方法正好相反，decode() 方法用于将 bytes 类型的二进制数据转换为 str 类型，这个过程也称为“解码”。
#
# decode() 方法的语法格式如下：
#
#   bytes.decode([encoding="utf-8"][,errors="strict"])
#
# 该方法中各参数的含义如表 2 所示。
#
#   参数	                    含义
#   bytes	            表示要进行转换的二进制数据。
#   encoding="utf-8"	指定解码时采用的字符编码，默认采用 utf-8 格式。当方法中只使用这一个参数时，可以省略“encoding=”，直接写编码方式即可。
#
# 注意，对 bytes 类型数据解码，要选择和当初编码时一样的格式。
#
#   errors = "strict"	指定错误处理方式，其可选择值可以是：
#   strict：遇到非法字符就抛出异常。
#   ignore：忽略非法字符。
#   replace：用“？”替换非法字符。
#   xmlcharrefreplace：使用 xml 的字符引用。
# 该参数的默认值为 strict。
str = "C语言中文网"
bytes = str.encode()
print(bytes.decode())
# 注意，如果编码时采用的不是默认的 UTF-8 编码，则解码时要选择和编码时一样的格式，否则会抛出异常
