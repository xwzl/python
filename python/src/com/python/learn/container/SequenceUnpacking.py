x1, y1 = (11, 22)
print(x1, y1)

x2, y2 = {1, 2}
print(x2, y2)

x3, y3 = [1, 2]
print(x3, y3)

# 字典的序列解包有点特殊
x4, y4 = {"x4": 12, "y4": 12}.values()
print(x4, y4)
