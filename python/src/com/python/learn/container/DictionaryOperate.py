# 和列表相同，字典也是许多数据的集合，属于可变序列类型。不同之处在于，它是无序的可变序列，其保存的内容是以“键值对”的形式存放的。
#
# 字典类型是 Python 中唯一的映射类型。“映射”是数学中的术语，简单理解，它指的是元素之间相互对应的关系，即通过一个元素，可以唯一找到另一个元素。
#
# 字典中，习惯将各元素对应的索引称为键（key），各个键对应的元素称为值（value），键及其关联的值称为“键值对”。
#
# 字典类型很像学生时代常用的新华字典。我们知道，通过新华字典中的音节表，可以快速找到想要查找的汉字。其中，字典里的音节表就相当于字典类型中的键，而键对应的汉字则相当于值。
#
#               主要特征	                                                        解释
#       通过键而不是通过索引来读取元素	    字典类型有时也称为关联数组或者散列表（hash）。它是通过键将一系列的值联系起来的，这样就可以通过键从字典中获取指定项，但不能通过索引来获取。
#       字典是任意数据类型的无序集合	        和列表、元组不同，通常会将索引值 0 对应的元素称为第一个元素。而字典中的元素是无序的。
#       字典是可变的，并且可以任意嵌套	    字典可以在原处增长或者缩短（无需生成一个副本），并且它支持任意深度的嵌套，即字典存储的值也可以是列表或其它的字典。
#       字典中的键必须唯一	                字典中，不支持同一个键出现多次，否则，只会保留最后一个键值对。
#       字典中的键必须不可变	                字典中的值是不可变的，只能使用数字、字符串或者元组，不能使用列表。
#
#   Python 中的字典类型相当于 Java 或者 C++ 中的 Map 对象。
#
# 和列表、元组一样，字典也有它自己的类型。Python 中，字典的数据类型为 dict，通过 type() 函数

jsonStr = {'name': '张三', 'age': 12}
print("我的乖乖，json 字符串就是 map 对象，就是 Java 中 map 对象", jsonStr)
print(jsonStr.get("age"))

# Python创建字典
#
# 创建字典的方式有很多，下面一一做介绍。
#
# 花括号语法创建字典
#
# 由于字典中每个元素都包含 2 部分，分别是键和值，因此在创建字典时，键和值之间使用冒号分隔，相邻元素之间使用逗号分隔，所有元素放在大括号 {} 中。
#
# 可以看到，同一字典中，键值可以是整数、字符串或者元组，只要符合唯一和不可变的特性；对应的值可以是 Python 支持的任意数据类型。
print("\npython 第一种赋值方式 {}")
scores = {'语文': 89, '数学': 92, '英语': 93}
print(scores)
# 空的花括号代表空的dict
empty_dict = {}
print(empty_dict)
# 使用元组作为dict的key
dict2 = {(20, 30): 'good', 30: [1, 2, 3]}
print(dict2)

# 通过 fromkeys() 方法创建字典
#
# Python 中，还可以使用 dict 字典类型提供的 fromkeys() 方法创建所有键值为空的字典，使用此方法的语法格式为：
#
#   dictName = dict.fromkeys(list，value=None)
#
# 其中，list 参数表示字典中所有键的列表，value 参数默认为 None，表示所有键对应的值。
print("字典第二种赋值方式，dict.fromkeys")
subject = {"语文", "数学", "英语"}  # set
# 这里用 set 的原因是保证 key 的唯一性
fromkeys = dict.fromkeys(subject)
print("dict.fromkeys 创建的 dict value 为空", fromkeys)
print(type([1, 2, 3]))
print(type({1, 2, 3}))
# 可以看到，dict_fromkeys 列表中的元素全部作为了 scores 字典的键，而各个键对应的值都为空（None）。此种创建方式，通常用于初始化字典，设置 value 的默认值。
dict_fromkeys = dict.fromkeys("areYou")
print(dict_fromkeys)

# 通过 dict() 映射函数创建字典
#
# 通过 dict() 函数创建字典的写法有多种，表 2 罗列出了常用的几种方式，它们创建的都是同一个字典 a。

# 注意，其中的 one、two、three 都是字符串，但使用此方式创建字典时，字符串不能带引号。
print("\n dict() 方法创建数据")
one = dict(one=1, two=2, three=3)
print("one", one)

# 向 dict() 函数传入列表或元组，而它们中的元素又各自是包含 2 个元素的列表或元组，其中第一个元素作为键，第二个元素作为值
print("\n dict() 方法通过元组或者list创建数据")
two = [["x11", "11"], ["x12", "12"]]
three = [("x21", "21"), ("x22", "22")]
print("列表--列表", dict(two))
print("列表--元组", dict(three))
four = (("y11", "11"), ("y12", "12"))
five = (["y21", "21"], ["y22", "22"])
print("元组--元组", dict(four))
print("元组--列表", dict(five))

# 通过应用 dict() 函数和 zip() 函数，可将前两个列表转换为对应的字典。
keys = ["key1", "key2"]
values = ["value", "value2"]
six = dict(zip(keys, values))
print(six)

# 创建空的字典
dict5 = dict()
print(dict5)

# Python 访问字典
#
# 和列表、元组不同，它们访问元素都是通过下标，而字典不同，它是通过键来访问对应的元素值。
#
# 因为字典中元素是无序的，所以不能像列表、元组那样，采用切片的方式一次性访问多个元素。
#
# 例如，如果想访问刚刚建立的字典 a 中，获取元素 1，可以使用下面的代码：
#
#   >>> a['one']
#   1
#
# 在使用此方法获取指定键的值时，如果键不存在，则会抛出如下异常：
#
#   >>> a['four']
#   Traceback (most recent call last):
#       File "<pyshell#2>", line 1, in <module>
#       a['four']
#   KeyError: 'four'
#
# 另外，除了上面这种方式外，Python 更推荐使用 dict 类型提供的 get() 方法获取指定键的值。get() 方法的语法格式为：
#
#       dict.get(key[,default])
#
# 其中，dict 指的是所创建的字典名称；key 表示指定的键；default 用于指定要查询的键不存在时，此方法返回的默认值，如果不手动指定，会返回 None。
#
# 例如，通过 get() 方法获取字典 a 中“two”对应的值，执行代码如下
a = dict(one=1, two=2, three=3)
a.get('two')
# 指定默认值
print(a.get(12, "1"))
items = a.items()
print(items)
a.pop("one")
print(a)

# 由于字典属于可变序列，所以我们可以任意操作字典中的键值对（key-value 对）。Python 中，常见的字典操作有以下几种：
#
#   向现有字典中添加新的键值对。
#   修改现有字典中的键值对。
#   从现有字典中删除指定的键值对。
#   判断现有字典中是否存在指定的键值对。
#
# 初学者要牢记，字典中常常包含多个键值对，而 key 是字典的关键数据，字典的基本操作都是围绕 key 值实现的。

# Python字典添加键值对
# 如果要为 dict 添加键值对，只需为不存在的 key 赋值即可。
base_dict = {"one": 1, "two": 2}
print("dict 判断键是否存在用 in", "one" in base_dict)
base_dict["three"] = 3
print(base_dict)
print("true") if "four" in base_dict else print("false")
print(base_dict)

if "four" in base_dict:
    base_dict["four"] = 16
    print("如果 base_dict 中存在键 \"four\" 则修值为16", base_dict)
else:
    print("base_dict 不存在 \"four\"键")

# del base_dict['four']  # 容易报错
# base_dict.pop('four')
print(base_dict)

# dict 的常用方法
print("============================== dict 常用方法演示==============================")

print(dir(dict))

# Python keys()、values() 和 items()方法
# 这 3 个方法之所以放在一起介绍，是因为它们都用来获取字典中的特定数据。keys() 方法用于返回字典中的所有键；values() 方法用于返回字典中所有键对应的值；
# items() 用于返回字典中所有的键值对。
print("Python keys()、values() 和 items()方法")
common_method = {'one': 1, 'two': 2}
print(common_method.keys())
print(common_method.values())
print(common_method.items())

# 注意，在 Python 2.x 中，这三个方法的返回值是列表类型。但在 Python 3 中，并不是我们常见的列表和元组类型，因为 Python 3不希望用户直接操作这几个方法的返回值。
# 如果想使用返回的数据，有以下 2 种方法：
print(list(common_method.keys()))

for key in common_method.keys():
    print(key, end=" ")
print()

for values in common_method.values():
    print(values, end=" ")
print()

for key, value in common_method.items():
    print(key, ":", value, end=" ")
print

# 共享变量都是浅拷贝
deep_copy = common_method.copy()
deep_copy["one"] = 11
print("深拷贝的值不会会影响原来对象的值", deep_copy, common_method)

# 注意，copy() 方法所遵循的拷贝原理，既有深拷贝，也有浅拷贝。拿拷贝字典 a 为例，copy() 方法只会对最表层的键值对进行深拷贝，也就是说，
# 它会再申请一块内存用来存放 {'one': 1, 'two': 2, 'three': []}；而对于某些列表类型的值来说，此方法对其做的是浅拷贝，也就是说，b 中的
# [1,2,3] 的值不是自己独有，而是和 a 共有。

a = {'one': 1, 'two': 2, 'three': [1, 2, 3]}
b = a.copy()
# 向 a 中添加新键值对，由于b已经提前将 a 所有键值对都深拷贝过来，因此 a 添加新键值对，不会影响 b。
a['four'] = 100
print(a)
print(b)
# 由于 b 和 a 共享[1,2,3]（浅拷贝），因此移除 a 中列表中的元素，也会影响 b。
a['three'].remove(1)
del a["one"]
# 总结 dict 的 copy 方法对键是深拷贝，原对象键的删除不会影响拷贝对象的值，新增键值对也不会影响拷贝对象的值，但是原对象对共享变量值得修改会影响拷贝对象的值
print(a)
print(b)

# python 中的 update()方法
#
# update() 方法可使用一个字典所包含的键值对来更新己有的字典。
#
# 在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，那么原 value 会被覆盖；如果被更新的字典中不包含对应的键值对，则该键值对被添加进去。
update_dict = {"x": 1, "y": 2}
update_dict.update({"x": 2, "z": 3})
# 从上面的执行过程可以看出，由于被更新的 dict 中已包含 key 为“one”的键值对，因此更新时该键值对的 value 将被改写；但如果被更新的 dict 中不包含 key 为“four”的键值对，
# 那么更新时就会为原字典增加一个键值对。
print(update_dict)

# pop() 方法用于获取指定 key 对应的 value，并删除这个键值对。
print(update_dict.pop("x"))
print(update_dict)

# Python popitem()方法
#
# popitem() 方法用于随机弹出字典中的一个键值对。
#
# 注意，此处的随机其实是假的，它和 list.pop() 方法一样，也是弹出字典中最后一个键值对。但由于字典存储键值对的顺序是不可知的，因此 popitem() 方法总是弹出底层存储的最后一个键值对。
a = {'one': 1, 'two': 2, 'three': 3}
print(a)
# 弹出字典底层存储的最后一个键值对
print(a.popitem())
print(a)

# 实际上，由于 popitem 弹出的是一个元组，因此我们也可以通过序列解包的方式，用两个变量分别接收 key 和 value。
a = {'one': 1, 'two': 2, 'three': 3}
# 将弹出项的key赋值给k、value赋值给v
k, v = a.popitem()
print(k, v)

# Python setdefault()方法
#
# setdefault() 方法也用于根据 key 来获取对应 value 的值。但该方法有一个额外的功能，即当程序要获取的 key 在字典中不存在时，该方法会先为这个不存在的 key
# 设置一个默认的 value，然后再返回该 key 对应的 value。
#
# 也就是说，setdefault() 方法总能返回指定 key 对应的 value；如果该键值对存在，则直接返回该 key 对应的 value；如果该键值对不存在，则先为该 key 设置默认的
# value，然后再返回该 key 对应的 value。
a = {'one': 1, 'two': 2, 'three': 3}
# 设置默认值，该key在dict中不存在，新增键值对
print(a.setdefault('four', 9.2))
print(a)
# 设置默认值，该key在dict中存在，不会修改dict内容
print(a.setdefault('one', 3.4))
print(a)
