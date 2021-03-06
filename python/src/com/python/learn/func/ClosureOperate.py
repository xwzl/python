# 闭包，又称闭包函数或者闭合函数，其实和前面讲的嵌套函数类似，不同之处在于，闭包中外部函数返回的不是一个具体的值，而是一个函数。一般情
# 况下，返回的函数会赋值给一个变量，这个变量可以在后面被继续执行调用。
print(2 ** 3)


# 闭包函数，其中 exponent 称为自由变量
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方
print(square(2))  # 计算 2 的平方
print(cube(2))  # 计算 2 的立方


# 看到这里，读者可能会问，为什么要闭包呢？上面的程序，完全可以写成下面的形式：
def nth_power_rewrite(base, exponent):
    return base ** exponent


# 上面程序确实可以实现相同的功能，不过使用闭包，可以让程序变得更简洁易读。设想一下，比如需要计算很多个数的平方，那么读者觉得写成下面哪一种形式更好呢？
# 不使用闭包
res1 = nth_power_rewrite(1, 2)
res2 = nth_power_rewrite(2, 2)
res3 = nth_power_rewrite(3, 2)
print(res1)
print(res2)
print(res3)

# 使用闭包
# 其次，和缩减嵌套函数的优点类似，函数开头需要做一些额外工作，当需要多次调用该函数时，如果将那些额外工作的代码放在外部函数，就可以减少多次调用导致的不必要开销，提高程序的运行效率。
square = nth_power(2)
res1 = square(1)
res2 = square(2)
res3 = square(3)
print(res1)
print(res2)
print(res3)


# 闭包类似于偏向函数
def hello_people(ketty):
    def inner(tiger):
        return tiger, ketty

    return inner


# Python闭包的__closure__属性
#
# 闭包比普通的函数多了一个 __closure__ 属性，该属性记录着自由变量的地址。当闭包被调用时，系统就会根据该地址找到对应的自由变量，完成整体的函数调用。
#
# 以 nth_power() 为例，当其被调用时，可以通过 __closure__ 属性获取自由变量（也就是程序中的 exponent 参数）存储的地址
square = nth_power(2)
# 查看 __closure__ 的值
print(square.__closure__)

people = hello_people("people")
# baby
baby, babies = people("baby")
print(baby, babies)
print(people.__closure__)
