# 序列是一个用于存储多个值的连续空间，每个值都有一个对应的编号，称为索引
# 属于序列结构的包括：字符串，列表，元组，集合，字典

# 如何使用索引
s='helloworld'
print(s[0])

# 序列的切片
print(s[0:5:2])
print(s[:5:1])
print(s[::-1])
print(s[-1:-11:-1])

# 序列的相加和相乘
a='hello'
b='world'
print(a+b)
print(a*4)
print(len(s))
print(max(s))

print('s.index',s.index('o'))
print('s.count',s.count('o'))