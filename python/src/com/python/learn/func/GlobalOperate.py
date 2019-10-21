def hello():
    x = 1
    print(locals())
    print(globals())
    print(globals()['y'])
    # 但实际上，不管是使用 globals() 还是使用 locals() 获取的全局范围内的“变量字典”，都可以被修改，而这种修改会真正改变全局变量本身
    globals()['y'] = 12
    # 但通过 locals() 获取的局部范围内的“变量字典”，即使对它修改也不会影响局部变量
    locals()['x'] = 12
    print(x)


y = 2
hello()
print(y)
# 函数外部调用，其实和 globals 获取的变量字典值一样
print(locals())
