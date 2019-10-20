# 很多编程语言都允许定义个数可变的参数，这样可以在调用函数时传入任意多个参数。Python 也不例外，在定义函数时也可以使用可变参数。
#
# 可变参数，又称不定长参数，即传入函数中的实际参数可以是任意多个。Python 定义可变参数，主要有以下 2 种形式。
#
# 1 可变参数：形参前添加一个 '*'
#
# 此种形式的语法格式如下所示：
#
#   *args
#
# 其中，args 表示创建一个名为 args 的空元组，该元组可接受任意多个外界传入的非关键字实参。
def books(total, *book):
    print(book)
    for value in book:
        print(value)


# *可变参数把参数当作元组传入
books(12, "java 入门到放弃", "python 入门到放弃")


# Python 允许个数可变的形参可以处于形参列表的任意位置（不要求是形参列表的最后一个参数）但同时普通参数必须以关键字实参的形式传值
# 定义了支持参数收集的函数
def test(*hello, num):
    print(hello)
    # books被当成元组处理
    for b in hello:
        print(b)
    print(num)


# 调用test()函数
test("C语言中文网", "Python教程", num=20)


# 可变参数：形参前添加两个'*'
#
# 这种形式的语法格式如下：
#
#   **kwargs
#
# *kwargs 表示创建一个名为 kwargs 的空字典。该字典可以接收任意多个以关键字参数赋值的实际参数。

# 定义了支持参数收集的函数
def test(x, y, z=3, *book, **scores):
    print(x, y, z)
    print(book)
    print(scores)


test(1, 2, 3, "C语言中文网", "Python教程", 语文=89, 数学=94)

# 这里需要注意一点，对于以上面方式定义的 test() 函数，参数 z 的默认值几乎不能发挥作用。比如按如下方式调用 test() 函数
test(1, 2, "C语言中文网", "Python教程", 语文=89, 数学=94)


