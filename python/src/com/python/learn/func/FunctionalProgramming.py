# 所谓函数式编程，是指代码中每一块都是不可变的，都由纯函数的形式组成。这里的纯函数，是指函数本身相互独立、互不影响，对于相同的输入，总会有相同的输出。
#
# 除此之外，函数式编程还具有一个特点，即允许把函数本身作为参数传入另一个函数，还允许返回一个函数。
#
# 例如，想让列表中的元素值都变为原来的两倍，可以使用如下函数实现：
import functools


def multiply_2(lists):
    for index in range(0, len(lists)):
        lists[index] *= 2
    return lists


lists = [1, 2, 3, 4, 5, 6]
print(multiply_2(lists))
print([x * 2 for x in lists])


# 而要想让 multiply_2() 成为一个纯函数的形式，就得重新创建一个新的列表并返回，也就是写成下面这种形式：
def multiply_2_pure(list):
    new_list = []
    for item in list:
        new_list.append(item * 2)
    return new_list


# 函数式编程的优点，主要在于其纯函数和不可变的特性使程序更加健壮，易于调试和测试；缺点主要在于限制多，难写。
#
# 注意，纯粹的函数式编程语言（比如 Scala），其编写的函数中是没有变量的，因此可以保证，只要输入是确定的，输出就是确定的；而允许使用变量的程序设计语言，由于函数内部的变量状态不
# 确定，同样的输入，可能得到不同的输出。
#
# Python 允许使用变量，所以它并不是一门纯函数式编程语言。Python 仅对函数式编程提供了部分支持，主要包括 map()、filter() 和 reduce() 这 3 个函数，它们通常都结合 lambda 匿
# 名函数一起使用。接下来就对这 3 个函数的用法做逐一介绍。

# Python map()函数
#
# map() 函数的基本语法格式如下：
#
#   map(function, iterable)
#
# 其中，function 参数表示要传入一个函数，其可以是内置函数、自定义函数或者 lambda 匿名函数；iterable 表示一个或多个可迭代对象，可以是列表、字符串等。
#
# map() 函数的功能是对可迭代对象中的每个元素，都调用指定的函数，并返回一个 map 对象。
#
#   注意，该函数返回的是一个 map 对象，不能直接输出，可以通过 for 循环或者 list() 函数来显示。
list_map = [1, 2, 3, 4, 5, 6]
maps = map(lambda x: str(x) + "1", list_map)
# map 方法获取的变量不能直接获取值
print(maps)
print(list(maps))
# 被消费了就没有值
for value in maps:
    print(" value:", value)

# 注意，由于 map() 函数是直接由用 C 语言写的，运行时不需要通过 Python 解释器间接调用，并且内部做了诸多优化，所以相比其他方法，此方法的运行效率最高。
listDemo1 = [1, 2, 3, 4, 5]
listDemo2 = [3, 4, 5, 6, 7]
new_list = map(lambda x, y: x + y, listDemo1, listDemo2)
print(list(new_list))

# Python filter()函数
#
# filter()函数的基本语法格式如下：
#
#   filter(function, iterable)
#
# 此格式中，function 参数表示要传入一个函数，iterable 表示一个可迭代对象。
#
# filter() 函数的功能是对 iterable 中的每个元素，都使用 function 函数判断，并返回 True 或者 False，最后将返回 True 的元素组成一个新的可遍历的集合。
listDemo = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, listDemo)
print(list(new_list))


def divModTwo(x):
    return x % 2 == 0


listDemo = [1, 2, 3, 4, 5]
demo = filter(divModTwo, listDemo)
print(list(demo))

# filter 好像不可以多个参数
new_list = map(lambda x, y: x - y > 0, [3, 5, 6], [1, 5, 8])
print(list(new_list))

# Python reduce()函数
#
# reduce() 函数通常用来对一个集合做一些累积操作，其基本语法格式为：
#
#   reduce(function, iterable)
#
# 其中，function 规定必须是一个包含 2 个参数的函数；iterable 表示可迭代对象。
#
# 注意，由于 reduce() 函数在 Python 3.x 中已经被移除，放入了 functools 模块，因此在使用该函数之前，需先导入 functools 模块。
listDemo = [1, 2, 3, 4]
# 累计相乘
product = functools.reduce(lambda x, y: x * y, listDemo)
print(product)

# 总结
#
# 通常来说，当对集合中的元素进行一些操作时，如果操作非常简单，比如相加、累积这种，那么应该优先考虑使用 map()、filter()、reduce() 实现。另外，在数据量
# 非常多的情况下（比如机器学习的应用），一般更倾向于函数式编程的表示，因为效率更高。
#
# 当然，在数据量不多的情况下，使用 for 循环等方式也可以。不过，如果要对集合中的元素做一些比较复杂的操作，考虑到代码的可读性，通常会使用 for 循环。
