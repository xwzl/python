# 异常机制已经成为判断一门编程语言是否成熟的标准，除传统的像 C 语言没有提供异常机制之外，目前主流的编程语言如 Python、 Java、 Kotlin 等都提供了成熟的异常机制。
#
# 异常机制可以使程序中的异常处理代码和正常业务代间分离，保证程序代码更加优雅，并可以提高程序的健壮性。
#
# Python 的异常机制主要依赖 try 、except 、else、finally 和 raise 五个关键字：
# try 关键字后缩进的代码块简称 try 块，它里面放置的是可能引发异常的代码；
# 在 except 后对应的是异常类型和一个代码块，用于表明该 except 块处理这种类型的代码块；
# 在多个 except 块之后可以放一个 else 块，表明程序不出现异常时还要执行 else 块；
# 最后还可以跟一个 finally 块，finally 块用于回收在 try 块里打开的物理资源，异常机制会保证 finally 块总被执行；
# raise 用于引发一个实际的异常，raise 可以单独作为语句使用，引发一个具体的异常对象；
#
# Python 提供了try except语句捕获并处理异常，该异常处理语句的基本语法结构如下：
#
#   try:
#      可能产生异常的代码块
#   except [(Error1, Error2, ...) [as e]]:
#         处理异常的代码块1
#   except [(Error3, Error4, ...) [as e]]:
#         处理异常的代码块2
#
# 该格式中，[] 括起来的部分可以使用，也可以省略；(Error1,Error2,...) 、(Error3,Error4,...) 表示各自的 except 块可以处理异常的具体类型；[as e] 表示将异常类型赋值给
# 变量 e（方便在 except 块中调用异常类型）。
#
#   注意，except 后面也可以不指定具体的异常名称，这样的话，表示要捕获所有类型的异常。
#
# 另外，从 try except 的基本语法格式可以看出，try 块仅有一个，但 except 代码块可以有多个，这是为了针对不同的异常类型提供不同的异常处理方式。当程序发生不同的意外情况时，
# 会对应不同的异常类型，Python 解释器就会根据该异常类型来决定使用哪个 except 块来处理该异常。
# 通过在 try 块后提供多个 except 块可以无须在异常处理块中使用 if 判断异常类型，但依然可以针对不同的异常类型提供相应的处理逻辑，从而提供更细致、更有条理的异常处理逻辑。
#
# try except 语句的执行流程如下：
#
#   首先执行 try 中的代码块，如果执行过程中出现异常，系统会自动生成一个异常对象，该异常对象会提交给 Python 解释器，此过程被称为引发异常。
#   当 Python 解释器收到异常对象时，会寻找能处理该异常对象的 except 块，如果找到合适的 except 块，则把该异常对象交给该 except 块处理，这个过程被称为捕获异常。如果 Python
#
# 解释器找不到捕获异常的 except 块，则程序运行终止，Python 解释器也将退出。
#
# 事实上，不管程序代码块是否处于 try 块中，甚至包括 except 块中的代码，只要执行该代码块时出现了异常，系统总会自动生成一个 Error 对象。如果程序没有为这段代码定义任何的 except
# 块，则 Python 解释器无法找到处理该异常的 except 块，程序就会停止运行；反之，如果程序发生异常，并且该异常经 try 捕获并由 except 处理完成，则程序会继续执行。
try:
    a = int(input("输入被除数："))
    b = int(input("输入除数："))
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except (ValueError, ArithmeticError) as errors:
    print("程序发生了数字格式异常、算术异常之一")
    print(errors)
except():
    print("未知异常")
print("程序继续运行")


# 访问异常信息
#
# 如果程序需要在 except 块中访问异常对象的相关信息，可以通过为 except 块添加as a来实现。当 Python 解释器决定调用某个 except 块来处理该异常对象时，会将异常对象赋值给 except 块后
# 的异常变量，程序即可通过该变量来获得异常对象的相关信息。
#
# 所有的异常对象都包含了如下几个常用属性和方法：
#
#   args：该属性返回异常的错误编号和描述字符串。
#   errno：该属性返回异常的错误编号。
#   strerror：该属性返回异常的描述宇符串。
#   with_traceback()：通过该方法可处理异常的传播轨迹信息。
def foo():
    try:
        fis = open("a.txt");
    except Exception as e:
        # 访问异常的错误编号和详细信息
        print(e.args)
        # 访问异常的错误编号
        print(e.errno)
        # 访问异常的详细信息
        print(e.strerror)
        # print(e.with_traceback())


foo()

try:
    a = int(input("输入被除数："))
    b = int(input("输入除数："))
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except ValueError:
    print("数值错误：程序只能接收整数参数")
except ArithmeticError:
    print("算术错误")
except Exception:
    print("未知异常")

# 上面程序针对 ValueError、ArithmeticError 类型的异常，提供了专门的异常处理逻辑。该程序运行时的异常处理逻辑可能有如下几种情形：
# 如果在运行该程序时输入的参数不是数字，而是字母，将发生数值错误，Python 将调用 ValueError 对应的 except 块处理该异常。
# 如果在运行该程序时输入的第二个参数是 0，将发生除 0 异常，Python 将调用 ArithmeticError 对应的 except 块处理该异常。
# 如果在程序运行时出现其他异常，该异常对象总是 Exception 类或其子类的实例，Python 将调用 Exception 对应的 except 块处理该异常。
#
# 实际上，在进行异常捕获时，不仅应该把 Exception 类对应的 except 块放在最后，而且所有父类异常的 except 块都应该排在子类异常的 except 块的后面（ 即：先处理小异常，再处理大异常）。
# 虽然 Python 语法没有要求，但在实际编程时一定要记住先捕获小异常，再捕获大异常。


# 在 Python 中，还有另一种异常处理结构，就是 try except else 语句，也就是在原来 try except 语句的基础上再添加一个 else 子句，其作用是指定当 try 块中没有发现异常时要执行的代码。
# 换句话说，当 try 块中发现异常，则 else 块中的语句将不会被执行。
s = input('请输入除数:')
try:
    result = 20 / int(s)
    print('20除以%s的结果是: %g' % (s, result))
except ValueError:
    print('值错误，您必须输入数值')
except ArithmeticError:
    print('算术错误，您不能输入0')
else:
    print('没有出现异常')
print("程序继续运行")


def else_test():
    s = input('请输入除数:')
    result = 20 / int(s)
    print('20除以%s的结果是: %g' % (s, result))


def right_main():
    try:
        print('try块的代码，没有异常')
    except:
        print('程序出现异常')
    else:
        # 将else_test放在else块中
        else_test()


def wrong_main():
    try:
        print('try块的代码，没有异常')
        # 将else_test放在try块代码的后面
        else_test()
    except:
        print('程序出现异常')

# 对比上面两个输出结果，用户输入的都是 0，这样都会导致 else_test() 函数出现异常。如果将 else_test() 函数放在 try 块的代码的后面，此时 else_test() 函数运行产生的异常将会被 try 块
# 对应的 except 捕获，这正是 Python 异常处理机制的执行流程：但如果将 else_test() 函数放在 else 块中，当 else_test() 函数出现异常时，程序没有 except 块来处理该异常，该异常将会传
# 播给 Python 解释器，导致程序中止。
wrong_main()
right_main()
