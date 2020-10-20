# python 中特有写法，交互数据

x, y = 100, 200

t = x
x = y
y = t

x, y = y, x
print("x value {} , y value {}".format(x, y))
