import sys  # 引入 sys 模块

number_list1 = [1, 2, 3, 4]
it1 = iter(number_list1)  # 创建迭代器对象
print(next(it1))  # 输出迭代器的下一个元素
# 1
print(next(it1))
# 2

print('######################')
number_list2 = [1, 2, 3, 4]
it2 = iter(number_list2)  # 创建迭代器对象
for x in it2:
    print(x, end=" ")

print('')
print('######################')
number_list3 = [1, 2, 3, 4]
it3 = iter(number_list3)  # 创建迭代器对象

while True:
    try:
        print(next(it3))
    except StopIteration:
        sys.exit()
