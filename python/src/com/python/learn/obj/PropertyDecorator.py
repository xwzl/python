# 既要保护类的封装特性，又要让开发者可以使用“对象.属性”的方式操作操作类属性，除了使用 property() 函数，Python 还提供了 @property 装饰器。
# 通过 @property 装饰器，可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号。
#
# @property 的语法格式如下：
#
#   @property
#   def 方法名(self)
#        代码块
#
# 而要想实现修改 area 属性的值，还需要为 area 属性添加 setter 方法，就需要用到 setter 装饰器，它的语法格式如下：
#
#   @方法名.setter
#   def 方法名(self, value):
#        代码块
#
# 除此之外，还可以使用 deleter 装饰器来删除指定属性，其语法格式为：
#
#   @方法名.deleter
#   def 方法名(self):
#        代码块
#
# 例如，定义一个矩形类，并定义用 @property 修饰的方法操作类中的 area 私有属性
class Rect:
    def __init__(self, area):
        self.__area = area
        self.qq = "腾讯"

    # 使用 ＠property 修饰了 area() 方法，这样就使得该方法变成了 area 属性的 getter 方法。需要注意的是，如果类中只包含该方法，那么 area 属性将是一个只读属性
    @property
    def area(self):
        return self.__area

    # 而要想实现修改 area 属性的值，还需要为 area 属性添加 setter 方法，就需要用到 setter 装饰器
    # 这样，area 属性就有了 getter 和 setter 方法，该属性就变成了具有读写功能的属性。
    @area.setter
    def area(self, area):
        self.__area = area

    @area.deleter
    def area(self):
        self.__area = 0


rect = Rect("成都")
print(rect.area)
rect.qq = 10
rect.area = 11
print(rect.area)
print(rect.qq)

del rect.area
print("删除后的area值为：", rect.area)


