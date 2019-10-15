# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用 printme 函数，不加参数会报错
# printme()


# 函数参数的使用不需要使用指定顺序：
# 可写函数说明
def printinfo(name, age):
    """打印任何传入的字符串"""
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")


# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")


# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)

print("------------------------")


# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
# 可写函数说明
def printinfo2(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo2(10)
printinfo2(70, 60, 50)

print("------------------------")


# 还有一种就是参数带两个星号 **基本语法如下：
#
# def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 加了两个星号 ** 的参数会以字典的形式导入。
# 可写函数说明
def printinfo3(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo3(1, a=2, b=3)

print("------------------------")


# 声明函数时，参数中星号 * 可以单独出现，例如:

def f(a, b, *, c):
    return a + b + c


# f(1,2,3)   # 报错
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: f() takes 2 positional arguments but 3 were given
t = f(1, 2, c=3)  # 正常
print(t)
# 6
