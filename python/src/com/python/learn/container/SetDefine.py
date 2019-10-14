# Python 中的集合，和数学中的集合概念一样，用来保存不重复的元素，即集合中的元素都是唯一的，互不相同。
#
# 从形式上看，和字典类似，Python 集合会将所有元素放在一对大括号 {} 中，相邻元素之间用“,”分隔，如下所示：
#
#   {element1,element2,...,element n}
#
# 其中，element n 表示集合中的元素，个数没有限制。
#
# 从内容上看，同一集合中，只能存储不可变的数据类型，包括整形、浮点型、字符串、元组，无法存储列表、字典、集合这些可变的数据类型，
# 否则 Python 解释器会抛出 TypeError 错误。
#
# 并且需要注意的是，数据必须保证是唯一的，因为集合对于每种数据元素，只会保留一份。例如：
#
#   {1,2,1,(1,2,3),'c','c'}
#
# 由于 Python 中的 set 集合是无序的，所以每次输出时元素的排序顺序可能都不相同。
#
# 其实，Python 中有两种集合类型，一种是 set 类型的集合，另一种是 frozenset 类型的集合，它们唯一的区别是，set 类型集合可以做添加、删
# 除元素的操作，而 forzenset 类型集合不行。
#
# Python 创建 set 集合
#
# Python 提供了两种创建 set 集合的方法，分别是使用{}创建和使用set()函数将列表、元组等类型数据转换为集合。

# 使用{}创建 set 集合
#
# 在 Python 中，创建 set 集合可以像列表、元素和字典一样，直接将集合赋值给变量，从而实现创建集合的目的，其语法格式如下：
#
#   setname = {element1,element2,...,element n}
#
# 其中，set_name 表示集合的名称，起名时既要符合 Python 命名规范，也要避免与 Python 内置函数重名
set_init = {1, 2, 3, 4, 5, 6, 7}
print(set_init)

for value in set_init:
    print("验证 set 集合随机性", value)

print(set_init.pop())

# set() 函数创建集合
#
# set() 函数为 Python 的内置函数，其功能是将字符串、列表、元组、range 对象等可迭代对象转换成集合。该函数的语法格式如下：
# setName = set(iteration)
#
# 其中，iteration 就表示字符串、列表、元组、range 对象等数据。
listData = [12, 13, 123, 422]
listConvertSet = set(listData)
print(listConvertSet)
print(set("hello set "))
print(set(range(1, 10, 2)))
print(set())  # 空 set 集合，如果用 {} 创建，python 会把它识别为空字典

# book
bookStore = "the %(book)s  of price is %(price)2.2f $"
javaBook = {"book": "《Java 入门到放弃》", "price": 12.5}
print(bookStore % javaBook)

if javaBook.get("price") > 12:
    print("这本书太贵了，买不起啊！")
else:
    print("这本如此实惠，考虑一下呢？")

for key, value in javaBook.items():
    print("key:", key, " value:", value)

# Python访问set集合元素
# 由于集合中的元素是无序的，因此无法向列表那样使用下标访问元素。Python 中，访问集合元素最常用的方法是使用循环结构，将集合中的数据逐一读取出来。
a = {1, 'c', 1, (1, 2, 3), 'c'}
print("set 集合取值")
for ele in a:
    print(ele, end=' ')

# Python删除set集合
# 和其他序列类型一样，手动函数集合类型，也可以使用 del() 语句，例如：
a = {1, 'c', 1, (1, 2, 3), 'c'}
print(a)
# del (a) 实际上不用删除变量，垃圾处理机制嘛
# print(a)


