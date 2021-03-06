# Python缓存重用机制 -- python 初始化变量并不一定开辟新的内存
#
# Python 缓冲机制是为提高程序执行的效率服务的，实际上就是在 Python 解释器启动时从内存空间中开辟出一小部分，用来存储高频使用的数据，这样可以大
# 大减少高频使用的数据创建时申请内存和销毁时撤销内存的开销。
#
# Python 在存储数据时，会根据数据的读取频繁程度以及内存占用情况来考虑，是否按照一定的规则将数据存储缓存中。那么问题来了，内存重用机制适用于哪些
# 基本数据类型呢？
#
# 表 1 罗列了 Python 是否将指定数据存入缓存中的规则：
#
#                数据类型	                    是否可以重用	                                            生效范围
#           范围在 [-5, 256] 之间的小整数	如果之前在程序中创建过，就直接存入缓存，后续不再创建。 	      全局
#                  bool 类型
#               字符串类型数据
#              大于 256 的整数	            只要在本代码块内创建过，就直接缓存，后续不再创建。	            本代码块
#             大于 0 的浮点型小数
#             小于 0 的浮点型小数	        不进行缓存，每次都需要额外创建。


# 范围在 [-5, 256] 之间的小整数
int1 = -5
int2 = -5
print("[-5, 256] 情况下的两个变量：", id(int1), id(int2))  # 此程序中，大量使用 id() 内置函数，该函数的功能是获取变量（对象）所在的内存地址。

# bool类型
bool1 = True
bool2 = True
print("bool类型情况下的两个变量：", id(bool1), id(bool2))

# 对于字符串
s1 = "3344"
s2 = "3344"
print("字符串情况下的两个交量", id(s1), id(s2))

# 大于 256 的整数
int3 = 257
int4 = 257
print("大于 256 的整数情况下的两个变量", id(int3), id(int4))

# 大于 0 的浮点数
f1 = 256.4
f2 = 256.4
print("大于 0 的浮点数情况下的两个变量", id(f1), id(f2))

# 小于 0 的浮点数
f3 = -2.45
f4 = -2.45
print("小于 0 的浮点数情况下的两个变量", id(f3), id(f4))

# 小于 -5 的整数
n1 = -6
n2 = -6
print("小于 -5 的整数情况下的两个变量", id(n1), id(n2))


# 好像 python3 对所有的变量都进行了缓存,不存在上面的缓存规则

def fun():
    # [-5,256]
    int1 = -5
    print("fun中 -5 的存储状态", id(int1), id(int2))

    # bool类型
    bool3 = True
    print("fun中 bool 类型的存储状态", id(bool3), id(bool2))

    # 字符串类型
    s1 = "3344"
    print("fun 中 3344 字符串的存储状态", id(s1), id(s2))
    # 大于 256
    int3 = 257
    print("fun中 257 的存储状态", id(int3), id(int4))
    # 浮点类型
    f1 = 256.4
    print("fun 中 256.4 的存储状态", id(f1), id(f2))
    # 小于 -5
    n1 = -6
    print("fun 中 -6 的存储状态", id(n1), id(n2))

fun()
