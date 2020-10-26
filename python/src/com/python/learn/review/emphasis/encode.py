# ASCII (8 bit  0 - 127) -> Latin1(ISO-8859-1 8 位 0-255) --> Unicode 编码
# 使用内置函数 chr 和 ord 能够查看数字和字符的对应关系
print(ord('a'))
print(chr(97))


# def is_number(value):

def is_str(value):
    return "This is str" if type(value) is str else "This is not str"


print(is_str("value"))
