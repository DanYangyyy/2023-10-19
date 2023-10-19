# 遍历字典

stu = {
    'id':1,
    'name':"wangwu",
    'score':98
}
for key in stu:
    print(key,stu[key])

print(stu.keys())
print(stu.values())
print(stu.items())

for key,values in stu.items():
    print(key,values)