# 函数注解是 Python 3 最独特的功能之一，关于它的介绍，官方文档是这么说的，“函数注解是关于用户自定义函数使用类型的完全可选的元信息”。也就是说，官方将函数注解的用途
# 归结为：为函数中的形参和返回值提供类型提示信息。
#
# 下面是对 Python 官方文档中的示例稍作修改后的程序，可以很好的展示如何定义并获取函数注解：
#
# def f(ham:str,egg:str='eggs')->str:
#   pass
# print(f.__annotations__)
#
# 输出结果为：
#
# {'ham': <class 'str'>, 'egg': <class 'str'>, 'return': <class 'str'>}
#
# 如上所示，给函数中的参数做注解的方法是在形参后添加冒号“：”，后接需添加的注解（可以是类（如 str、int 等），也可以是字符串或者表示式）；给返回值做注解的方法是将注解
# 添加到 def 语句结尾的冒号和 -> 之间。
#
# 注意，如果参数有默认值，参数注解位于冒号和等号之间。比如 eggs:str='eggs'，它表示 eggs 参数的默认值为 'eggs'，添加的注解为 str。
#
# 给函数定义好注解之后，可以通过函数对象的 __annotations__ 属性获取，它是一个字典，在应用运行期间可以获取。
def no_operate(x: int, y: str = "default value") -> str:
    return str(x) + y


print("python 中加一个 ： 就是加入注解", no_operate(1), no_operate(1, "value"))
print(no_operate.__annotations__)


# 事实上，函数注解并不局限于类型提示，而且在 Python 及其标准库中也没有单个功能可以利用这种注解，这也是这个功能独特的原因。
#
# 注意，函数注解没有任何语法上的意义，只是为函数参数和返回值做注解，并在运行获取这些注解，仅此而已。换句话说，为函数做的注解，Python不做检查，不做强制，不做验证，什么操
# 作都不做，函数注解对Python解释器没任何意义。
def square(number: "一个数字") -> "返回number的平方":
    return number ** 2


print(square(10))
print(square.__annotations__)

