# 要理解 MetaClass 的底层原理，首先要深入理解 Python 类型模型。本节将从以下 2 点对 Python 类型模型做详细的介绍。
#
# 1. 所有的 Python 的用户定义类，都是 type 这个类的实例
#
# 事实上，类本身不过是一个名为 type 类的实例，可以通过如下代码进行验证：
class MyClass:
    pass


instance = MyClass()
print(type(instance))
print(type(MyClass))


# 用户自定义类，只不过是 type 类的 __call__ 运算符重载。
#
# 当定义完成一个类时，真正发生的情况是 Python 会调用 type 类的 __call__ 运算符。
class MyClass:
    data = 1


# Python 底层执行的是下面这段代码：
#
#   class = type(classname, superclasses, attributedict)
#
# 其中等号右边的 type(classname, superclasses, attributedict) 就是 type 的 __call__ 运算符重载，它会进一步调用下面这 2 个函数：
#
#   type.__new__(typeclass, classname, superclasses, attributedict)
#   type.__init__(class, classname, superclasses, attributedict)
instance = MyClass()
print(MyClass, instance)
print(instance.data)
MyClass = type('MyClass', (), {'data': 2})
instance = MyClass()
print(MyClass, instance)
print(instance.data)

# 由此可见，正常的 MyClass 定义，和手工调用 type 运算符的结果是完全一样的。
#
# 总之，正是 Python 的类创建机制，给了 metaclass 大展身手的机会，即一旦把一个类型 MyClass 设置成元类 MyMeta，那么它就不再由原生的 type 创建，而是会调用 MyMeta
# 的 __call__ 运算符重载：
#
#   class = type(classname, superclasses, attributedict)
#
# # 变为了
#
#   class = MyMeta(classname, superclasses, attributedict)
#
# 使用 metaclass 的风险
#
# 正如上面所看到的那样，metaclass 这样“逆天”的存在，会"扭曲变形"正常的 Python 类型模型，所以，如果使用不慎，对于整个代码库造成的风险是不可估量的。
#
# 换句话说，metaclass 仅仅是给小部分 Python 开发者，在开发框架层面的 Python 库时使用的。而在应用层，metaclass 往往不是很好的选择。

