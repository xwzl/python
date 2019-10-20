# zip() 函数可以把两个列表“压缩”成一个 zip 对象（可迭代对象），这样就可以使用一个循环并行遍历两个列表。为了测试 zip() 函数的功能，我们可以先
# 在交互式解释器中“试验”一下该函数的功能。
x = [1, 2, 3]
y = ['x', 'y', 'z']
# 如果 zip() 函数压缩的两个列表长度不相等，那么 zip() 函数将以长度更短的列表为准。
print([x for x in zip(x, y)])
print(zip(x, y))

# 从上面的测试结果来看，zip() 函数压缩得到的可迭代对象所包含的元素是由原列表元素组成的元组。
#
# Python 2.x 的 zip() 函数直接返回列表，而不是返回 zip 对象。Python 2.x 的 zip() 函数返回的列表所包含的元素和 Python 3.x 的 zip() 返回的 zip 对象所包含的元素相同。

books = ['疯狂Kotlin讲义', '疯狂Swift讲义', '疯狂Python讲义']
prices = [79, 69, 89]
# 使用zip()函数压缩两个列表，从而实现并行遍历
for book, price in zip(books, prices):
    print("%s的价格是: %5.2f" % (book, price))
