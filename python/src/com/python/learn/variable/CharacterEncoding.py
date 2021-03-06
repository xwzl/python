import sys

# 什么是字符编码？
# 我们知道，计算机是以二进制的形式来存储数据的，即它只认识 0 和 1 两个数字。 20 世纪 60 年代，是计算机发展的早期，这时美国是计算机领域的老大，它制定了一套编码
# 标准，解决了 128 个英文字符与二进制之间的对应关系，被称为 ASCII 字符编码（简称 ASCII 码）。
# ASCII 码，全称为美国信息交换标准代码，是基于拉丁字母的一套字符编码，主要用于显示现代英语，因为万维网的出现，使得 ASCII 码广为使用，其直到 2007 年 12 月才逐
# 渐被 Unicode 取代。
#
# 虽然英语用 128 个字符编码已经够用，但计算机不仅仅用于英语，如果想表示其他语言，128 个符号显然不够用，所以很多其他国家都在 ASCII 的基础上发明了很多别的编码，
# 例如包含了汉语简体中文格式的 GB2312 编码格式（使用 2 个字节表示一个汉字）。
#
# 也正是由于出现了很多种编码格式，导致了“文件显示乱码”的情况。比如说，发送邮件时，如果发信人和收信人使用的编码格式不一样，则收信人很可能看到乱码的邮件。基于这
# 个原因，Unicode 字符集应运而生。
#
# Unicode 字符集又称万国码、国际码、统一码等。从名字就可以看出来，它是以统一符号为目标的字符集。Unicode 对世界上大部分的文字系统进行了整理、编码，使得电脑可以
# 用更简单的方式来呈现和处理文字。
#
# 注意，在实际使用时，人们常常混淆字符集和字符编码这两个概念，我认为它们是不同的：
#
#   字符集定义了字符和二进制的对应关系，为每个字符分配了唯一的编号。可以将字符集理解成一个很大的表格，它列出了所有字符和二进制的对应关系，计算机显示文字或者存储
#   文字，就是一个查表的过程；
#   而字符编码规定了如何将字符的编号存储到计算机中，要知道，有些字符编码（如 GB2312 和 GBK）规定，不同字符在存储时所占用的字节数是不一样的，因此为了区分一个字符
#   到底使用了几个字节，就不能将字符的编号直接存储到计算机中，字符编号在存储之前必须要经过转换，在读取时还要再逆向转换一次，这套转换方案就叫做字符编码。
#
# Unicode 字符集可以使用的编码方案有三种，分别是：
#
#    UTF-8：一种变长的编码方案，使用 1~6 个字节来存储；
#    UTF-32：一种固定长度的编码方案，不管字符编号大小，始终使用 4 个字节来存储；
#    UTF-16：介于 UTF-8 和 UTF-32 之间，使用 2 个或者 4 个字节来存储，长度既固定又可变。
#
# 其中，UTF-8 是目前使用最广的一种 Unicode字符集的实现方式，可以说它几乎已经一统江湖了。

encoding = sys.getdefaultencoding()
print(encoding)

# python3 中也可以用 ord() 和 chr() 函数实现字符和编码数字之间的转换
print(ord('A'))  # 字符转换数字
print(ord('z'))
print(chr(101))  # 数字转换字符

# Python 3 新增了 bytes 类型，用于代表字节串（这是本教程创造的一个词，用来和字符串对应）。字符串（str）由多个字符组成，以字符为单位进行操作；字节串（bytes）由多个字节组成，以字节为单位进行操作。
#
# bytes 和 str 除操作的数据单元不同之外，它们支持的所有方法都基本相同，bytes 也是不可变序列。
#
# bytes 对象只负责以字节（二进制格式）序列来记录数据，至于这些数据到底表示什么内容，完全由程序决定。如果采用合适的字符集，字符串可以转换成字节串；反过来，字节串也可以恢复成对应的字符串。
#
# 由于 bytes 保存的就是原始的字节（二进制格式）数据，因此 bytes 对象可用于在网络上传输数据，也可用于存储各种二进制格式的文件，比如图片、音乐等文件。
#
# 如果希望将一个字符串转换成 bytes 对象，有如下三种方式：
#
#   如果字符串内容都是 ASCII 字符，则可以通过直接在字符串之前添加 b 来构建字节串值。
#   调用 bytes() 函数（其实是 bytes 的构造方法）将字符串按指定字符集转换成字节串，如果不指定字符集，默认使用 UTF-8 字符集。
#   调用字符串本身的 encode() 方法将字符串按指定字符集转换成字节串，如果不指定字符集，默认使用 UTF-8 字符集。

# 创建一个空的 bytes
b1 = bytes()

# 创建一个空的 byte
b2 = b''

# 同过 b 前缀指定 hello 是 bytes 类型的值
b3 = b'hello'

print(b3)  # 输出 b'hello'
print(b3[0])  # 输出 h 对应的 unicode 编码
print(b3[2:4])  # 输出 ll

# 调用 bytes 方法将字符串转换成 bytes 对象
b4 = bytes('这是一个字符串转字节数组', encoding='utf-8')
print(b4)

# 利用字符串的encode()方法编码成bytes，默认使用utf-8字符集
b5 = "这是一个字符串转字节数组".encode('utf-8')
print(b5)

# 编码和解码
print(b5.decode())

# \xe8\xbf\x99\xe6\x98\xaf\xe4\xb8\x80\xe4\xb8\xaa\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2\xe8\xbd\xac\xe5\xad\x97\xe8\x8a\x82\xe6\x95\xb0\xe7\xbb\x84
#
# 从上面的输出结果可以看出，字节串和字符串非常相似，只是字节串里的每个数据单元都是 1 字节。
#
#   计算机底层有两个基本概念：位（bit）和字节（Byte），其中 bit 代表 1 位，要么是 0，要么是 1，就像一盏灯，要么打开，要么熄灭；Byte 代表 1 字节，1 字节包含 8 位。
#
# 在字节串中每个数据单元都是字节，也就是 8 位，其中每 4 位（相当于 4 位二进制数，最小值为 0 ，最大值为 15）可以用一个十六进制数来表示，因此每字节需要两个十六进制数表示，所以
# 可以看到上面的输出是 b'\xe6\x88\x91\xe7\x88\xb1Python\xe7\xbc\x96\xe7\xa8\x8b'，比如 \xe6 就表示 1 字节，其中 \x 表示十六进制，e6 就是两位的十六进制数。
#
# 这里简单介绍一下字符集的概念。计算机底层并不能保存字符，但程序总是需要保存各种字符的，那该怎么办呢？计算机“科学家”就想了一个办法：为每个字符编号，当程序要保存字符时，实际上保
# 存的是该字符的编号；当程序读取字符时，读取的其实也是编号，接下来要去查“编号一字符对应表”（简称码表）才能得到实际的字符。
#
# 因此，所谓的字符集，就是所有字符的编号组成的总和。早期美国人给英文字符、数字、标点符号等字符进行了编号，他们认为所有字符加起来顶多 100 多个，只要 1 字节（8 位，支持 256 个字
# 符编号）即可为所有字符编号一一这就是 ASCII 字符集。
#
# 后来，亚洲国家纷纷为本国文字进行编号，即制订本国的字符集，但这些字符集并不兼容。于是美国人又为世界上所有书面语言的字符进行了统一编号，这次他们用了两个字节(16 位，支持 65536 个
# 字符编号），这就是 Unicode 字符集。实际使用的 UTF-8, UTF-16 等其实都属于 Unicode 字符集。
#
# 由于不同人对字符的编号完全可以很随意，比如同一个“爱”字，我可以为其编号为 99，你可以为其编号为 199，所以同一个编号在不同字符集中代表的字符完全有可能是不同的。因此，对于同一个字
# 符串，如果采用不同的字符集来生成 bytes 对象，就会得到不同的 bytes 对象
