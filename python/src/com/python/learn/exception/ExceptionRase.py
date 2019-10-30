# 很多时候，系统是否要引发异常，可能需要根据应用的业务需求来决定，如果程序中的数据、执行与既定的业务需求不符，这就是一种异常。由于与业务需求不符而产生的异常，必须由程序员来决定引发，
# 系统无法引发这种异常。
#
# 如果需要在程序中自行引发异常，则应使用 raise 语句，该语句的基本语法格式为：
#
#   raise [exceptionName [(reason)]]
#
# 其中，用 [] 括起来的为可选参数，其作用是指定抛出的异常名称，以及异常信息的相关描述。如果可选参数全部省略，则 raise 会把当前错误原样抛出；如果仅省略 (reason)，则在抛出异常时，将
# 不附带任何的异常描述信息。
#
# 也就是说，raise 语句有如下三种常用的用法：
#
#   raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。
#   raise 异常类名称：raise 后带一个异常类名称。该语句引发指定异常类的默认实例。
#   raise 异常类名称(描述信息)：在引发指定异常的同时，附带异常的描述信息。
#
# 上面三种用法最终都是要引发一个异常实例（即使指定的是异常类，实际上也是引发该类的默认实例），raise 语句每次只能引发一个异常实例。
#
# 注意，即使是用户自行引发的异常，也可以使用 try except 来捕获它。当然也可以不管它，让该异常向上（先调用者）传播，如果该异常传到 Python 解释器，那么程序就会中止。
def main():
    try:
        # 使用try...except来捕捉异常
        # 此时即使程序出现异常，也不会传播给main函数
        mtd(3)
    except Exception as e:
        print('程序出现异常:', e)
    # 不使用try...except捕捉异常，异常会传播出来导致程序中止
    # mtd(3)


def mtd(a):
    if a > 0:
        raise ValueError("a的值大于0，不符合要求")


# 从上面程序可以看到，程序既可在调用 mtd(3) 时使用 try except 来捕获异常，这样该异常将会被 except 块捕获；也可直接调用 mtd(3)，这样该函数的异常就会直接导致程序中止。
#
# 上面第一行输出是第一次调用 mtd (3) 的结果，该方法引发的异常被 except 块捕获并处理。后面的大段输出则是第二次调用 mtd(3) 的结果，由于该异常没有被 except 块捕获，导致程序中止。
#
# 第二次调用 mtd(3) 引发的以“File”开头的三行输出，其实显示的就是异常的传播轨迹信息。也就是说，如果程序不对异常进行处理，Python 默认会在控制台输出异常的传播轨迹信息。
main()


# raise 不需要参数
#
# 正如前面所看到的，在使用 raise 语句时可以不带参数，此时 raise 语句处于 except 块中，它将会自动引发当前上下文激活的异常；否则，通常默认引发 RuntimeError 异常。
class AuctionException(Exception):
    pass


class AuctionTest:
    def __init__(self, init_price):
        self.init_price = init_price

    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            # 此处只是简单地打印异常信息
            print("转换出异常：", e)
            # 再次引发自定义异常
            raise AuctionException("竞拍价必须是数值，不能包含其他字符！")  # ①
            # raise AuctionException(e)
        if self.init_price > d:
            raise AuctionException("竞拍价比起拍价低，不允许竞拍！")
        initPrice = d


def main():
    at = AuctionTest(20.4)
    try:
        at.bid("df")
    except AuctionException as ae:
        # 再次捕获到bid()方法中的异常，并对该异常进行处理
        print('main函数捕捉的异常：', ae)


# 从输出结果来看，此时 main() 函数再次捕获了 ValueError，它就是在 bid() 方法中 except 块所捕获的原始异常。
main()

# except 和 raise 同时使用
#
# 在实际应用中对异常可能需要更复杂的处理方式。当一个异常出现时，单靠某个方法无法完全处理该异常，必须由几个方法协作才可完全处理该异常。也就是说，在异常出现的
# 当前方法中，程序只对异常进行部分处理，还有些处理需要在该方法的调用者中才能完成，所以应该再次引发异常，让该方法的调用者也能捕获到异常。
#
# 为了实现这种通过多个方法协作处理同一个异常的情形，可以在 except 块中结合 raise 语句来完成。如下程序示范了except 和 raise 同时使用的方法：
#
# 自定义异常类
#
# 很多时候，程序可选择引发自定义异常，因为异常的类名通常也包含了该异常的有用信息。所以在引发异常时，应该选择合适的异常类，从而可以明确地描述该异常情况。在这种情
# 形下，应用程序常常需要引发自定义异常。
#
# 用户自定义异常都应该继承 Exception 基类或 Exception 的子类，在自定义异常类时基本不需要书写更多的代码，只要指定自定义异常类的父类即可。
#
# 下面程序创建了一个自定义异常类：
#
#   class AuctionException(Exception):
#         pass
#
# 上面程序创建了 AuctionException 异常类，该异常类不需要类体定义，因此使用 pass 语句作为占位符即可。
#
# 在大部分情况下，创建自定义异常类都可采用与上面程序相似的代码来完成，只需改变 AuctionException 异常的类名即可，让该异常的类名可以准确地描述该异常。
