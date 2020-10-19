# 源码解读

# 输入字串， [，表示可选参数
# S.find(sub[, start[, end]]) -> int
print("hello python".find("pt", 4))

# 默认补齐空格
print("字符拆补齐".ljust(10, "+"))
print("center".center(20, "-"))
print("    strip       ".strip())
print("    strip       ".rstrip())

# join(iterable)
name_list = ["mike", "tom", "jack", "sun"]
print("-".join(name_list))
print("+".join({"x": "1", "y": 2}))

print("How are you".split(" "))

print(oct(10))
print(bin(97))
print(hex(55))

encode = "👌".encode("utf8")
print(encode)
print(encode.decode("utf8"))
