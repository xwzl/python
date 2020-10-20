# 内存地址
# 字符串 元祖 数字 为不可变对象

import random

x, y = int(100000), int(100000)
m, n = "10", "10"
print("x memory address: %d,y memory address: %d" % (id(x), id(y)))
print("m memory address: %d,n memory address: %d" % (id(m), id(n)))

m = "11"
n = "12"
print("m memory address: %d,n memory address: %d" % (id(m), id(n)))

choice = random.choice("12346")
print(choice)

# 直接从列表中返回数据
subjects = ["语文", "数学", "英语"]
print(random.choice(subjects))
