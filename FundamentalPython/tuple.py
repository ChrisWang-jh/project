# 不可变序列
# 元组的创建与删除
t=('hello',[10,20,30],77)
print(t)
t=tuple('helloworld')
print(t)
t=tuple([10,20,30])# 注意这里要加[]
print(t)

# 元组支持索引，切片，遍历(与list相同)