# 定义函数
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return


# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")


# python 传不可变对象实例

def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)  # 结果是 2


# 传可变对象实例
# 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：


# 可写函数说明
def changeme(mylist):
    """修改传入的列表"""
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)
