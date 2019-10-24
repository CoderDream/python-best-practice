aList = ['Google', 'Runoob', 'Taobao', 'Facebook']

aList.sort()
print("List : ", aList)

# 以下实例降序输出列表：



# 列表
vowels = ['e', 'a', 'u', 'o', 'i']

# 降序
vowels.sort(reverse=True)

# 输出结果
print('降序输出:', vowels)


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)

# 输出类别
print('排序列表：', random)

# random2 = [
#     {'id': '300723', 'name': '一品红'},
#     {'id': '300724', 'name': '捷佳伟创'}
# ]
# # 指定第二个元素排序
# random2.sort(key=takeSecond)
# # 输出类别
# print('排序列表：', random2)

