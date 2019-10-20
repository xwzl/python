# 第一个例子，假设 C 语言中文网想做 VIP 促销活动，准备进行打折，现需要写一个 apply_discount() 函数，要求是，向该函数传入原来的价格和折扣力度，该函数返回打折后的价格。
# apply_discount() 大致应该写成如下这样：
# price 为原价，discount 为折扣力度
def apply_discount(price, discount):
    updated_price = price * (1 - discount)
    # 这样一来，如果开发人员修改相关的代码，或者是加入新的功能，导致 discount 数值异常时，只要运行程序就很容易能发现问题，这也从侧面印证了前面多讲的，assert 的加入可以
    # 有效预防程序漏洞，提高程序的健壮性。
    assert 0 <= updated_price <= price, '折扣价应在 0 和原价之间'
    return updated_price


# 可以看到，在计算新价格的后面，添加了一个 assert 语句，用来检查折后价格，这里要求新折扣价格必须大于等于 0、小于等于原来的价格，否则就抛出异常。
#
# 我们可以试着输入几组数，来验证一下这个功能
print(apply_discount(100, 0.2))


# print(apply_discount(100, 1.1))
#
# 另外，在实际工作中，assert 还有一些很常见的用法
def func(value):
    assert isinstance(value, list), '输入内容必须是列表'
    # 下面的操作都是基于前提：input 必须是 list
    if len(value) == 1:
        pass
    elif len(value) == 2:
        pass
    else:
        pass


# 以上给大家介绍了 2 个有关 assert 的使用场景，很多读者可能觉得，assert 的作用和 if 语句非常接近，那么他们之间是否可以相互替代呢？
#
# 要注意，前面讲过，assert 的检查是可以被关闭的，比如在命令行模式下运行 Python 程序时，加入 -O 选项就可以使程序中的 assert 失效。一旦 assert 失
# 效，其包含的语句也就不会被执行。
#
# 还是拿 C 语言中文网用户来说，只有 VIP 用户才可以阅读 VIP 文章，我们可以设计如下这个函数来模式判断用户身份的功能：
#
#   def login_user_identity(user_id):
#         # 凭借用户 id 判断该用户是否为 VIP 用户
#         assert user_is_Vip(user_id), "用户必须是VIP用户，才能阅读VIP文章"
#         read()
#
# 此代码从代码功能角度上看，并没有问题，但在实际场景中，基本上没人会这么写，因为一旦 assert 失效，则就造成任何用户都可以阅读 VIP 文章，这显然是不合理的。
#
# 所以正确的做法是，使用 if 条件语句替代 assert 语句进行相关的检查，并合理抛出异常：

# def login_user_identity(user_id):
#     #凭借用户 id 判断该用户是否为 VIP 用户
#     if not user_is_Vip(user_id):
#         raise Exception("用户必须是VIP用户，才能阅读VIP文章")
#     read()