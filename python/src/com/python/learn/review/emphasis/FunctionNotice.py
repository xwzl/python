def position_function(x, y="1"):
    print("x is position param,y is key word param")
    print("key word param must be before position param")
    print("x value is :{},y value is:{}".format(x, y))


# position_function(y="222", "位置参数")
position_function("位置参数", y="222")

# 位置参数,可变参数,关键参数,可变关键参数 顺序依次书写
# python 中不允许方法重载,且同一个文件中全局变量不允许与方法名称相同
position_function = 11
