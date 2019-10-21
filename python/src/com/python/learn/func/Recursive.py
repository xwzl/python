# 在一个函数体内调用它自身，被称为函数递归。函数递归包含了一种隐式的循环，它会重复执行某段代码，但这种重复执行无须循环控制。
#
# 例如有如下数学题。己知有一个数列：f(0) = 1，f(1) = 4，f(n + 2) = 2*f(n+ 1) +f(n)，其中 n 是大于 0 的整数，求 f(10) 的值。
# 这道题可以使用递归来求得。下面程序将定义一个 fn() 函数，用于计算 f(10) 的值。 f(n)=2*f(n-1)+f(n-2) n>=2

cache = {}


def hello_table_plus(n):
    if n == 0:
        return 1
    if n == 1:
        return 4
    if cache.get(n) is None:
        cache[n] = 2 * hello_table(n - 1) + hello_table(n - 2)
        return cache.get(n)
    else:
        return cache.get(n)


def hello_table(n):
    if n == 0:
        return 1
    if n == 1:
        return 4
    return 2 * hello_table(n - 1) + hello_table(n - 2)


print(hello_table())
print(hello_table_plus(34))


