# 1.使用 in 来判定某个元素是否存在列表当中
a = [1, 2, 3, 4, 5]
print(2 in a)
print(20 in a)
print(2 not in a)
print(20 not in a)


# 2.使用 index 得到元素在列表中的下标
b = [6, 7, 8, 9, 0]
print(b.index(6))


# 3.使用pop删除列表末尾元素
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
c.pop()
print(c)


# 4. 指定下标删除元素
c.pop(4)
print(c)
c.pop(1)
print(c)


# 使用remove删除指定元素
c.remove(8)
print(c)

