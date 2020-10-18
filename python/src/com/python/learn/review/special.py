# 元组赋值
print(type({}))  # 空字典
print(type(set()))  # 空集合
x = 11, 12
print(type(x))  # 元组类型
x, y = 11, 13
print(type(x))  # 元祖拆包

# x, y, z = 1, 2, 3, 4, 5, 6, 7, 8 报错
# 对于中拆包，* 表示参数为可变参数，自动封装为列表对象
x, *y1, z = 1, 2, 3, 4, 5, 6, 7, 8
print(x, y1, z)

# 逻辑运算符
a, b = 10, 12

if a > 9 and b < 13:
    print("and  &")

if a > 9 or b < 13:
    print("and  &")

if a > 10 & b < 12:
    print("and  &")

if a > 9 | b < 13:
    print("and  &")


def bool_false():
    print("print False")
    return False


def bool_true():
    print("print True")
    return True


if bool_false() and bool_true():
    print("第一个判断为 False,不会执行第二个判断")

if bool_true() and bool_false():
    print("第一个判断为 False,不会执行第二个判断")

if bool_true() or bool_false():
    print("第一个判断为 False,不会执行第二个判断")

if bool_false() or bool_true():
    print("第一个判断为 False,不会执行第二个判断")

# not 取反
print(not (2 > 3))

# 逻辑运算的优先级:  not > and > or
print(True or False and True)  # True and True ==> True
print(False or not False)  # False or True ==> True
print(True or True and False)  # True or True ==> True

# 强烈建议:在开发中，使用括号来说明运算符的优先级
print(True or True and False)  # True
print(True or (True and False))

# 逻辑运算符规则:
# 逻辑与运算:
# 只要有一个运算数是False,结果就是False;只有所有的运算数都是True,结果才是True
# 短路:只要遇到了False,就停止，不再继续执行了
# 取值:取第一个为False,如果所有的运算数都是True,取最后一个运算数


# 逻辑或运算:
# 只要有一个运算数是True,结果就是True;只有所有的运算数都是False,结果才是False
# 短路:只要遇到了True,就停止，不再继续执行了
# 取值:取第一个为True的值，如果所有的运算数都是False,取最后一个运算数


# python 里面不支持 switch case 语句

age = input("请输入你的年龄:")
# age = int(input("请输入你的年龄:"))
age = int(age)
if age < 0:
    print("年龄参数违法")
elif age > 18:
    print("恭喜你，成功注册账号")
else:
    print("未成年人不允许玩游戏")
