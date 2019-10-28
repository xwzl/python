# 多态
class Animal:
    def move(self, field):
        print("动物在%s" % field)


class Bird(Animal):
    def move(self, field):
        print('鸟在%s' % field)


class Dog(Animal):
    def move(self, field):
        print('狗在%s' % field)


a = Animal()
a.move("叫")
a = Bird()
a.move("飞")
a = Dog()
a.move("跑")


class Canvas:
    def draw_pic(self, shape):
        print('--开始绘图--')
        shape.draw(self)


class Rectangle:
    def draw(self, canvas):
        print('在%s上绘制矩形' % canvas)


class Triangle:
    def draw(self, canvas):
        print('在%s上绘制三角形' % canvas)


class Circle:
    def draw(self, canvas):
        print('在%s上绘制圆形' % canvas)


c = Canvas()
# 传入Rectangle参数，绘制矩形
c.draw_pic(Rectangle())
# 传入Triangle参数，绘制三角形
c.draw_pic(Triangle())
# 传入Circle参数，绘制圆形
c.draw_pic(Circle())
