# 转义，可以理解为"采用某些方式暂时取消该字符本来的含义"，这里的"某种方式"指的就是在指定字符前添加反斜杠 \，以此来表示对该字符进行转义。
#
# 举个例子，在 Python 中单引号（或双引号）是有特殊作用的，它们常作为字符（或字符串）的标识（只要数据用引号括起来，就认定这是字符或字符串），而
# 如果字符串中包含引号（例如 'I'm a coder'），为了避免解释器将字符串中的引号误认为是包围字符串的“结束”引号，就需要对字符串中的单引号进行转义，
# 使其在此处取消它本身具有的含义，告诉解释器这就是一个普通字符。
#
#
#     转义字符	             说明
#       \	        在行尾的续行符，即一行未完，转到下一行继续写
#       \'	        单引号
#       \"	        双引号
#       \0	        空
#       \n	        换行符
#       \r	        回车符
#       \t	        水平制表符，用于横向跳到下一制表位
#       \a	        响铃
#       \b	        退格（Backspace）
#       \\	        反斜线
#       \0dd	    八进制数，dd 代表字符，如 \012 代表换行
#       \xhh	    十六进制数，hh 代表字符，如 \x0a 代表换行
s2 = '商品名\t\t单价\t\t数量\t\t总价'
s3 = 'C语言小白变怪兽\t99\t\t2\t\t198'
print(s2)
print(s3)
