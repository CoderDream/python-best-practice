# Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上end = ""：

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()
# 以上实例执行结果为：
#
# a
# b
# ---------
# a
# b