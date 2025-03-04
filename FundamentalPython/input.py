
name=input('plz write your name:')
print('my name is:'+name)

# 输入整数类型的数据
num=input('plz choose a number')
print('The choosen number is:'+num) # 这里不报错说明num是字符串类型
num=int(num) # 这里我们利用内置函数int将字符串类型的num转换成整数类型
print('The choosen number is:',num)

print(type('name'))