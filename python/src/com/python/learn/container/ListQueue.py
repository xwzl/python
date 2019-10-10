# 队列和栈是两种数据结构，其内部都是按照固定顺序来存放变量的，二者的区别在于对数据的存取顺序：
#
#   队列是，先存入的数据最先取出，即“先进先出”。
#   栈是，最后存入的数据最先取出，即“后进先出”。
#
# 考虑到 list 类型数据本身的存放就是有顺序的，而且内部元素又可以是各不相同的类型，非常适合用于队列和栈的实现。本节将演示如何使用 list 类型变量来实现队列和栈。
#
# Python list实现队列
#
# 使用 list 列表模拟队列功能的实现方法是，定义一个 list 变量，存入数据时使用 insert() 方法，设置其第一个参数为 0，即表示每次都从最前面插入数据；读取数据时，使
# 用 pop() 方法，即将队列的最后一个元素弹出。
#
# 如此 list 列表中数据的存取顺序就符合“先进先出”的特点。实现代码如下：

# 定义一个空列表，当做队列
from collections import deque

queue = []

# 向队列中插入元素
queue.insert(0, "1")
queue.insert(0, "2")
queue.insert(0, "3")
queue.insert(0, "4")

print(queue)
print("取出第一个元素", queue.pop())
print("取出第二个元素", queue.pop())
print("取出第三个元素", queue.pop())
print("取出第四个元素", queue.pop())

# Python list实现栈
#
# 使用 list 列表模拟栈功能的实现方法是，使用 append() 方法存入数据；使用 pop() 方法读取数据。
# append() 方法向 list 中存入数据时，每次都在最后面添加数据，这和前面程序中的 insert() 方法正好相反。
stack = []
stack.append("1")
stack.append("2")
stack.append("3")
stack.append("4")

print(stack)
print("取出倒数第一个元素", stack.pop())
print("取出倒数第二个元素", stack.pop())
print("取出倒数第三个元素", stack.pop())
print("取出倒数第四个元素", stack.pop())

# collections模块实现栈和队列
#
# 前面使用 list 实现队列的例子中，插入数据的部分是通过 insert() 方法实现的，这种方法效率并不高，因为每次从列表的开头插入一个数据，列表中所有元素都得向后移动一个位置。
#
# 这里介绍一个相对更高效的方法，即使用标准库的 collections 模块中的 deque 结构体，它被设计成在两端存入和读取都很快的特殊 list，可以用来实现栈和队列的功能。

queueAndStack = deque()
queueAndStack.append(1)
queueAndStack.append(2)
queueAndStack.append("hello")
print(list(queueAndStack))
# 实现队列功能，从队列中取一个元素，根据先进先出原则，这里应输出 1
print(queueAndStack.popleft())
# 实现栈功能，从栈里取一个元素，根据后进先出原则，这里应输出 hello
print(queueAndStack.pop())
# 再次打印列表
print(list(queueAndStack))
