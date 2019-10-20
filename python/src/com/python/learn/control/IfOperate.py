# if 表达式真假值的判断方法
#
# 从前面的示例可以看到，Python 执行 if 语句时，会判断 if 表达式的值是 True 还是 False 。那么是不是只能使用 bool 类型的表达式呢？
#
# 不是。表达式可以是任意类型，当下面的值作为 bool 表达式时，会被解释器当作 False 处理：
#
#   False、None、0、""、()、[]、{}
#
# 从上面介绍可以看出，除了 False 本身，各种代表“空”的 None、空字符串、空元组、空列表、空字典都会被当成 False 处理。
emptyList = []
print(type(emptyList))
if emptyList:
    print("这是一个空列表，不只是 False 可用于条件表达式")

# 很多程序都提供了“空语句”支持，Python 也不例外，Python 的 pass 语句就是空语句。
#
# 有时候程序需要占一个位、放一条语句，但又不希望这条语句做任何事情，此时就可通过 pass 语句来实现。通过使用 pass 语句，可以让程序更完整。
value = input("请输入一个整数：")
value = int(value)

if value > 15:
    # 空语句，相当于占位符
    pass
elif value < 10:  # else if 与 Java 中不一样，表示 el
    print("小于10")
else:
    print("10-15 之间")
