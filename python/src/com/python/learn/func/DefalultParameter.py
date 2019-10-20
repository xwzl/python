# 我们知道，在调用函数时，如果不指定某个参数，解释器会抛出异常。为了解决这个问题，Python 允许为参数设置默认值，即在定义函数时，直接给形式参数指定一个默认值，
# 这样的话，即便调用函数时没有给拥有默认值的形参传递参数，该参数可以直接使用定义函数时设置的默认值。
#
# 定义带有默认值参数的函数，其语法格式如下：
#
#   def 函数名(...，形参名=默认值)：
#         代码块
#
# 注意，在使用此格式定义函数时，指定有默认值的形式参数必须在所有没默认值参数的最后，否则会产生语法错误。

def hello_python(language="python", description="非常好"):
    print(language, "是一个门编程语言")
    print("大家说它", description)


# 全部使用默认参数
hello_python()
# language 使用默认参数
hello_python(description="覆盖默认参数")
hello_python("java", "very nice")


# 再次强调，由于 Python 要求在调用函数时关键字参数必须位于位置参数的后面，因此在定义函数时指定了默认值的参数（关键字参数）必须在没有默认值的参数之后

# 定义一个打印三角形的函数，有默认值的参数必须放在后面
def print_triangle(char, height=5):
    for i in range(1, height + 1):
        # 先打印一排空格
        for j in range(height - i):
            print(' ', end='')
        # 再打印一排特殊字符
        for j in range(2 * i - 1):
            print(char, end='')
        print()


print_triangle('@', 6)
print_triangle('#', height=7)
print_triangle(char='*')
