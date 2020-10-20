# 内存地址

# 字符串 元祖 数字 为不可变对象
x, y = int(100000), int(100000)
m, n = "10", "10"
print("x memory address: %d,y memory address: %d" % (id(x), id(y)))
print("m memory address: %d,n memory address: %d" % (id(m), id(n)))

m = "11"
n = "12"
print("m memory address: %d,n memory address: %d" % (id(m), id(n)))
