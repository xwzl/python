# Python装饰器的应用场景
#
# 装饰器用于身份认证
#
# 首先是最常见的身份认证的应用。这个很容易理解，举个最常见的例子，大家登录微信，需要输入用户名密码，然后点击确认，这样服务器端便会查询你的用户名是否存在、是否和密码匹配等等。
# 如果认证通过，就可以顺利登录；反之，则提示你登录失败。
#
# 再比如一些网站，你不登录也可以浏览内容，但如果你想要发布文章或留言，在点击发布时，服务器端便会查询你是否登录。如果没有登录，就不允许这项操作等等
# import functools
# def authenticate(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         request = args[0]
#         # 如果用户处于登录状态
#         if check_user_logged_in(request):
#             # 执行函数 post_comment()
#             return func(*args, **kwargs)
#         else:
#             raise Exception('Authentication failed')
#
#     return wrapper
#
#
# @authenticate
# def post_comment(request, ...)
#
# 注意，对于函数来说，它也有自己的一些属性，例如 __name__ 属性，代码中 @functools.wraps(func) 也是一个装饰器，如果不使用它，则 post_comment.__name__ 的值为 wrapper。而使用
# 它之后，则 post_comment.__name__ 的值依然为 post_comment。
#
# 上面这段代码中，定义了装饰器 authenticate，函数 post_comment() 则表示发表用户对某篇文章的评论，每次调用这个函数前，都会先检查用户是否处于登录状态，如果是登录状态，则允许这项操
# 作；如果没有登录，则不允许。

# 装饰器用于日志记录
#
# 日志记录同样是很常见的一个案例。在实际工作中，如果你怀疑某些函数的耗时过长，导致整个系统的延迟增加，想在线上测试某些函数的执行时间，那么，装饰器就是一种很常用的手段。
import time
import functools


# 装饰器用于记载函数执行时间
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {:.3f} ms'.format(func.__name__, (end - start) * 1000))
        return res

    return wrapper


# 这里，装饰器 log_execution_time 记录某个函数的运行时间，并返回其执行结果。如果你想计算任何函数的执行时间，在这个函数上方加上@log_execution_time即可。
@log_execution_time
def calculate_similarity(items):
    print("Hello " + items)


calculate_similarity("face book")

# 装饰器用于输入合理性检查
# 在大型公司的机器学习框架中，调用机器集群进行模型训练前，往往会用装饰器对其输入（往往是很长的 json 文件）进行合理性检查。这样就可以大大避免输入不正确对机器造成的巨大开销。
# 它的写法往往是下面的格式：
# import functools
# def validation_check(input):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         ... # 检查输入是否合法
#
# @validation_check
# def neural_network_training(param1, param2, ...):
#
# 其实在工作中，很多情况下都会出现输入不合理的现象。因为我们调用的训练模型往往很复杂，输入的文件有成千上万行，很多时候确实也很难发现。
#
# 试想一下，如果没有输入的合理性检查，很容易出现“模型训练了好几个小时后，系统却报错说输入的一个参数不对，成果付之一炬”的现象。这样的“惨案”，大大减缓了开发效率，也对机器资源造成了巨大浪费。

# 缓存装饰器

# 关于缓存装饰器的用法，其实十分常见，这里以 Python 内置的 LRU cache 为例来说明。
#
# LRU cache，在 Python 中的表示形式是 @lru_cache。@lru_cache 会缓存进程中的函数参数和结果，当缓存满了以后，会删除最近最久未使用的数据。
#
# 正确使用缓存装饰器，往往能极大地提高程序运行效率。举个例子，大型公司服务器端的代码中往往存在很多关于设备的检查，比如使用的设备是安卓还是 iPhone，版本号是多少。
# 这其中的一个原因，就是一些新的功能，往往只在某些特定的手机系统或版本上才有（比如 Android v200+）。
#
# 这样一来，我们通常使用缓存装饰器来包裹这些检查函数，避免其被反复调用，进而提高程序运行效率，比如写成下面这样：
# @lru_cache
# def check(param1, param2, ...) # 检查用户设备类型，版本号等等
