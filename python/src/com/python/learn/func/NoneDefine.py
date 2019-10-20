# 在 Python 中，有一个特殊的常量 None（N 必须大写）。和 False 不同，它不表示 0，也不表示空字符串，而表示没有值，也就是空值。
#
# None 有自己的数据类型，我们可以在 IDLE 中使用 type() 函数查看它的类型
#
# 需要注意的是，None 是 NoneType 数据类型的唯一值（其他编程语言可能称这个值为 null、nil 或 undefined），也就是说，我们不能再创建其它 NoneType 类
# 型的变量，但是可以将 None 赋值给任何变量。如果希望变量中存储的东西不与任何其它值混淆，就可以使用 None。
#
# 除此之外，None 常用于 assert、判断以及函数无返回值的情况。举个例子，在前面章节中我们一直使用 print() 函数输出数据，其实该函数的返回值就是 None。
# 因为它的功能是在屏幕上显示文本，根本不需要返回任何值，所以 print() 就返回 None
#
# 另外，对于所有没有 return 语句的函数定义，Python 都会在末尾加上 return None，使用不带值的 return 语句（也就是只有 return 关键字本身），那么就返
# 回 None。