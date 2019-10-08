# 在实际开发中，经常需要将一些（不只一个）数据暂储起来，以便将来使用。说到这里，一些读者可能知道或听说过数组，它就可以把多个数据挨个存储到一起，通过数组下标可以访问数组中的
# 各个元素。但使用数组存储数据有一个弊端，就是所存储的数据必须类型一致。
#
# 需要明确的是，Python 中没有数组，但是加入了更加强大的列表。如果把数组看做是一个集装箱，那么 Python 的列表就是一个工厂的仓库。
#
# 从形式上看，列表会将所有元素都放在一对中括号 [] 中，相邻元素之间用逗号分隔，如下所示：
#
#       [element1,element2,element3,...,elementn]
#
# 格式中，element1~elementn 表示列表中的元素，个数没有限制，只要是 Python 支持的数据类型就可以。
#
# 从内容上看，列表可以存储整数、实数、字符串、列表、元组等任何类型的数据，并且和数组不同的是，在同一个列表中元素的类型也可以不同。比如说：
#
#       ["c.biancheng.net" , 1 , [2,3,4] , 3.0]
#
# 可以看到，列表中同时包含字符串、整数、列表、浮点数这些数据类型。
# 注意，在使用列表时，虽然可以将不同类型的数据放入到同一个列表中，但通常情况下不这么做，同一列表中只放入同一类型的数据，这样可以提高程序的可读性。
#
# 另外，在其它 Python 教程中，经常用 list 代指列表，这是因为列表的数据类型就是 list，通过 type() 函数就可以知道，例如：
#
#       type(["c.biancheng.net" , 1 , [2,3,4] , 3.0])
#
# 可以看到，它的数据类型为 list，就表示它是一个列表。
print("---------------------创建列表的两种形式---------------------")

# 使用 = 运算符直接创建列表
#
# 和其他类型的 Python 变量一样，创建列表时，也可以使用赋值运算符“=”直接将一个列表赋值给变量，其语法格式如下：
#
#       listname = [element1 , element2 , element3 , ... , elementn]
#
# 其中，listname 表示列表的名称，注意，在命名时既要符合 Python 命名规范，也要尽量避开与 Python 的内置函数重名。
num = [1, 2, 3, 4, 5, 6, 7]
name = ["C语言中文网", "http://c.biancheng.net"]
program = ["C语言", "Python", "Java"]
empty_list = []  # 创建空列表

# 使用list()函数创建列表
# 除使用前面介绍的方括号语法创建列表之外，Python 还提供了一个内置的 list() 函数来创建列表，它可用于将元组、区间（range）等对象转换为列表
a_tuple = ('1', '2', '3', '4', '5')
lists = list(a_tuple)  # 元祖转换为列表
# 使用range()函数创建区间（range）对象，左开右闭
a_range = range(1, 5)
# 将区间转换成列表
b_list = list(a_range)
print(b_list)

# 访问列表元素
# 除了单个访问列表元素，还可用切片的方式截取列表元素，获取新的列表
ranges = [1, 2, 3, 4, 5, 6, 7]
print(ranges[0])
print(ranges[1:2])  # 切片的操作也是左开右闭

# Python删除列表
# 对于已经创建的列表，如果不再使用，可以使用 del 语句将其删除。
# 实际开始时，del 语句不常用，因为 Python 自带的垃圾回收机制会自动销毁不用的列表，所以即使开发者不手动将其删除，Python 也会自动将其回收。
#
# del 的语法格式为：
#
#   del listName
#
# 其中，listName 表示要删除列表的名称。
names = ["C语言中文网", "http://c.biancheng.net"]
print(names)
del names  # 删除后的列表无法继续使用
# print(names)

print("---------------------列表添加元素---------------------")

# 列表添加元素
#
# 使用“+”运算符，确实可以像列表中添加元素。但是这种方式的执行效率并不高，更建议大家使用列表提供的 append() 方法
#
# Python append()方法添加元素
#
# append() 方法用于在列表的末尾追加元素，该方法的语法格式如下：
#
#   listName.append(element)
#
# 其中，listName 指的是要添加元素的列表；obj 表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等。
#
# 可以看到，即便给 append() 方法传递列表或者元组，此方法也只会将其视为一个元素，直接添加到列表中，从而形成包含列表和元组的新列表
appends = ['我', '们']
# 追加元组，元组被当成一个元素
tuples = ('是', '好')
appends.append(tuples)
print(appends)
# append 方法单个添加元素
appends.append('孩')
print(appends)
# 追加列表，列表被当成一个元素
appends.append(['子', '!'])
print(appends)
print("listName.append 方法将元祖、集合当成一个元素插入列表,对于类型校验比较严格列表，使用 listName.extend 方法比较合适\n")
# Python extend()方法添加元素
#
# 当然，如果希望不将被追加的列表或元组当成一个整体，而是只追加列表中的元素，则可使用列表提供的 extend() 方法。
#
# extend()方法的语法格式如下：
#
#   listName.extend(obj)
books = ['Java 入门到放弃', 'Python 入门到放弃']
# extend 方法将元祖和集合拆分为单独的个体添加
books.extend(("Go 入门当放弃", "C++ 入门到放弃"))  # 元祖
books.extend(["PHP 入门到放弃", "C 入门到放弃"])
print(books)
print("listName.extend 将元组、列表转换为一个一个的元素拼接到列表中\n")

# Python insert() 方法插入元素
#
# 如果希望在列表中间增加元素，则可使用列表的 insert() 方法，此方法的语法格式为：
#
#   listName.insert(index , obj)
#
# 其中，index 参数指的是将元素插入到列表中指定位置处的索引值。
#
# 使用 insert() 方法向列表中插入元素，和 append() 方法一样，无论插入的对象是列表还是元组，都只会将其整体视为一个元素。
inserts = ["WE", "EDG"]
inserts.insert(1, ("RNG", "JDG"))  # 插入指定的元素
inserts.insert(1, ["CG", "IG"])
print(inserts)
print("listName.insert(index,element) 向指定位置插入元素，目测性能不好")

print("---------------------列表添加元素---------------------\n")

# Python list列表删除元素（3种方法）
#
# 在列表中删除元素，主要分为以下 3 种应用场景：
#
#   根据目标元素所在位置的索引值进行删除，可使用 del 语句；
#   根据元素的值进行删除，可使用列表（list类型）提供的 remove() 方法；
#   将列表中所有元素全部删除，可使用列表（list类型）提供的 clear() 方法。
#
# 根据索引值删除元素
#
# 删除列表中指定元素，和删除列表类似，也可以使用 del 语句实现。
# del 语句是 Python 中专门用于执行删除操作的语句，不仅可用于删除列表的元素，也可用于删除变量等。
delLists = [1, 2, 3, 4, 5, 6]
del delLists[-1]
print(delLists)
print("del 删除元素直接指定元素索引删除即可")

# 删除中间一段，左开右闭吗？
del delLists[1:3]
print(delLists)
print("del 支持区间删除元素，同样是左开右闭")

# 根据元素值删除
#
# 除使用 del 语句之外，Python 还提供了 remove() 方法来删除列表元素，该方法并不是根据索引来删除元素的，而是根据元素本身的值来执行删除操作的。
#
# remove() 方法会删除第一个和指定值相同的元素，如果找不到该元素，该方法将会引发 ValueError 错误。
c_list = [20, 'crazyIt', 30, -4, 'crazyIt', 3.4]
# 删除第一次找到的30
c_list.remove(30)
print(c_list)
# 删除第一次找到的'crazyIt'
c_list.remove('crazyIt')
print(c_list)
# 再次尝试删除 30，会引发 ValueError 错误
# c_list.remove(30)
# 使用 remove 之前，最好判断元素是否存在
print(c_list.count(0))  # 获取列表中元素的个数

# clear 清楚所有元素
c_list.clear()
print(c_list)

print("---------------------修改元素---------------------\n")

# 列表的元素相当于变量，因此程序可以对列表的元素赋值，这样即可修改列表的元素
a_list = [2, 4, -3.4, 'crazyIt', 23]
# 对第3个元素赋值
a_list[2] = 'fKit'
print(a_list)  # [2, 4, 'fKit', 'crazyIt', 23]
# 对倒数第2个元素赋值
a_list[-2] = 9527
print(a_list)  # [2, 4, 'fKit', 9527, 23]

# 上面代码通过索引到列表元素赋值，程序既可使用正数索引，也可使用负数索引，这都没有问题。
#
# 此外，程序也可通过 slice 语法对列表其中一部分赋值。在执行这个操作时，并不要求新赋值的元素个数与原来的元素个数相等。
# 这意味着通过这种方式既可为列表增加元素，也可为列表删除元素。
b_list = list(range(1, 5))
print(b_list)
# 将第2个到第4个（不包含）元素赋值为新列表的元素
b_list[1: 3] = ['a', 'b']
print(b_list)  # [1, 'a', 'b', 4]

# 如果对列表中空的 slice 赋值，就变成了为列表插入元素
# 将第3个到第3个（不包含）元素赋值为新列表的元素，就是插入
b_list[2: 2] = ['x', 'y']
print(b_list)  # [1, 'a', 'x', 'y', 'b', 4]

# 如果将列表其中一段赋值为空列表，就变成了从列表中删除元素。例如如下代码：
# 将第3个到第6个（不包含）元素赋值为空列表，就是删除
b_list[2: 5] = []
print(b_list)  # [1, 'a', 4]

# 对列表使用 slice 语法赋值时，不能使用单个值；如果使用字符串赋值，Python 会自动把字符串当成序列处理，其中每个字符都是一个元素。例如如下代码：
# Python会自动将str分解成序列
b_list[1: 3] = 'Charlie'
print(b_list)  # [1, 'C', 'h', 'a', 'r', 'l', 'i', 'e']

# 在使用 slice 语法赋值时，也可指定 step 参数。但如果指定了 step 参数，则要求所赋值的列表元素个数与所替换的列表元素个数相等。例如如下代码：
c_list = list(range(1, 10))
# 指定step为2，被赋值的元素有4个，因此用于赋值的列表也必须有4个元素
c_list[2: 9: 2] = ['a', 'b', 'c', 'd']
print(c_list)  # [1, 2, 'a', 4, 'b', 6, 'c', 8, 'd']
