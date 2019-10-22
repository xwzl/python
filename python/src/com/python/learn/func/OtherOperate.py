# eval() 和 exec() 函数的功能是相似的，都可以执行一个字符串形式的 Python 代码（代码以字符串的形式提供），相当于一个 Python 的解释器。二者不同之
# 处在于，eval() 执行完要返回结果，而 exec() 执行完不返回结果
#
# eval()和exec()的用法
#
# eval() 函数的语法格式为：
#
#   eval(expression, globals=None, locals=None, /)
#
# 而 exec() 函数的语法格式如下：
#
#   exec(expression, globals=None, locals=None, /)
#
# 可以看到，二者的语法格式除了函数名，其他都相同，其中各个参数的具体含义如下：
#
#   expression：这个参数是一个字符串，代表要执行的语句 。该语句受后面两个字典类型参数 globals 和 locals 的限制，只有在 globals 字典和 locals 字典作用域内的函数和变量才能被执行。
#   globals：这个参数管控的是一个全局的命名空间，即 expression 可以使用全局命名空间中的函数。如果只是提供了 globals 参数，而没有提供自定义的 __builtins__，则系统会将当前环境中的
#            __builtins__ 复制到自己提供的 globals 中，然后才会进行计算；如果连 globals 这个参数都没有被提供，则使用 Python 的全局命名空间。
#   locals：这个参数管控的是一个局部的命名空间，和 globals 类似，当它和 globals 中有重复或冲突时，以 locals 的为准。如果 locals 没有被提供，则默认为 globals。
#
# 注意，__builtins__ 是 Python 的内建模块，平时使用的 int、str、abs 都在这个模块中。通过 print(dic["__builtins__"]) 语句可以查看 __builtins__ 所对应的 value。
#
# 首先，通过如下的例子来演示参数 globals 作用域的作用，注意观察它是何时将 __builtins__ 复制 globals 字典中去的：
dic = {'b': 3}  # 定义一个字
print(dic.keys())  # 先将 dic 的 key 打印出来，有一个元素 b
exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
print(dic.keys())  # exec 后，dic 的 key 多了一个

# 如果不加入呢？
qq = {'x': 3}
exec("pp = 3", qq)
print(qq.keys())

# 上面的代码是在作用域 dic 下执行了一句 a = 4 的代码。可以看出，exec之前 dic 中的 key 只有一个 b。执行完 exec() 之后，系统在 dic 中生成了两个新的 key，分别是 a 和 __builtins__。
# 其中，a 为执行语句生成的变量，系统将其放到指定的作用域字典里；__builtins__ 是系统加入的内置 key。
a = 10
b = 20
c = 30
g = {'a': 6, 'b': 8}  # 定义一个字典
t = {'b': 100, 'c': 10}  # 定义一个字典
print(eval('a+b+c', g, t))  # 定义一个字典 116
print(g.keys())
print(t.keys())

# exec()和eval()的区别
# 前面已经讲过，它们的区别在于，eval() 执行完会返回结果，而 exec() 执行完不返回结果。
a = 1
exec("a = 2")  # 相当于直接执行 a=2
print(a)
a = exec("2+3")  # 相当于直接执行 2+3，但是并没有返回值，a 应为 None
print(a)
a = eval('2+3')  # 执行 2+3，并把结果返回给 a
print(a)

# eval() 和 exec() 函数的应用场景
#
# 在使用 Python 开发服务端程序时，这两个函数应用得非常广泛。例如，客户端向服务端发送一段字符串代码，服务端无需关心具体的内容，直接跳过 eval() 或 exec() 来执行，这样的设计会使服务端与客户端的
# 耦合度更低，系统更易扩展。
#
# 另外，如果读者以后接触 TensorFlow 框架，就会发现该框架中的静态图就是类似这个原理实现的：
#
#   TensorFlow 中先将张量定义在一个静态图里，这就相当将键值对添加到字典里一样；
#   TensorFlow 中通过 session 和张量的 eval() 函数来进行具体值的运算，就当于使用 eval() 函数进行具体值的运算一样。
#
# 需要注意的是，在使用 eval() 或是 exec() 来处理请求代码时，函数 eval() 和 exec() 常常会被黑客利用，成为可以执行系统级命令的入口点，进而来攻击网站。解决方法是：通过设置其命名空间里的可执行函
# 数，来限制 eval() 和 exec() 的执行范围。
maps = {"a": 3, "b": 5}
print(eval("a + b", maps))

# exec 与 eval 是执行一串字符串的 python 代码
exec("print(a+b)", {"a": 10, "b": 20}, {"b": 50})  # local 变量范围内的参数会覆盖 globals 的参数
exec("print(a+b);print(a*b)", {"a": 10, "b": 20}, {"b": 50})
eval1 = eval("maps['a'] + maps['b']")
print(eval1)

# 常用的就是将字符串类型json转为json对象
a = "{'a': [1, 2, 3], 'b': (3, 4)}"
print(eval(a))
