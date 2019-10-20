# 如果程序需要有多个返回值，则既可将多个值包装成列表之后返回，也可直接返回多个值。如果 Python 函数直接返回多个值，Python 会自动将多个返回值封装成元组。
def multipleReturnValues(lists):
    count = 0
    sums = 0
    for value in lists:
        if isinstance(value, int) or isinstance(value, float):
            sums += value
            count += 1
    return sums, sums / count


five = {"12", "13", 12, 333, 112, 12, 313, 31, 3, 121, 12.2}
values = multipleReturnValues(five)

print(values)

total, average = values
print(total, average)
