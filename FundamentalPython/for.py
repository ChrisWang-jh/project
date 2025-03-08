# 可以遍历的对象包括：字符串，文件，组合数据类型，数组....
for i in 'hello':
    print(i)

# range函数，产生包含n但不包含
for i in range(1,11):
    if i%2:
        print(i,'is odd')
    else:
        print(i,'is even')

s=0 # 存储累加和
for i in range(1,11):
    s=s+i # s+=i
print('1~10之间的累加和为:',s)

print('---------找到100~999之间的水仙花数-----------')
'''
水仙花数指的是
153=3*3*3+5*5*5+1*1*1
ps:这种用三个’隔开的一样是注释
'''
for i in range(100,1000):
    singledigit=i%10 # 个位上的数字
    tens=i//10%10 # 十位上的数字
    hundred=i//100 # 百位上的数字
    if i==singledigit**3+tens**3+hundred**3:
        print(i,'is 水仙花数')
