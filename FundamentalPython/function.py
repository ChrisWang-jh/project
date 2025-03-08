# 函数的定义和调用

# 定义一个累加和函数
def getsum(num):#函数定义处的参数num称为形式参数
    s=0
    for i in range(num+1):
        s=s+i
    print(f'1~{num}之间的累加和为：{s}') ##注意print的缩进位置
# 调用函数
getsum(100)#函数调用处的称为实际参数

# 函数默认值参数的使用：在定义函数时定义一个形式参数的默认值，如果调用函数时没有实际参数的输入则使用默认参数
def happyeveryday(name='Agnes',age='18'):
    print(f'Wish {name} happyeveryday!')
    print(f'Forever {age}!')
happyeveryday()

a=input('plz write your name:')
b=input('plz write your age:')
happyeveryday(name=a,age=b)

# 可变参数
#个数可变的位置参数(*para)；个数可变的关键字参数(**para)
# para是形式参数名称，可接收任意个数的实际参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)

fun([10,20],30,40)
fun(10,20,30,40)
fun(*[10,20],30,40)

def func(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'--->',value)

func(name='chris',age='21')
d={'name':'chris','age':'21'}
func(**d)

# 函数的返回值：return:如果函数的计算结果要在其他函数中继续使用，那么在定义这个函数的时候就要被定义成带返回值的函数
def calculate(a,b):
    print(a+b)
calculate(10,20)# 会输出30
# print(calculate(10,20))# 会输出None，因为我们没有给这个函数定义返回值
def cal2(a,b):
    s=a+b
    return s
t=cal2(10,20)
print(t)
# 多个返回值的情况(输出类型会变为元组)
def accumulate(num):
    s=0
    evensum=0
    oddsum=0
    for i in range(num+1):
        if i%2==0:
            evensum+=i
        else:
            oddsum+=i
        s+=i
    return s,evensum,oddsum
q=accumulate(100)
print(type(q))
print(q)
d,f,g=q
print(d,f,g)


# 变量的作用域：局部变量和全体变量
'''
定义在函数中的变量称为局部变量，外部不可调用
但是当局部变量和全局变量名称相同时，局部变量优先级更高
可以使用命令：global.s,来将在循环内的局部变量设置成全局变量
'''

# 匿名函数lambda(一般在函数仅有一行代码，一个返回值时使用)
def cal(a,b):
    return a+b
s=lambda a,b:a+b # s就表示一个匿名函数
print(type(s))
print(s(10,20))

students=[
    {'name':'AAA','score':'89'},
    {'name':'BBB','score':'96'},
    {'name':'CCC','score':'72'},
    {'name':'DDD','score':'99'},
]
students.sort(key=lambda x:x.get('score'),reverse=True)
print(students)

# 递归函数
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)# 自己调用自己
print(fac(5))

# 常见内置函数：类型转换函数，数学函数，迭代器操作函数（对可迭代对象，如列表，元组进行操作）
# filter，map的对象是函数
def judge(n):
    return n%3==0
obj=filter(judge,range(10))# 通过指定条件过滤对象并返回一个迭代器对象
print(type(obj))
print(obj)
print(list(obj))

def upper(x):
    return x.upper()
lst=['hello','python','magic']
obj2=map(upper,lst)# 通过function对每个可迭代对象都进行一次操作，然后返回一个迭代器对象
print(list(obj2))