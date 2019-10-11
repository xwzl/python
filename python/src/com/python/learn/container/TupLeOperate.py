# 元组是 python 中另一个重要的序列结构，和列表类似，也是有一系列按特定顺序排序的元素组成。和列表不同的是
# 列表可以任意操作元素，是可变序列；而元组是不可变序列，即元组中的元素不可以单独修改。
#
# 元组可以看做是不可变得的列表。通常情况下，元组用于保存不可修改的内容。
#
# 从形式上看，元组的所有元素都放在一对小括号中，相邻元素之间用逗号分隔，如下所示：
#
#   （e1,e2,...,en）
#
# 其中 element1~elementn 表示元组中的各个元素，个数没有限制，且只要是 Python 支持的数据类型就可以。
#
# 从存储内容上看，元组可以存储整数、实数、字符串、列表、元组等任何类型的数据，并且在同一个元组中，元素的类型可以不同，例如：
#
#   ("c.biancheng.net",1,[2,'a'],("abc",3.0))
#
# 在这个元组中，有多种类型的数据，包括整形、字符串、列表、元组。
#
# 另外，我们都知道，列表的数据类型是 list，那么元组的数据类型是什么呢？通过 type() 函数，就可以查看到元组的数据类型，例如：
#
#   >>> type(("c.biancheng.net",1,[2,'a'],("abc",3.0)))
#   <class 'tuple'>
#
# 可以看到，元组是 typle 类型，这也是很多教程中用 tuple 指代元组的原因。

# Python 创建元组
#
# Python 提供了多种创建元组的方法，下面一一进行介绍。
#
# 和其他类型的 Python 变量一样，在创建元组时，可以使用赋值运算符“=”直接将一个元组赋值给变量，其语法格式如下：
#
#       tuplename = (element1,element2,...,elementn)
#
# 其中，tuplename 表示创建的元组名，可以使用任何符合 Python 命名规则，且不和 Python 内置函数重名的标识符作为元组名。
# 再次强调，创建元组的语法和创建列表的语法非常相似，唯一的不同在于，创建列表使用的是 []，而创建元组使用的是 ()。

print("------------- = 运算符直接创建元组 -------------")

# 合法元组对象
num = (7, 14, 21, 28, 35)
a_tuple = ("C语言中文网", "http://c.biancheng.net")
python = ("Python", 19, [1, 2], ('c', 2.0))

print(a_tuple)

# 创建元组 a_typle
a_tuple = ("C语言中文网",)
print(type(a_tuple))
print(a_tuple)

# 需要额外注意的一点是，当创建的元组中只有一个元素时，此元组后面必须要加一个逗号“,”，否则 Python 解释器会将其误认为字符串
# 创建字符串 a
a = ("C语言中文网")
print(type(a))
print(a)

print("需要额外注意一点的是,元组中只有一个元素是，python 解释器会误认为字符串")

# 使用tuple()函数创建元组
#
# 除了第一种最常见的创建方式外，Python还提供了 tuple() 函数来创建元组，它可以直接将列表、区间（range）等对象转换成元组。
#
# tuple 函数的语法格式如下：
#
#   tuple(data)
#
# 其中，data 表示可以转化为元组的数据，其类型可以是字符串、元组、range 对象等。

# 将列表元素转换为元组
# 将列表转换成元组
a_list = ['crazyIt', 20, -1.2]
a_tuple = tuple(a_list)
print(a_tuple)
# 使用range()函数创建区间（range）对象
a_range = range(1, 5)
print(a_range)
# 将区间转换成元组
b_tuple = tuple(a_range)
print(b_tuple)
# 创建区间时还指定步长
c_tuple = tuple(range(4, 20, 3))
print(c_tuple)

# python 访问元祖元素
#
# 和列表完全一样，如果想访问元组中的元素，可以使用元组中各元素的索引值获取，
getTuple = (1, 2, 3, 4)
print("获取单个元素", getTuple[1])

print("通过切片获取元组元素：", getTuple[:2])

# python 修改元组元素
#
# 前面讲过，元组是不可变序列，元组的元素不可以单独进行修改。但是元组也不是完全不能修改

# 我们可以对元组进行重新赋值：
a_tuple = ('crazyit', 20, -1.2)
print(a_tuple)
# 对元组进行重新赋值
a_tuple = ('c.biancheng.net', "C语言中文网")
print(a_tuple)

# 另外，还可以通过连接多个元组的方式向元组中添加新元素。例如：
a_tuple = ('crazyit', 20, -1.2)
print(a_tuple)
# 连接多个元组
a_tuple = a_tuple + ('c.biancheng.net',)
print(a_tuple)
# 需要注意的是，在使用此方式时，元组连接的内容必须都是元组，不能将元组和字符串或列表进行连接，否则或抛出 TypeError 错误

# Python删除元组
a_tuple = ('crazyit', 20, -1.2)
print(a_tuple)
# 删除a_tuple元组,基本不用删除 垃圾回收机制
# del (a_tuple)
