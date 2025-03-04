# 利用type函数查看变量的数据类型
a=8
b='chris'
c=2.12
print(type(a),type(b),type(c))

# 利用id函数查看变量的内存地址
print(id(a),id(b))

# 整数和浮点类型
# 使用不同进制表示数字
num1=123
num2=0b11 # 二进制
num3=0o70 # 八进制
num4=0x8ABF # 十六进制
print(num1,num2,num3,num4)

# 转义字符 \n \t \' \" r
print('----------------------')
print('Hello\nworld') # 换行
print('Hello\tworld') # 空格填满制表位
print('\'Helloworld\'') # 输出引号
print(r'Hello\nworld') # 使转义字符失效

# 字符串类型
# 字符串的索引和切片
word='helloworld'
print(word[0],word[-10])
s='中文组成的字符串一样可以接受索引'
print(s[5:])
print(s[-5:-1])

# 字符串的操作
print(word+s)
print(s*2)
print('中文' in s)
print('hello' in s)

# 布尔类型
# 布尔值以及如何查询一个字符串的布尔值
x=True
print(x)
print(type(x))
print(bool(x))
print(bool(0),bool(0.0),bool(1))
print(bool(''),bool('hello'))

# 数据类型的转换
