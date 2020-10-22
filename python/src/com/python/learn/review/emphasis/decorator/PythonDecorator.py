# Python 内置的 3 种函数装饰器，分别是 ＠staticmethod、＠classmethod 和 @property，其中 staticmethod、classmethod 和 property 都是 Python 的内置函数。
# 那么，我们是否可以开发自定义的函数装饰器呢
#
# 答案是肯定的。当程序使用“＠函数”（比如函数 A）装饰另一个函数（比如函数 B）时，实际上完成如下两步：
#
#   将被修饰的函数（函数 B）作为参数传给 ＠ 符号引用的函数（函数 A）。
#   将函数 B 替换（装饰）成第 1 步的返回值
#
# 从上面介绍不难看出，被“＠函数”修饰的函数不再是原来的函数，而是被替换成一个新的东西（取决于装饰器的返回值）。其实所谓的装饰器，就是通过装饰器函数，来修改原函数的一些
# 功能，使得原函数不需要修改
def funA(fn):
    print('A')
    fn()  # 执行传入的fn参数
    return 'fkit'


'''
下面装饰效果相当于：funA(funB)，
funB 将会替换（装饰）成 funA() 语句的返回值；
由于funA()函数返回 fkit，因此 funB 就是 fkit
'''


@funA
def funB():
    print('B')


print(funB)  # fkit


# 其实，简单地理解函数装饰器的作用，上面程序可以等价地转换成如下程序：
#
#   def funA(fn):
#      print('A')
#      fn() # 执行传入的fn参数
#      return 'fkit'
#   def funB():
#        print('B')
#   funB = funA(funB)
#   print(funB) # fkit
# 注意，此程序中的 funB = funA(funB) 就等同于上面程序中 @funA 所起的作用。

# 上面程序使用 ＠funA 修饰 funB，这意味着程序要完成两步操作：
# 将 funB 作为 funA() 的参数，也就是上面代码中 @funA 相当于执行 funA(funB)。
# 将 funB 替换成 funA() 执行的结果，funA() 执行完成后返回 fkit，因此 funB 就不再是函数，而是被替换成一个字符串。

def hello(fn):
    fn()
    return "test"


@hello
def baby():
    print("pay")


# 这个方法只能那个啥对的，不加括号
print(baby)


def sex():
    print("Happy")


sex()


# 别忘记了，被修饰的函数总是被替换成 ＠ 符号所引用的函数的返回值，因此被修饰的函数会变成什么，完全由于 ＠ 符号所引用的函数的返回值决定，换句话说，如
# 果 ＠ 符号所引用的函数的返回值是函数，那么被修饰的函数在替换之后还是函数

# 带参数的函数装饰器
#
# 读者可能会想到，如果原函数 funB() 中有参数需要传递给函数装饰器，应该如何实现？
#
# 一个简单的办法是，可以在对应的函数装饰器 funA() 上，添加相应的参数
def foo(fn):
    # 定义一个嵌套函数
    def bar(a):
        fn(a * (a - 1))
        print("*" * 15)
        return fn(a * (a - 1))

    return bar


'''
下面装饰效果相当于：foo(my_test)，
my_test将会替换（装饰）成该语句的返回值；
由于foo()函数返回bar函数，因此my_test就是bar
同时，my_test 的参数 a 对应 bar 函数的参数 a
'''


@foo
def my_test(a):
    print("==my_test函数==", a)


# 打印my_test函数，将看到实际上是bar函数
print(my_test)
# 下面代码看上去是调用my_test()，其实是调用bar()函数
my_test(10)


def days(fn):
    def full_days(years):
        fn(years * 365)
        return years * 365

    return full_days


@days
def age(mix):
    print("好天气啊")


# 装饰器的作用相当于模板方法
print(age(10))


# 在此基础上，还有一个问题，如果程序中另外还有一个函数，也需要使用 funA 装饰器，但是这个新的函数有 2 个参数，此时又该怎么办呢？
# 在这种情况下，最简单的解决方式是用 *args 和 **kwargs 作为 foo 函数装饰器内部函数 bar() 的参数，*args 和 **kwargs 表示接受任意数量和类型的参数，因此函数装饰器可以写成下面的形式：
def foo(fn):
    # 定义一个嵌套函数
    def bar(*args, **kwargs):
        fn(*args, **kwargs)

    return bar


@foo
def my_test(a):
    print("==my_test函数==", a)


@foo
def new_test(a, b):
    print("==new_test函数==", a, " ", b)


my_test(10)
new_test(6, 5)


# 带自定义参数的函数装饰器
#
# 其实，函数装饰器还有更大程度的灵活性。刚刚说了，装饰器可以接受原函数任意类型和数量的参数，除此之外，它还可以接受自己定义的参数。
#
# 举个例子，比如要定义一个参数，来表示装饰器内部函数被执行的次数，那么就可以写成下面这种形式：
def foo(num):
    def my_decorator(fn):
        def bar(*args, **kwargs):
            for i in range(num):
                fn(*args, **kwargs)

        return bar

    return my_decorator


@foo(3)
def my_test(a):
    print("==my_test函数==", a)


@foo(5)
def new_test(a, b):
    print("==new_test函数==", a, " ", b)


my_test(10)
new_test(6, 5)

# 函数装饰器也可以嵌套
#
# 上面示例中，都是使用一个装饰器的情况，但实际上，Python 也支持多个装饰器，比如：
#
#   @decorator1
#   @decorator2
#   @decorator3
#   def func():
#         ...
# 上面程序的执行顺序是里到外，所以它等效于下面这行代码：
#
#   decorator1( decorator2( decorator3(func) ) )
#
# 这里不再给出具体实例，有兴趣的读者可自行编写程序进行测试。
