class Student(object):

    def __init__(self, n) -> None:
        super().__init__()
        self.n = n
        self.count = 0

    # python 中类重写了 __iter__ 和 __next__ 方法,就可以当作一个可迭代对象
    # for x in class_instance 方法将调用 __iter__ 返回一个迭代器,然后调用
    # __next__ 方法获取迭代器中的下一个元素，迭代器中 raise StopIteration
    # 作为迭代器完结的标准
    def __iter__(self):
        return self

    # 迭代器的使用
    def __next__(self):
        self.count += 1
        if self.count < self.n:
            return self.count
        else:
            raise StopIteration

    # 生成器的使用
    @staticmethod
    def generation_use(index: int):
        result = 0
        num1 = 1
        num2 = 1
        while result < index:
            x = num1
            num1, num2 = num2, num1 + num2
            result += 1
            print(type(x))
            yield x


s = Student(10)

for value in s:
    print(value)

use = Student.generation_use(130)
for u in use:
    print(u)
