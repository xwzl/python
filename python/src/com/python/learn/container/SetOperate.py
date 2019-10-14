import time

# Python set 集合最常用的操作是向集合中添加元素、删除元素，以及集合之间做交集，并集、差集等运算。
#
# 向 set 集合中添加元素
#
# set 集合中添加元素，可以使用 set 类型提供的 add() 方法实现，该方法的语法格式为：
#
#   setName.add(element)
#
# 其中，setName 表示要添加元素的集合，element 表示要添加的元素内容。
#
# 需要注意的是，使用 add() 方法添加的元素，只能是数字、字符串、元组或者布尔类型（True 和 False）值，不能添加列表、字典、集
# 合这类可变的数据，否则 Python 解释器会报 TypeError 错误

a = {1, 2, 3}
a.add((1, 2))
print(a)
# a.add([1, 2])
# print(a)

dicts = {"java": 1, "go": 2}
print("java" not in dicts)

# 上面程序中，由于集合中的元素 1 已被删除，因此当再次尝试使用 remove() 方法删除时，会引发 KeyError 错误。
#
# 如果我们不想在删除失败时令解释器提示 KeyError 错误，还可以使用 discard() 方法，此方法和 remove() 方法的用法完全相同，唯一的
# 区别就是，当删除集合中元素失败时，此方法不会抛出任何错误。
print("set 删除元素有两个方法，一个是 remove 方法，如果元素不在集合集中报错， 相反的是 discard() 删除元素，元素不存不会报错")
numberSet = {1, 2, 3, 4, 5, 6, 7}
numberSet.discard(2)
numberSet.discard(2)
# numberSet.remove(2) # 元素不存报错


# Python set集合做交集、并集、差集运算
#
# 集合最常做的操作就是进行交集、并集、差集以及对称差集运算
# 交集 & 并集 | 差集 - 对称差集 ^
dataSet = {1, 3, 5}
dataSet1 = {5, 7, 9}
print(dataSet & dataSet1)  # 交集 5
print(dataSet1 | dataSet)  # 交集 1 3 5 7 9
print(dataSet - dataSet1)  # 差集 1 3
print(dataSet1 - dataSet)  # 差集 1 3
print(dataSet ^ dataSet1)  # 对称差集

print("\nset 常用方法\n")
# add 方法
dataSet2 = {1, 2}
dataSet2.add(3)
print("dataSet2:", dataSet2)

dataSet2.clear()
print("dataSet2元素 已清空", dataSet2)

dataSet2 = {1, 2, 3}
dataSet3 = {3, 4, 5}
diff = dataSet2.difference(dataSet3)
print("difference 方法 dataSet2 中有而 dataSet3 没有的元素复制给 diff:", diff)
dataSet2.difference_update(dataSet3)
print("difference_update 方法删除 dataSet2 与 dataSet3 相同的元素：", dataSet2)

dataSet2.discard(2)  # 删除元素 2，不存在也不报错
dataSet2 = {1, 2, 3}

intersection = dataSet2.intersection(dataSet3)
print("intersection 方法把 dataSet2 与 dataSet3 相同的元素赋值给 intersection：", intersection)

dataSet2.intersection_update(dataSet3)
print("intersection_update 方法把 dataSet2 与 dataSet3 相同的元素赋值给 dataSet2:", dataSet2)

dataSet2 = {1, 2, 3}

print("判断是否有交集", dataSet2.isdisjoint(dataSet3))

dataSet4 = {1, 2}
print("判断是否是子集：", dataSet4.issubset(dataSet2))  # True

print("判断是否是父集：", dataSet4.issuperset(dataSet2))  # False

print("排除相同的元素，并返回", dataSet2.symmetric_difference(dataSet3))

dataSet2.symmetric_difference_update(dataSet3)

print("删除相同的元素并赋值 dataSet2", dataSet2)
dataSet2 = {1, 2, 3}

print("union 并集：", dataSet2.union(dataSet3))

updateSet = {1, 2}
print(", update 用于将列表或者集合中元素添加到 set 集合中")
updateSet.update([1, 2, 3, 4])
print(updateSet)

# frozenset 是 set 的不可变版本，因此 set 集合中所有能改变集合本身的方法（如 add、remove、discard、xxx_update 等），frozenset 都不支持；
# set 集合中不改变集合本身的方法，fronzenset 都支持。
#
# 在交互式解释器中输入 dir(frozenset) 命令来查看 frozenset 集合的全部方法，可以看到如下输出结果：
#
#   >>> dir(frozenset)
#   ['copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
#
# 很明显，frozenset 的这些方法和 set 集合同名方法的功能完全相同。
#
# frozenset 的作用主要有两点：
#
#   当集合元素不需要改变时，使用 frozenset 代替 set 更安全。
#   当某些 API 需要不可变对象时，必须用 frozenset 代替set。比如 dict 的 key 必须是不可变对象，因此只能用 frozenset；再比如 set 本身的集合元
#   素必须是不可变的，因此 set 不能包含 set，set 只能包含 frozenset。

s = set()
# 创建 frozenset 不可变集合，使用 frozenset() 函数
frozen_s = frozenset('Kotlin')
# 为set集合添加frozenset
s.add(frozen_s)
print('s集合的元素：', s)
sub_s = {'Python'}


# 为set集合添加普通set集合，程序报错
# s.add(sub_s)

def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None


# 在上面程序的基础上，如果列表有 n 个元素，因为查找的过程需要遍历列表，那么最坏情况下的时间复杂度就为 O(n)。即使先对列表进行排序，再使
# 用二分查找算法，也需要 O(logn) 的时间复杂度，更何况列表的排序还需要 O(nLogN) 的时间。
#
# 但如果用字典来存储这些数据，那么查找就会非常便捷高效，只需 O(1) 的时间复杂度就可以完成，因为可以直接通过键的哈希值，找到其对应的值，而
# 不需要对字典做遍历操作，实现代码如下：
products = [
    (111, 100),
    (222, 30),
    (333, 150)
]
print('The price of product 222 is {}'.format(find_product_price(products, 222)))
print('The price of product 222 is {}'.format(products[222]))


# 统计时间需要用到 time 模块中的函数，了解即可


def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products:  # A
        if price not in unique_price_list:  # B
            unique_price_list.append(price)
    return len(unique_price_list)


ids = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(ids, price))
# 计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))


# 使用集合完成同样的工作
def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)


# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))
