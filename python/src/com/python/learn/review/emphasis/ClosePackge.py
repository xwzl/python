# 闭包

def foo():
    print("简单嗲用")


def coo():
    print("简单调用")
    return foo


coo()()  # 相当于 coo() foo() 连续调用


def outer1():
    print("外部函数")

    def inner():
        print("内部函数第一次")

        def inner_inner():
            print("内部函数第二次")

        return inner_inner

    return inner


# 连续套娃
inner_fuc = outer1()
inner_fuc()
inner_inner_func = inner_fuc()

outer1()()()


def outer():
    x = 10  # 在外部函数里定义了一个变量x,是一个局部变量

    def inner():
        # 在内部函数如何修改外部函数的局部变量
        nonlocal x  # 此时，这里的x不再是新增的变量，而是外部的局部变量x
        y = x + 1
        print('inner里的y = ', y)
        x = 20  # 不是修改外部的x变量，而是在inner函数内部又创建了一个新的变量x

    return inner


outer()()
