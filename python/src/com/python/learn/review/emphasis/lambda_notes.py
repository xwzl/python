from functools import reduce


def say():
    print("给函数起一个别名")


say_plus = say  # 给函数其别名

say_plus()

# 大多数不这样调用 lambda 表达式，一般用来当参数传递
add_lambda = lambda x, y: x + y

print(add_lambda(1, 1))


def lambda_method(x, y, do_operate):
    return do_operate(x, y)


print(lambda_method(11, 13, lambda param1, param2: (param1 + param2) * (param1 - 1)))

# 有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 2, 1, 7, 6]

# 列表的sort方法，会直接对列表进行排序
# nums.sort()
# print(nums)


ints = (5, 9, 2, 1, 3, 8, 7, 4)
# sorted内置函数，不会改变原有的数据，而是生成一个新的有序的列表
x = sorted(ints)
print(x)

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 172}
]

# 字典和字典之间不能使用比较运算 <
# students.sort()

# foo() takes 0 positional arguments but 1 was given
# foo这个函数需要 0 个位置参数，但是在调用的时候传递了一个参数
# def foo(ele):
#     # print("ele = {}".format(ele))
#     return ele['height']  # 通过返回值告诉sort方法，按照元素的那个属性进行排序


# 需要传递参数 key 指定比较规则
# key参数类型是函数

# 在sort内部实现的时候，调用了foo方法，并且传入了一个参数，参数就是列表里的元素
# students.sort(key=foo)

students.sort(key=lambda ele: ele['score'])
print(students)

lists = [111, 12, 4, 5, 465, 14, 134, 34, 1234, 12, 4, 125, 123, 5]

# 对于 filter 或者 sort 内置函数来说，返回的是新数据
result = filter(lambda x1: x1 & 1 == 0, lists)
# filter 返回的是一个可迭代对象
print(list(result))

lists.sort(key=lambda x1: x1)
print(lists)

# reduce 函数
# 类似与 x1 + y1 的值赋值给 x1,然后再次执行该方法
# x,i = 0,0
# while i < len(lists)-1:
#       x = lists[i]+lists[i+1]
#       i +=1
print(reduce(lambda x1, y1: x1 + y1, lists))

# initial 给第一个位置参数赋予初始值
# 因为 p = p['age'] + q['age'] 计算一轮后，p 从 map 转化为 type 会报错
# 如果我们假定 p 初始值为 0， q 会从第一个 key 取值
print(reduce(lambda p, q: p + q['age'], students, 0))
