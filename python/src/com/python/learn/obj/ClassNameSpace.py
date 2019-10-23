# 所有位于 class 语句中的代码，其实都位于特殊的命名空间中，通常称之为类命名空间。Python 中，编写的整个程序默认处于全局命名空间内，而类体则处于类命名空间内。
#
# Python 允许在全局范围内放置可执行代码，当 Python 执行该程序时，这些代码就会获得执行的机会。类似地，Python 同样允许在类范围内放置可执行代码，当 Python 执
# 行该类定义肘，这些代码同样会获得执行的机会。
global_fn = lambda p: print('执行lambda表达式，p参数: ', p)


class Category:
    cate_fn = lambda p, y: print('执行lambda表达式，p参数: ', p, y)


# 调用全局范围内的global_fn，为参数p传入参数值
global_fn('fkit')
c = Category()
# 调用类命名空间内的cate_fn，Python自动绑定第一个参数
c.cate_fn("hello")

