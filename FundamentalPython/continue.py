# 跳转语句continue跳过当前循环直接进入下一次循环
s=0
i=1
while i<=100:
    if i%2==1:
        i=i+1 # 这行代码是必要的！
        continue
    s=s+i
    i=i+1
print('1~100之间的偶数和为:',s)

c=0
for j in range(1,101):
    if j%2==1:
        continue
    else:
        c=c+j
print('1~100之间的偶数和为:',c)
