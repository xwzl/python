# 有些时候，程序需要进行反向遍历，此时可通过 reversed() 函数，该函数可接收各种序列（元组、列表、区间等）参数，然后返回一
# 个“反序排列”的法代器，该函数对参数本身不会产生任何影响。
#
# 在交互式解释器中，测试该函数的过程如下：
rangeValue = range(1, 10)
for value in reversed(rangeValue):
    print(value)

print([x for x in reversed(rangeValue)])

# sorted() 函数与 reversed() 函数类似，该函数接收一个可迭代对象作为参数，返回一个对元素排序的列表。
a = [20, 30, -1.2, 3.5, 90, 3.6]
print(sorted(a))
# 从上面的运行过程来看，sorted() 函数也不会改变所传入的可迭代对象，该函数只是返回一个新的、排序好的列表。
#
# 在使用 sorted() 函数时，还可传入一个 reverse 参数，如果将该参数设置为 True，则表示反向排序
print(sorted(a, reverse=True))
# 通过 sorted() 函数的帮助，程序可对可迭代对象按照由小到大的顺序进行遍历。
my_list = ['fKit', 'crazyIt', 'Charlie', 'fox', 'Emily']
for s in sorted(my_list, key=len):
    print(s)
