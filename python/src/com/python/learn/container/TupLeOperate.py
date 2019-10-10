# 元组是 python 中另一个重要的序列结构，和列表类似，也是有一系列按特定顺序排序的元素组成。和列表不同的是
# 列表可以任意操作元素，是可变序列；而元组是不可变序列，即元组中的元素不可以单独修改。
#
# 元组可以看做是不可变得的列表。通常情况下，元组用于保存不可修改的内容。
#
# 从形式上看，元组的所有元素都放在一对小括号中，相邻元素之间用逗号分隔，如下所示：
#
#   （e1,e2,...,en）
#
# 其中 element1~elementn 表示元组中的各个元素，个数没有限制，且只要是 Python 支持的数据类型就可以。
#
# 从存储内容上看，元组可以存储整数、实数、字符串、列表、元组等任何类型的数据，并且在同一个元组中，元素的类型可以不同，例如：
#
#   ("c.biancheng.net",1,[2,'a'],("abc",3.0))
#
# 在这个元组中，有多种类型的数据，包括整形、字符串、列表、元组。
#
# 另外，我们都知道，列表的数据类型是 list，那么元组的数据类型是什么呢？通过 type() 函数，就可以查看到元组的数据类型，例如：
#
#   >>> type(("c.biancheng.net",1,[2,'a'],("abc",3.0)))
#   <class 'tuple'>
#
# 可以看到，元组是 typle 类型，这也是很多教程中用 tuple 指代元组的原因。
