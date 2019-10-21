# 简单的理解偏函数，它是对原始函数的二次封装，是将现有函数的部分参数预先绑定为指定值，从而得到一个新的函数，该函数就称为偏函数。相比原函数，偏函数具有较少的可变参数，
# 从而降低了函数调用的难度。
#
# 定义偏函数，需使用 partial 关键字（位于 functools 模块中），其语法格式如下：
#
#   偏函数名 = partial(func, *args, **kwargs)
#
# 其中，func 指的是要封装的原函数，*args 和 **kwargs 分别用于接收无关键字实参和关键字实参。
#
#   有关 *args 和 **kwargs 作为函数形参更详细的解释，可阅读《Python函数可变参数（*args, **kwargs）》一节。
#
# 下面举几个例子，让大家可以直观感受一下偏函数的用法和功能。
from functools import partial


def hello_world(name, content):
    print("%s say %s" % (name, content))


lists = ["people"]
# 定义偏函数，其封装了 hello_world() 函数，并为 name 参数设置了默认参数
HelloWorld = partial(hello_world, content="hello world")
# 由于 content 参数已经有默认值，因此调用偏函数时，可以不指定
# 注意，必须采用关键字参数的形式给 age 形参传参，因为如果以无关键字参数的方式，该实参将试图传递给 name 形参
HelloWorld("jack")


def mod(n, m):
    return n % m


# 定义偏函数，并设置参数 n 对应的实参值为 100
#
# 偏函数通过将任意数量（顺序）的参数，转化为另一个带有剩余参数的函数对象，从而实现了截取函数功能（偏向）的效果。在实际应用中，可以使用一个原函数，然后将其封
# 装多个偏函数，在调用函数时全部调用偏函数，一定程序上可以提高程序的可读性。
mod_by_100 = partial(mod, 100)
print(mod(100, 7))
print(mod_by_100(7))
