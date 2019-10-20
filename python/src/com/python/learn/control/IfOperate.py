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


