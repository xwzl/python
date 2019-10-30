# logging模块用法快速攻略
#
# 无论使用哪种编程语言，最常用的调试代码的方式是：使用输出语句（比如 C 语言中使用 printf，Python 中使用 print() 函数）输出程序运行过程中一些关键的变量的值，查看它们的
# 值是否正确，从而找到出错的地方。这种调试方法最大的缺点是，当找到问题所在之后，需要再将用于调试的输出语句删掉。
#
# 在 Python 中，有一种比频繁使用 print() 调试程序更简便的方法，就是使用 logging 模块，该模块可以很容易地创建自定义的消息记录，这些日志消息将描述程序执行何时到达日志函数
# 调用，并列出指定的任何变量当时的值。
#
# 启用 logging 模块很简单，直接将下面的代码复制到程序开头：
import logging

# 读者不需要关心这两行代码的具体工作原理，但基本上，当 Python 记录一个事件的日志时，它会创建一个 LogRecord 对象，保存关于该事件的信息。
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 假如我们编写了如下一个函数，其设计的初衷是用来计算一个数的阶乘，但该函数有些问题，需要调试：
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s%%)' % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % n)
    return total


# 可以看到，通过 logging.debug() 函数可以打印日志信息，这个 debug() 函数将调用 basicConfig() 打印一行信息，这行信息的格式是在 basicConfig() 函数中指定的，并
# 且包括传递给 debug() 的消息。
#
# 分析程序的运行结果，factorial(5) 返回 0 作为 5 的阶乘的结果，这显然是不对的。for 循环应该用从 1 到 5 的数，乘以 total 的值，但 logging.debug() 显示的日志信
# 息表明，i 变量从 0 开始，而不是 1。因为 0 乘任何数都是 0，所以接下来的迭代中，total 的值都是错的。日志消息提供了可以追踪的痕迹，帮助我们弄清楚程序运行过程哪里不
# 对。
print(factorial(5))
logging.debug('End of program')

# Python logging日志级别
#
# “日志级别”提供了一种方式，按重要性对日志消息进行分类。5 个日志级别如表 1 所示，从最不重要到最重要。利用不同的日志函数，消息可以按某个级别记入日志。
#
# 日志级别的好处在于，我们可以改变想看到的日志消息的优先级。比如说，向 basicConfig() 函数传入 logging.DEBUG 作为 level 关键字参数，这将显示所有级别为 DEBUG 的日
# 志消息。当开发了更多的程序后，我们可能只对错误感兴趣，在这种情况下，可以将 basicConfig() 的 level 参数设置为 logging.ERROR，这将只显示 ERROR 和 CRITICAL 消息，
# 跳过 DEBUG、INFO 和 WARNING 消息。
#
# Python logging禁用日志
#
# 在调试完程序后，可能并不希望所有这些日志消息出现在屏幕上，这时就可以使用 logging.disable() 函数禁用这些日志消息，从而不必进入到程序中，手工删除所有的日志调用。
#
# logging.disable() 函数的用法是，向其传入一个日志级别，它会禁止该级别以及更低级别的所有日志消息。因此，如果想要禁用所有日志，只要在程序中添加 logging.disable(logging.CRITICAL) 即可
#
# 因为 logging.disable() 将禁用它之后的所有消息，所以可以将其添加到程序中更接近 import logging 的位置，这样更容易找到它，方便根据需要注释掉它，或取消注释，从而启用或禁用日志消息。
#
# 将日志消息输出到文件中
#
# 虽然日志消息很有用，但它们可能塞满屏幕，让你很难读到程序的输出。考虑到这种情况，可以将日志信息写入到文件，既能使屏幕保持干净，又能保存信息，一举两得。
#
# 将日志消息输出到文件中的实现方法很简单，只需要设置 logging.basicConfig() 函数中的 filename 关键字参数即可，例如：
#
#   import logging
#   logging.basicConfig(filename='demo.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#
# 此程序中，将日志消息存储到了 demo.txt 文件中，该文件就位于运行的程序文件所在的目录。

