# 选择结构
number=eval(input('plz choose a number:'))
if number==123456: # 等值判断,==这个比较操作符会返回布尔值true或者false，如果结果是true则会执行循环
    print('Congratulation!')
if number!=123456: # 同样可以使用else语句
    print('what a pity!')

print('-'*10,'以上if循环是通过比较运算符比较出来的，结果是布尔类型','-'*10)
n=98
if n%2: # python中一切皆对象，0，空字符串的布尔值为false
    print(n,'is odd') # 98和2的余数是0，0的布尔值是false，则这行代码不会被执行
if not n%2:
    print(n,'is even')

# 双分支结构if-else
number=eval(input('plz choose a number:'))
if number==123456:
    print('Congratulation!')
else:
    print('what a pity!')
print('--------以上结果可以利用条件语句简化--------')

result='congratulation!' if number==123456 else 'waht a pity!'
print(result)

print('congratulation!'if number==123456 else 'what a pity!')

# 多分支结构
score=eval(input('plz write your score:'))
if score<0 or score>100:
    print('score is irreal!')
elif 0<=score<60:
    print('E')
elif 60<=score<70:
    print('D')
elif 70<=score<80:
    print('C')
elif 80<=score<90:
    print('B')
else:
    print('A')

# 嵌套if
current=input('did you drink? plz answer y or n:')
if current=='y':
    vol=eval(input('how many u drink:'))
    if vol<20:
        print('have a good trip')
    elif 20<=vol<80:
        print('damn bro, you are arrested!')
    else:
        print('damn!!!!!!!!!!')
else:
    print('have a good trip')

# 条件连接
user=input("plz write your username:")
password=eval(input("pla write your password:"))
if user=='chriswang' and password==888888:
    # 这里密码已经被eval转换成整数类型了，不要加引号（像user一样）否则会要求输入字符串类型的888888
    print('sign in successfully')
else:
    print('username or password is not correct')
# 用or连接的可以参考上面成绩判断不真实的地方