for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print('当前字母为 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当期变量值为 :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")
# 当前字母为 : R
# 当前字母为 : u
# 当前字母为 : n
# 当前字母为 : o
# 当前字母为 : o
# 当期变量值为 : 10
# 当期变量值为 : 9
# 当期变量值为 : 8
# 当期变量值为 : 7
# 当期变量值为 : 6
# Good bye!

print('######################')
for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)
print("Good bye!")

print('######################')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

print('######################')
# while True:
#     pass  # 等待键盘中断 (Ctrl+C)

print('######################')
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
