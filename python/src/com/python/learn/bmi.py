height = float(input("输入身高："))  # 输入身高
weight = float(input("输入体重："))  # 输入体重
bmi = weight / (height * height)  # 计算BMI指数
# 判断身材是否合理
if bmi < 18.5:
    # 下面 2 行同属于 if 分支语句中包含的代码，因此属于同一作用域
    print("BMI指数为：" + str(bmi))  # 输出BMI指数
    print("体重过轻")
if 18.5 <= bmi < 24.9:
    print("BMI指数为：" + str(bmi))  # 输出BMI指数
    print("正常范围，注意保持")
if 24.9 <= bmi < 29.9:
    print("BMI指数为：" + str(bmi))  # 输出BMI指数
    print("体重过重")
if bmi >= 29.9:
    print("BMI指数为：" + str(bmi))  # 输出BMI指数
    print("肥胖")
