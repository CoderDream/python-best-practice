# 集合
# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。

# 可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。

# 以下是一个简单的演示：

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 删除重复的
# {'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)  # 检测成员
# True
print('crabgrass' in basket)
# False

# 以下演示了两个集合的操作
a = set('abracadabra')
b = set('alacazam')
print(a)  # a 中唯一的字母
# {'a', 'r', 'b', 'c', 'd'}
print(a - b)  # 在 a 中的字母，但不在 b 中
# {'r', 'd', 'b'}
print(a | b)  # 在 a 或 b 中的字母
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)  # 在 a 和 b 中都有的字母
# {'a', 'c'}
print(a ^ b)  # 在 a 或 b 中的字母，但不同时在 a 和 b 中
# {'r', 'd', 'b', 'm', 'z', 'l'}


print("------------------------")
# 集合也支持推导式：

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# {'r', 'd'}
