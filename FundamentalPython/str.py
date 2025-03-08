# 字符串str是不可变数据类型

# 大小写转换
s1='HELLOWORLD'
news1=s1.lower()
print(news1)
s2=news1.upper()
print(s2)
print(s1==s2)
print(id(s1))
print(id(s2))
print(id(s1)==id(s2))

# 字符串的分割
s='chriswangjh@qq.com'
a=s.split('@')# 会删除@
print(a)# 分割结果是一个列表

# 查找和数数
print(s.count('q'),end='\t')
print(s.find('q'),end='\t')
print(s.index('q'))

# 字符串可以进行：替换，部分删除，指定删除，填充，

# 格式化字符串(格式化后的字符串可以拼接其他数据类型)
# 占位字符串
name='chirs'# %s字符串占位符,%d整数占位符,%f小数占位符
age=18
score=99.5
print('姓名:%s,年龄:%d,得分:%f' % (name,age,score))
# f-string占位法***
print(f'姓名:{name},年龄:{age},得分:{score}')
# 字符串format方法
print('姓名:{0},年龄:{1},得分:{2}'.format(name,age,score))
# format进行输出格式控制

# 字符串的编码和解码 encode decode
'''
str--->bytes  编码
bytes--->str  解码
'''
s='你好中国'
scode=s.encode(errors='replace') # errors类型：strict,replace,ignore
scode2=s.encode('gbk',errors='strict')
print(scode)
print(scode2)

# 可以判断字符串是否全部包括数字，字符，全部大写与否......

# 字符串的拼接，去重
print('hello'+'world')
print('hello''world')
print(''.join(['hello','world']))
print('!好好'.join(['hello','world']))
print('%s%s' % ('hello','world'))
print(f'{'hello'}{'world'}')# ***更简洁
print('{0}{1}'.format('hello','world'))

# 正则表达式：一个特殊的字符序列.用于验证一个字符串是否符合某整形式
# 元字符：^,&,.,\w,\W,.......
# re模块：内部有用于处理正则表达式的函数