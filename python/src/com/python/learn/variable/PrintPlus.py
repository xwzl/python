# 同时输出多个变量和字符串，指定分隔符
user_name = "张三"
user_age = 15
print("读者名：", user_name, "年龄：", user_age)

# 从输出结果来看，使用 print() 函数输出多个变量时，print() 函数默认以空格隔开多个变量，如果读者希望改变默认的分隔符，可通过 sep 参数进行设置。
print("读者名：", user_name, "年龄：", user_age, sep='|')

# 在默认情况下，print() 函数输出之后总会换行，这是因为 print() 函数的 end 参数的默认值是“\n”，这个“\n”就代表了换行。如果希望 print() 函数输出
# 之后不会换行，则重设 end 参数即可
# 但由于它们都指定了 end＝""，因此每条 print() 语句的输出都不会换行，依然位于同一行。
print(40, "\t", end="")
print(50, "\t", end="")
print(60, "\t", end="")

# file 参数指定 print() 函数的输出目标，file 参数的默认值为 sys.stdout，该默认值代表了系统标准输出，也就是屏幕，因此 print() 函数默认输出到屏幕。
# 实际上，完全可以通过改变该参数让 print() 函数输出到特定文件中，
f = open("demo.txt", "w")  # 打开文件以便写入
print('沧海月明珠有泪'.encode("utf-8").decode(), file=f)
print('蓝回日暖玉生烟', file=f)
f.close()
