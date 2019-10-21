# 全局变量遮蔽
#
# 我们知道，全局变量默认可以在所有函数内被访问，但是，如果当函数中定义了与全局变量同名的变量时，就会发生局部变量遮蔽（hide）全局变量的情形，例如如下程序：
name = 'Charlie'


def test():
    # 直接访问name全局变量
    # print(name)  # Charlie
    # 该错误提示所访问的 name 变量还未定义。这是什么原因呢？这正是由于程序在 test() 函数中增加了“name='孙悟空'”一行代码造成的。
    # Python 语法规定，在函数内部对不存在的变量赋值时，默认就是重新定义新的局部变量，这会使得函数内部遮蔽重名的 name 全局变量。由于局部变量 name 在 print(name) 后才初始化，所以程序会报错。
    name = '孙悟空'
    print(name)  # Charlie


# 访问被遮蔽的全局变量。如果希望程序依然能访问 name 全局变量，且在函数中可重新定义 name 局部变量，也就是在函数中可以访问被遮蔽的全局变量，此时可通过 globals() 函数来实现
def test_plus():
    # 直接访问name全局变量
    print(globals()['name'])  # Charlie
    name = '孙悟空'


# 增加了“global name”声明之后，程序会把 name 变量当成全局变量，这意味着 test() 函数后面对 name 赋值的语句只是对全局变量赋值，而不是重新定义局部变量。
def test_global():
    # 声明name是全局变量，后面的赋值语句不会重新定义局部变量
    global name
    # 直接访问name全局变量
    print(name)  # Charlie
    name = '孙悟空'


# 总结：如果函数想调用全局变量，直接使用或者 globals['key'] 获取或者修改变量值。但是想命名与全局变量名称相同的局部变量名称，必须显示的调用 global 字段重新定义
# 全局变量的名称变为局部变量，例如 test_global 方法
test()
print(name)
