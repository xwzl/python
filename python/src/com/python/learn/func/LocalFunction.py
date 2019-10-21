# 前面所看到的函数都是在全局范围内定义的，它们都是全局函数。Python 还支持在函数体内定义函数，这种被放在函数体内定义的函数称为局部函数。
#
# 在默认情况下，局部函数对外部是隐藏的，局部函数只能在其封闭（enclosing）函数内有效，其封闭函数也可以返回局部函数，以便程序在其他作用域中使用局部函数。
def get_math_func(types, nn):
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

    # 调用局部函数
    if types == "square":
        return square(nn)
    elif types == "cube":
        return cube(nn)
    else:
        return factorial(nn)


# 如果封闭函数没有返回局部函数，那么局部函数只能在封闭函数内部调用，如上面程序所示。另外，还会出现一种情况，如果封闭函数将局部函数返回，且程序使用变量保存了封闭函数
# 的返回值，那么这些局部函数的作用域就会被扩大
print(get_math_func("square", 3))  # 输出9
print(get_math_func("cube", 3))  # 输出27
print(get_math_func("", 3))  # 输出6


# 部函数内的变量也会遮蔽它所在函数内的局部变量（这句话有点拗口）
def foo():
    # 局部变量name
    name = 'Charlie'

    # 该错误是由局部变量遮蔽局部变量导致的，在 bar() 函数中定义的 name 局部变量遮蔽了它所在 foo() 函数内的 name 局部变量，又因为 bar() 函数中的 name 局部变量定义在
    # print() 输出函数之后，使的 print(name) 执行时找不到合适的 name，因此导致程序报错。
    def bar():
        # 避免全局变量被重定义
        # 为了声明 bar() 函数中的“name='孙悟空'”赋值语句不是定义新的局部变量，只是访问它所在 foo() 函数内的 name 局部变量，Python 提供了 nonlocal 关键字，通过 nonlocal 语
        # 句即可声明访问赋值语句只是访问该函数所在函数内的局部变量。
        nonlocal name
        # 访问bar函数所在的foo函数的name局部变量
        print(name)  # Charlie
        # 不再是定义新的局部变量，而是访问它所在函数（foo() 函数）内的 name 局部变量
        name = '孙悟空'
        print(name)

    bar()
    # 也会影响原来的值
    print(name)


# nonlocal 和前面介绍的 global 功能大致相似，区别只是 global 用于声明访问全局变量，而 nonlocal 用于声明访问当前函数所在函数内的局部变量。
foo()
