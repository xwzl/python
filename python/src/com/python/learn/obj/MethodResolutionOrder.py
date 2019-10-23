# 我们知道，Python 类是支持（多）继承的，一个类的方法和属性可能定义在当前类，也可能定义在基类。针对这种情况，当调用类方法或类属性时，就需要对当前类以及它的基类进行搜索，以确定方法或属性
# 的位置，而搜索的顺序就称为方法解析顺序。
#
# 方法解析顺序（Method Resolution Order），简称 MRO。对于只支持单继承的编程语言来说，MRO 很简单，就是从当前类开始，逐个搜索它的父类；而对于 Python，它支持多继承，MRO 相对会复杂一些。
#
# 实际上，Python 发展至今，经历了以下 3 种 MRO 算法，分别是：
#
#   从左往右，采用深度优先搜索（DFS）的算法，称为旧式类的 MRO；
#   自 Python 2.2 版本开始，新式类在采用深度优先搜索算法的基础上，对其做了优化；
#   自 Python 2.3 版本，对新式类采用了 C3 算法。由于 Python 3.x 仅支持新式类，所以该版本只使用 C3 算法。
#
# 有读者可能会好奇，为什么 MRO 弃用了前两种算法，而选择最终的 C3 算法呢？原因很简单，前 2 种算法都存在一定的问题。

# 旧式类MRO算法
# 在使用旧式类的 MRO 算法时，以下面代码为例（程序一）:
# class A:
#     def method(self):
#         print("CommonA")
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     def method(self):
#         print("CommonC")
#
#
# class D(B, C):
#     pass


# 通过分析可以想到，此程序中的 4 个类是一个“菱形”继承的关系，当使用 D 类对象访问 method() 方法时，根据深度优先算法，搜索顺序为 D->B->A->C->A。
#
# 旧式类的 MRO 可通过使用 inspect 模块中的 getmro(类名) 函数直接获取。例如 inspect.getmro(D) 表示获取 D 类的 MRO。
#
# 因此，使用旧式类的 MRO 算法最先搜索得到的是基类 A 中的 method() 方法，即在 Python 2.x 版本中，此程序的运行结果为：
#
#   CommonA
#
# 但是，这个结果显然不是想要的，我们希望搜索到的是 C 类中的 method() 方法。
print(D().method())


# 新式类MRO算法
#
# 为解决旧式类 MRO 算法存在的问题，Python 2.2 版本推出了新的计算新式类 MRO 的方法，它仍然采用从左至右的深度优先遍历，但是如果遍历中出现重复的类，只保留最后一个。
#
# 仍以上面程序为例，通过深度优先遍历，其搜索顺序为 D->B->A->C->A，由于此顺序中有 2 个 A，因此仅保留后一个，简化后得到最终的搜索顺序为 D->B->C->A。
# 新式类可以直接通过 类名.__mro__ 的方式获取类的 MRO，也可以通过 类名.mro() 的形式，旧式类是没有 __mro__ 属性和 mro() 方法的。
#
# 可以看到，这种 MRO 方式已经能够解决“菱形”继承的问题，但是可能会违反单调性原则。所谓单调性原则，是指在类存在多继承时，子类不能改变基类的 MRO 搜索顺序，否则会导致程序发生异常。
class X(object):
    pass


class Y(object):
    pass


class A(X, Y):
    pass


class B(Y, X):
    pass


class C(A, B):
    pass
# 通过进行深度遍历，得到搜索顺序为 C->A->X->object->Y->object->B->Y->object->X->object，再进行简化（相同取后者），得到 C->A->B->Y->X->object。
#
# 下面来分析这样的搜索顺序是否合理，我们来看下各个类中的 MRO：
#
#   对于 A，其搜索顺序为 A->X->Y->object；
#   对于 B，其搜索顺序为 B->Y->X->object；
#   对于 C，其搜索顺序为 C->A->B->X->Y->object。
#
# 可以看到，B 和 C 中，X、Y 的搜索顺序是相反的，也就是说，当 B 被继承时，它本身的搜索顺序发生了改变，这违反了单调性原则。


# MRO C3
#
# 为解决 Python 2.2 中 MRO 所存在的问题，Python 2.3 采用了 C3 方法来确定方法解析顺序。多数情况下，如果某人提到 Python 中的 MRO，指的都是 C3 算法。
#
# 在 Python 2.3 及后续版本中，运行程序一，得到如下结果：
#
#   CommonC
#
# 运行程序二，会产生如下异常：
#
#    Traceback (most recent call last):
#       File "C:\Users\mengma\Desktop\demo.py", line 9, in <module>
#       class C(A, B):
#    TypeError: Cannot create a consistent method resolution
#       order (MRO) for bases X, Y
#
# 由此可见，C3 可以有效解决前面 2 种算法的问题。那么，C3 算法是怎样实现的呢？
#
# 以程序一为主，C3 把各个类的 MRO 记为如下等式：
#
#   类 A：L[A] = merge(A , object)
#   类 B：L[B] = [B] + merge(L[A] , [A])
#   类 C：L[C] = [C] + merge(L[A] , [A])
#   类 D：L[D] = [D] + merge(L[A] , L[B] , [A] , [B])
#
# 注意，以类 A 等式为例，其中 merge 包含的 A 称为 L[A] 的头，剩余元素（这里仅有一个 object）称为尾。
#
# 这里的关键在于 merge，它的运算方式如下：
#
#   检查第一个列表的头元素（如 L[A] 的头），记作 H。
#
# 若 H 未出现在 merge 中其它列表的尾部，则将其输出，并将其从所有列表中删除，然后回到步骤 1；否则，取出下一个列表的头部记作
