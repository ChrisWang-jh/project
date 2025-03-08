# break语句会跳出循环结构
# 在while循环中的应用
s=0
i=1
while i<10:
    s=s+i
    if s>=20:
        print('目前的累加和已经大于20,值为:',s)
        break
    i=i+1

# 在for循环中的使用
for i in 'helloworld':
    print(i)
    if i=='r':
        break

# 猜数游戏，随机生成一个1~100之间的整数，用户不断猜这个数，输出“大了”or“小了”，直到猜中为止，输出用户的猜测次数
import random
rand=random.randint(1,100)
guess=eval(input('plz guess a number:'))
if rand==guess:
    print('猜中啦！')
elif rand<guess:
    print('大了')
elif rand>guess:
    print('小了')
print(rand)

import random
rand=random.randint(1,100)
guess=eval(input('plz guess a number:'))
i=1
while guess!=rand:
    i=i+1
    if guess>rand:
        print('大了,请重新猜测')
        guess=eval(input('plz guess a number:'))
    if guess<rand:
        print('小了,请重新猜测')
        guess=eval(input('plz guess a number:'))
else:
    print('猜中啦！您总共用了',i,'次')
print('结果是:',rand)
