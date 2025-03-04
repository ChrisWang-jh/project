# eval函数作用：去掉字符串最外层的引号，直接按python语句执行
s='3+3.14'
print(eval(s),type(s))
w='helloworld'
print(eval('w'))
# eval函数经常与input配合使用，用于改变输入的数据类型