# python 中的装饰器,类似于 AOP,动态代理，cglib
# 1. 定义个原始函数 demo
# 2. 定义一个装饰器方法 decorator_func,定义内部方法并且返回，作为装饰 demo 方法的载体
# 3. 在原始函数 demo 上声明 @decorator_func,声明 demo 函数为被装饰器修饰
# 4. demo 函数被当作入参 func 传入 decorator 方法，由于 inner 函数中有特定的 func 方法增强
# 5. 由于闭包的特性，执行 demo 方法最终会执行被装饰器增强的方法逻辑
import time


# 相当于 aop 和 cglib
def decorator_func(func):
    print("增强 {} 方法".format(func))

    # 增强外部函数 func
    def inner():
        # 被装饰期间函数并不会被执行，最终执行 demo 方法的时候才会被执行
        start = time.time()
        func()  # 这里是最终执行方法的地方
        print("方法耗时{}".format(time.time() - start))

    return inner


@decorator_func
def demo():
    print("主程序将睡眠三秒钟")
    time.sleep(3)


# demo()=decorator_func(demo)
demo()  # 调用的是 decorator_func 增强后方法,其实就是 inner() 方法
