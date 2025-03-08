# 键值对
# 字典是可变数据类型
# 字典是无序的（哈希）

# 字典的创建方式
d={10:'cat',20:'dog',30:'frog',20:'pet'}
print(d) # key只能有一个，value可以有多个，当key重复时，会用后出现的value进行覆盖
list1=[10,20,30,40]
list2=['cat','dog','frog','pet']
zipobj=zip(list1,list2)
print(zipobj)# 输出结果为zip
d=dict(zipobj)
print(d)# 输出的类型为字典类型

# 只有不可变数据类型才能作为字典当中的键
t=(10,20,30)
print({t:10})# t是tuple可以作为字典当中的键，list不可以

# dict也是序列，可以进行求最大值，最小值，长度

# 字典元素的访问
print(d[10])
# print(d['cat']) d[]输入key用来获取value
print(d.get(10))
# 二者有细微差别：如果key不存在,d[key]会报错，而d.get[key]可以返回默认值
print(d.get(50),'不存在')

# 字典的遍历
for item in d.items():
    print(item)
