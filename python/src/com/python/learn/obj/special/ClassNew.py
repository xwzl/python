# __new__() 是一种负责创建类实例的静态方法，它无需使用 staticmethod 装饰器修饰，且该方法会优先 __init__() 初始化方法被调用。
#
# 一般情况下，覆写 __new__() 的实现将会使用合适的参数调用其超类的 super().__new__()，并在返回之前修改实例。
class DemoClass:
    instances_created = 0

    # __new__() 通常会返回该类的一个实例，但有时也可能会返回其他类的实例，如果发生了这种情况，则会跳过对 __init__() 方法的调用。
    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)
        # 调用父类的方法创建实例
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        # 类成员变量，相当于静态变量
        cls.instances_created += 1
        return instance

    # init 先于 new 调用
    def __init__(self, attribute):
        print("__init__():", self, attribute)
        self.attribute = attribute


test1 = DemoClass("abc")
test2 = DemoClass("xyz")
print(test1.number, test1.instances_created)
print(test2.number, test2.instances_created)
print(DemoClass.instances_created)


# __new__() 通常会返回该类的一个实例，但有时也可能会返回其他类的实例，如果发生了这种情况，则会跳过对 __init__() 方法的调用。
# 而在某些情况下（比如需要修改不可变类实例（Python 的某些内置类型）的创建行为），利用这一点会事半功倍。
class NonZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None

    def __init__(self, skipped_value):
        # 此例中会跳过此方法
        print("__init__()")
        super().__init__()


print(type(NonZero(-12)))
print(type(NonZero(0)))

# 那么，什么情况下使用 __new__() 呢？答案很简单，在 __init__() 不够用的时候。
#
# 例如，前面例子中对 Python 不可变的内置类型（如 int、str、float 等）进行了子类化，这是因为一旦创建了这样不可变的对象实例，就无法在 __init__() 方法中对其进行修改。
#
# 有些读者可能会认为，__new__() 对执行重要的对象初始化很有用，如果用户忘记使用 super()，可能会漏掉这一初始化。虽然这听上去很合理，但有一个主要的缺点，即如果使用这样的方
# 法，那么即便初始化过程已经是预期的行为，程序员明确跳过初始化步骤也会变得更加困难。不仅如此，它还破坏了“__init__() 中执行所有初始化工作”的潜规则。
#
# 注意，由于 __new__() 不限于返回同一个类的实例，所以很容易被滥用，不负责任地使用这种方法可能会对代码有害，所以要谨慎使用。一般来说，对于特定问题，最好搜索其他可用的解决方
# 案，最好不要影响对象的创建过程，使其违背程序员的预期。比如说，前面提到的覆写不可变类型初始化的例子，完全可以用工厂方法（一种设计模式）来替代。
#
# Python中大量使用 __new__() 方法且合理的，就是 MetaClass 元类
