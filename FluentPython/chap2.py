# 列表推导(list comprehension)
# ord函数：字符→码点
def part1():
    symbols = '1234567'
    codes = [ord(symbol) for symbol in symbols]
    print(codes)

# chr函数：码点→字符
def part2():
    print(chr(49))

# 列表推导同filter和map比较
def part3():
    symbols = '1234567'
    A = [ord(a) for a in symbols if ord(a) > 51]
    print(A)

    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols))) 
    beyond_ascii

# 生成器表达式（generator expression）
def part4():
    symbols = '1234567'
    a=tuple(ord(symbol) for symbol in symbols)
    print(a)

# 元组拆包, use "*" and "-"
def part5():
    a, b, *rest = range(5)
    c, *body, d = range(6)
    print(a, b, rest) # Note 'rest' at here no '*' in front
    print(c, body, d)

# 切片的应用
def part6():
    l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a=l[:2]
    b=l[2:]
    c=l[::3]
    d=l[1::3]
    e=l[::-1]
    f=l[::]
    print(a, b, c, d, e, f, sep='\n')
    l[2:5]=[0] #修改
    print(l)
    l[3::]=[1,2,3,4,5] #修改
    print(l)

# 建立由列表组成的列表

# 序列增量赋值 +， *， +=， *=

# sort函数的用法

# 用bisect管理已排序的序列

# 数组、内存视图、队列对于列表的优势
if __name__ == "__main__":
    #part1()
    #part2()
    #part3()
    #part4()
    #part5()
    part6()