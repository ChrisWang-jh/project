'''
while循环的四个步骤
初始化变量 条件判断 语句块 改变变量
'''
# 无限循环while的使用
answer=input('你现在上课吗?y/n:')# 1)初始化变量
while answer=='y':# 2)条件判断
    print('好的,上课吧,不打扰你了')# 3)语句块
    answer=input('你现在上课吗?y/n:')# 4)改变变量
else:
    print('和我一起玩吧！')# 如果我们把改变变量的语句放在else后面，则会不断输出’好的，上课吧，不打扰你了‘

# 求1~100之间的累加和
s=0
i=1
while i<=100:
    s=s+i
    i=i+1
print('1~100之间的累加和为:',s)

# 使用无限循环模拟用户登录(给用户三次机会)
i=0
while i<3:
    user=input('plz write your username:')
    password=input('plz write your password(6-digit):')
    if user=='chris' and password=='888888':
        print('sign in successfully!')
        i=4
    else:
        print('username or password is not correct,you have',2-i,'times left')
        i=i+1
if i==3:
    print('sorry,you tried too many times')
    
