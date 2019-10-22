# 使用 exec() 和 eval() 函数时，一定要记住，它们的第一个参数是字符串，而字符串的内容一定要是可执行的代码
s = "hello"
print(eval("print(s)"))

# 如果要将字符串 hello 通过 print 函数打印出来，可以写成如下的样子：
print(eval('s'))
