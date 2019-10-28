# 在某些情况下，一个类的对象是有限且固定的，比如季节类，它只有 4 个对象；再比如行星类，目前只有 8 个对象。这种实例有限且固定的类，在 Python 中被称为枚举类。
#
# 程序有两种方式来定义枚举类：
#
#   直接使用 Enum 列出多个枚举值来创建枚举类。
#   通过继承 Enum 基类来派生枚举类。
#
# 如下程序示范了直接使用 Enum 列出多个枚举值来创建枚举类
import enum

# 定义Season枚举类
# 该构造方法的第一个参数是枚举类的类名；第二个参数是一个元组，用于列出所有枚举值。
Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))

# 在定义了上面的 Season 枚举类之后，程序可直接通过枚举值进行前问，这些枚举值都是该枚举的成员，每个成员都有 name、value 两个属性，其中 name 属性值为该枚举值的变量
# 名，value 代表该枚举值的序号# 直接访问指定枚举
print(Season.SPRING)
# 访问枚举成员的变量名
print(Season.SPRING.name)
# 访问枚举成员的值
print(Season.SPRING.value)

# 程序除可直接使用枚举之外，还可通过枚举变量名或枚举值来访问指定枚举对象。

# 根据枚举变量名访问枚举对象
print(Season['SUMMER'])  # Season.SUMMER
# 根据枚举值访问枚举对象
print(Season(3))  # Season.FALL

# 此外，Python 还为枚举提供了一个 __members__ 属性，该属性返回一个 dict 字典，字典包含了该枚举的所有枚举实例。程序可通过遍历 __members__ 属性来访问枚举的所有实例
# 遍历Season枚举的所有成员
for name, member in Season.__members__.items():
    print(name, '=>', member, ',', member.value)


# 如果要定义更复杂的枚举，则可通过继承 Enum 来派生枚举类，在这种方式下程序就可以为枚举额外定义方法了。
class Orientation(enum.Enum):
    # 为序列值指定value值
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'

    def info(self):
        print('这是一个代表方向【%s】的枚举' % self.value)


print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
# 通过枚举变量名访问枚举
print(Orientation['WEST'])
# 通过枚举值来访问枚举
print(Orientation('南'))
# 调用枚举的info()方法
Orientation.EAST.info()
# 遍历Orientation枚举的所有成员
for name, member in Orientation.__members__.items():
    print(name, '=>', member, ',', member.value)


# 枚举的构造器
#
# 枚举也是类，因此枚举也可以定义构造器。为枚举定义构造器之后，在定义枚举实例时必须为构造器参数设置值。
class Gender(enum.Enum):
    MALE = '男', '阳刚之力'
    FEMALE = '女', '柔顺之美'

    def __init__(self, cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc

    @property
    def desc(self):
        return self._desc

    @property
    def cn_name(self):
        return self._cn_name


# 访问FEMALE的name
print('FEMALE的name:', Gender.FEMALE.name)
# 访问FEMALE的value
print('FEMALE的value:', Gender.FEMALE.value)
# 访问自定义的cn_name属性
print('FEMALE的cn_name:', Gender.FEMALE.cn_name)
# 访问自定义的desc属性
print('FEMALE的desc:', Gender.FEMALE.desc)
