# Python中的组合数据类型非常丰富，涵盖了列表、元组、集合、字典、字符串、字节等
# 列表是可变序列，列表中的元素可以是任意类型
# 列表用'[]'去定义，列表中的元素用','进行分割

# 列表的创建
lst=['hello','world',98,100]
print(lst)
lst2=list('helloworld')
print(lst2)
lst3=list(range(1,10,2))
print(lst3)

# 列表的删除
lst4=[1,2,3,4,5]
del lst

# enumerate函数进行列表的遍历
lst5=['hello','world','python','php']
for item in lst5:
    print(item)

for i in range(0,len(lst5)):
    print(i,'-->',lst5[i])

for index,item in enumerate(lst5):
    print(index,item)# 这里输出的index其实是序号不是索引，是我们可以手动修改的
# 手动修改序号的起使
for index,item in enumerate(lst5,start=1):
    print(index,item)

# 列表的排序操作
lst6=[1,38,19,87,0,98,6]
print('源列表',lst6)
lst6.sort() # 排序是在源列表的基础上进行的，不会产生新的列表对象
print('升序排列',lst6)
lst6.sort(reverse=True)
print('降序',lst6)
print('-'*50)
lst7=['banana','apple','Cat','Orange']
print('源列表',lst7)
# 升序排列，先排大写，后排小写(按照ASCII🐎)
lst7.sort()
print('升序',lst7)
lst7.sort(reverse=True)
print('降序',lst7)
# 自行指定排序规则
lst7.sort(key=str.lower)# 全部转变成小写
print(lst7)

# 排序的sorted函数，会新生成一个对象
asc_lst=sorted(lst7)# 默认升序
desc_lst=sorted(lst7,reverse=True)
print(lst7,asc_lst,desc_lst)

# 列表推导和生成器见fluentpython目录下的chap2

# 二维列表的生成
lst8=[
    ['city','population','score'],
    ['BeiJing',100,100],
    ['ShangHai',60,90],
    ['GuangZhou',40,95]
]
print(lst8)

# 遍历二维列表使用for循环
for i in lst8:# 第一个遍历的参数i代表行
    for item in i:# 第二个遍历的参数表示列
        print(item,end='\t')
    print()# 换行
