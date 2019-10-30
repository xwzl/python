# 在实际调试程序的过程中，有时只获得异常的类型是远远不够的，还需要借助更详细的异常信息才能解决问题。
#
# 捕获异常时，有 2 种方式可获得更多的异常信息，分别是：
#
#   使用 sys 模块中的 exc_info 方法；
#   使用 traceback 模块中的相关函数。
#
# 本节首先介绍如何使用 sys 模块中的 exc_info() 方法获得更多的异常信息。
#
#   有关 sys 模块更详细的介绍，可阅读《Python sys模块》。
#
# 模块 sys 中，有两个方法可以返回异常的全部信息，分别是 exc_info() 和 last_traceback()，这两个函数有相同的功能和用法，本节仅以 exc_info() 方法为例。
#
# exc_info() 方法会将当前的异常信息以元组的形式返回，该元组中包含 3 个元素，分别为 type、value 和 traceback，它们的含义分别是：
#   type：异常类型的名称，它是 BaseException 的子类（有关 Python 异常类，可阅读《Python常见异常类型》一节）
#   value：捕获到的异常实例。
#   traceback：是一个 traceback 对象。
# 使用 sys 模块之前，需使用 import 引入
import sys
import traceback

try:
    x = int(input("请输入一个被除数："))
    print("30除以", x, "等于", 30 / x)
except:
    # 输出结果中，第 2 行是抛出异常的全部信息，这是一个元组，有 3 个元素，第一个元素是一个 ZeroDivisionError 类；第 2 个元素是异常类型 ZeroDivisionError 类的一个实例；第 3 个元素为
    # 一个 traceback 对象。其中，通过前 2 个元素可以看出抛出的异常类型以及描述信息，对于第 3 个元素，是一个 traceback 对象，无法直接看出有关异常的信息，还需要对其做进一步处理。
    # print(sys.exc_info())
    traceback.print_tb(sys.exc_info()[2])
    print("其他异常...")

# 要查看 traceback 对象包含的内容，需要先引进 traceback 模块，然后调用 traceback 模块中的 print_tb 方法，并将 sys.exc_info() 输出的 traceback 对象作为参数参入。

