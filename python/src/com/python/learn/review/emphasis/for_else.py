for i in range(1, 10):
    if i == 10:
        break
    print("for 循环的打印", i)
else:
    print("break 未执行，将会执行这一行代码")

value = "abcdefghijkmnopqrstuvwzxy"

print(value[-1:3])

# 与 java 一样,字符串为不可变序列
# value[1] = 1

# 切片就是从字符串里复制一段指定的内容，生成一个新的字符串
m = 'abcdefghijklmnopqrstuvwxyz'
print(m[6])  # m[index] ==> 获取指定下标上的数据

# 切片语法  m[start:end:step]
# 包含start,不包含end
# step 指的是步长,理解为间隔。每隔 step-1 个取一次
# step 为负数，表示从右往左获取

print(m[2:9])  # 包含start,不包含end
print(m[2:])  # 如果只设置了start,会"截取"到最后
print(m[:9])  # 如果值设置了end,会从头开始"截取"

# 步长默认为 1
print(m[3:15:2])  # dfhjln
print(m[3:15:1])  # defghijklmno
# print(m[3:15:0])  # 步长不能为0
print('------------------')
# print(m[3:15:-1])  # 没有数据
print(m[15:3:-1])  # ponmlkjihgfe
print(m[::])  # abcdefghijklmnopqrstuvwxyz 从头到尾复制
print(m[::-1])  # zyxwvutsrqponmlkjihgfedcba

# start和end如果是负数，表示从右边数
print(m[-9:-5])  # rstu])
print(value[-12:-2])
