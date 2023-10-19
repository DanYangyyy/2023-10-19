# 使用 write 写入文件
f = open('C:/test/test.txt', 'w')
f.write('hello ')
f.close()

f = open('C:/test/test.txt', 'a')
f.write('world')
f.close()
