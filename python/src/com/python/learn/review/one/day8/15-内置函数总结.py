print(any(['hello', '', 'yes']))
print(any(['', 0]))  # 任意一个为 False 就是 False
print(all(['', 0]))  # 全部为 True 才是 True

nums = [1, 2, 3]
print(dir(nums))

print(dir('hello'))

exit(100)  # 推出程序

shang, yushu = divmod(15, 2)


def test():
    """
    这是一个函数
    :return:
    """
    return 0


help(test)
