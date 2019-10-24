# Python Set difference() 方法
# Python3 列表 Python 集合
#
# 描述
# difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
#
# 语法
# difference() 方法语法：
#
# set.difference(set)
# 参数
# set -- 必需，用于计算差集的集合
# 返回值
# 返回一个新的集合。
#
# 实例
# 返回一个集合，元素包含在集合 x ，但不在集合 y ：

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
# 输出结果为：

# {'cherry', 'banana'}
