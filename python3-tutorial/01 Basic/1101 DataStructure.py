from collections import deque

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
# 2 1 0
a.insert(2, -1)
a.append(333)
print(a)
# [66.25, 333, -1, 333, 1, 1234.5, 333]
idx = a.index(333)
print(idx)
# 1
a.remove(333)
print(a)
# [66.25, -1, 333, 1, 1234.5, 333]
a.reverse()
print(a)
# [333, 1234.5, 1, 333, -1, 66.25]
a.sort()
print(a)
# [-1, 1, 66.25, 333, 333, 1234.5]

# 将列表当做堆栈使用
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
# 用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。例如：


print("------------------------")
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
# [3, 4, 5, 6, 7]
print(stack.pop())
# 7
print(stack)
# [3, 4, 5, 6]
print(stack.pop())
# 6
print(stack.pop())
# 5
print(stack)
# [3, 4]


print("------------------------")

# 将列表当作队列使用
# 也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
# 在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue.popleft())  # The first to arrive now leaves
# 'Eric'
print(queue.popleft())  # The second to arrive now leaves
# 'John'
print(queue)  # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])

print("------------------------")

# 列表推导式
# 列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，
# 用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。

# 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
# 返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。

# 这里我们将列表中每个数值乘三，获得一个新的列表：

vec = [2, 4, 6]
print([3 * x for x in vec])
# [6, 12, 18]

print("------------------------")
# 现在我们玩一点小花样：

print([[x, x ** 2] for x in vec])
# [[2, 4], [4, 16], [6, 36]]


print("------------------------")

# 这里我们对序列里每一个元素逐个调用某方法：

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])  # 去掉左右空格
# ['banana', 'loganberry', 'passion fruit']

print("------------------------")

# 我们可以用 if 子句作为过滤器：

print([3*x for x in vec if x > 3])
# [12, 18]
print([3*x for x in vec if x < 2])
# []


print("------------------------")

# 以下是一些关于循环和其它技巧的演示：

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
# [8, 6, -18, 16, 12, -36, 24, 18, -54]
print([x+y for x in vec1 for y in vec2])
# [6, 5, -7, 8, 7, -5, 10, 9, -3]
print([vec1[i]*vec2[i] for i in range(len(vec1))])
# [8, 12, -54]


print("------------------------")

# 列表推导式可以使用复杂表达式或嵌套函数：

print([str(round(355/113, i)) for i in range(1, 6)])
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']
