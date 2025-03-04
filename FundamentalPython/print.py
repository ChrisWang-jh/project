a = 100
b = 50
print(90,a,b,a+b,a*b,'Hello World',"hello world")
print(a/b,b/a)
print(chr(56))
print(ord('c')) # 注意ord()函数中要加引号，否则会报错

# Use print to write sth in certain file
fp=open('note.txt','w') # open the file, 'w'--write
print('Hello world',file=fp) # print 'Hello world' in the file
fp.close()

# 多条print结果输出到一条显示
print('Hello',end='-->')
print('World')
print('Hello'+'World') # 只能是字符串连接字符串
# print函数的完整格式为：print(value,...,sep= '',end= '/n',file =none)

fp=open('note.txt','w')
print('i will write this sentense into this file',file=fp)
fp.close()