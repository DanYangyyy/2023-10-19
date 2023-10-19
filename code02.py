# 列表的拼接
# 使用 + 来实现
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)


# 使用 extend 来实现
c = ["hello", 1]
d = [2, "world"]
c.extend(d)
print(c)


# 使用 += 来实现
e = [7, 8, 9]
f = ["hello", "world"]
e += f
print(e)
print(f)