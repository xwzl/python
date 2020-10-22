import random
import time


def fix(func):
    def strong(x, *args, **kwargs):
        print("简单打印一下入参", x)

        start = time.time()
        # kwargs["time"] 没有传 time 参数会报错
        current_time = kwargs.get("time", 13)
        if current_time > 12:
            result = func(x)
            return result, time.time() - start
        else:
            return 0, time.time() - start

    return strong


@fix
def pay_amount(money, *args, **kwargs):
    time.sleep(random.random() * 10)
    return money * (money - 1)


# 装饰器使用场景，无缝增强原有方法
print(pay_amount(10, time=10))
print(pay_amount(12))
