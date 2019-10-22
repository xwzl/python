# 函数高级用法
#
# Python 的函数是“一等公民”，因此函数本身也是一个对象，函数既可用于赋值，也可用作其他函数的参数，还可作为其他函数的返回值。
#
# 使用函数变量
#
# Python 的函数也是一种值：所有函数都是 function 对象，这意味着可以把函数本身赋值给变量，就像把整数、浮点数、列表、元组赋值给变量一样。
# 定义一个计算乘方的函数
def powers(base, exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result


# 将pow函数赋值给my_fun，则my_fun可当成pow使用
my_fun = powers
print(my_fun(3, 4))  # 输出81


# 定义一个计算面积的函数
def area(width, height):
    return width * height


# 将area函数赋值给my_fun，则my_fun可当成area使用
my_fun = area
print(my_fun(3, 4))  # 输出12


def hello_world(name, vip):
    print("%s hello world ! %s" % (name, vip))


vip_man = hello_world
vip_man(name="Jack", vip="hello")


# 使用函数作为函数形参
#
# 有时候需要定义一个函数，该函数的大部分计算逻辑都能确定，但某些处理逻辑暂时无法确定，这意昧着某些程序代码需要动态改变，如果希望调用函数时能动态传入这些代
# 码，那么就需要在函数中定义函数形参，这样即可在调用该函数时传入不同的函数作为参数，从而动态改变这段代码。
# 定义函数类型的形参，其中fn是一个函数
def map_plus(data_plus, fn):
    result = []
    # 遍历data列表中每个元素，并用fn函数对每个元素进行计算
    # 然后将计算结果作为新数组的元素
    for e in data_plus:
        result.append(fn(e))
    return result


# 定义一个计算平方的函数
def square(n):
    return n * n


# 定义一个计算立方的函数
def cube(n):
    return n * n * n


# 定义一个计算阶乘的函数
def factorial(n):
    result = 1
    for index in range(2, n + 1):
        result *= index
    return result


data = [3, 4, 9, 5, 8]
print("原数据: ", data)
# 下面程序代码3次调用map()函数，每次调用时传入不同的函数
print("计算数组元素的平方")
print(map_plus(data, square))
print("计算数组元素的立方")
print(map_plus(data, cube))
print("计算数组元素的阶乘")
print(map_plus(data, factorial))


# 传说中的 lambda 表达式前身
def lambda_hello(text, qq):
    return qq(text)


# 写的什么
def qq_hello(p):
    return [x + x * (x + 1) for x in p]


p = range(1, 10)

for x in lambda_hello(p, qq_hello):
    print(x)


# 使用函数作为返回值（闭包）

def get_math_func(type):
    # 定义一个计算平方的局部函数
    def square(n):  # ①
        return n * n

    # 定义一个计算立方的局部函数
    def cube(n):  # ②
        return n * n * n

    # 定义一个计算阶乘的局部函数
    def factorial(n):  # ③
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    # 返回局部函数
    if type == "square":
        return square
    if type == "cube":
        return cube
    else:
        return factorial


# 调用get_math_func()，程序返回一个嵌套函数
math_func = get_math_func("cube")  # 得到cube函数
print(math_func(5))  # 输出125
math_func = get_math_func("square")  # 得到square函数
print(math_func(5))  # 输出25
math_func = get_math_func("other")  # 得到factorial函数
print(math_func(5))  # 输出120