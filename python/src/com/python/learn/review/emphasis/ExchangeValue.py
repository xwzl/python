# python 中特有写法，交互数据
import json

x, y = 100, 200

t = x
x = y
y = t

x, y = y, x
print("x value {} , y value {}".format(x, y))

students = ["张三", "李四", "王五"]
dumps = json.dumps(students)  # list 转 json 字符串
print(dumps)

loads = json.loads(dumps)  # json 字符串转 list
print(type(loads))

# python 中执行代码
eval("print(\"hello python\")")

