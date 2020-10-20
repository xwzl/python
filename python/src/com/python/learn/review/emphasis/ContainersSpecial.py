# 列表推导式
values = [i for i in range(1, 10)]
print(values)  # 1,10 列表

# 不需要有冒号
values = [i for i in range(1, 10) if i % 2 == 0]
print(values)  # 偶数

# 生成一个元组列表,具体的数据为 （x,y） 规定的类型
values = [(x, y) for x in range(2, 5) for y in range(4, 10)]
print(values)

# 实现分组一个 list 里面的元素，比如 [1,2,3,....,100] 变成 [[1,2,3],[4,5,6].....]
m = [i for i in range(1, 100)]
n = [m[j:j + 3] for j in range(1, 100, 2)]
print(n)

map = {"age": 1, "name": 11}
print(map.get("hello"))
