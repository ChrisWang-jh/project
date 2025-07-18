# 类的定义(首字母必须大写)定义了一个数据类型
class Person():
    pass

# 创建类的对象
chris=Person()
print(type(chris))

# 完整的类的创建
# 类应该包括：类属性，实例属性，实例方法，静态方法，类方法
class Student():
    school='北京四中'# 类属性，定义在类中，方法外的变量
    # 初始化方法（定义在类中的函数称为方法）
    def __init__(self,xingming,nianling):# 姓名，年龄是方法的参数，是局部变量，也就是说这两个变量的作用域只在init函数里
        self.name=xingming# 实例属性=局部变量，将局部变量赋值给实例属性self.name
        self.age=nianling#这样的话，在init这个函数外就可以调用这两个变量了
    # 定义在类中的函数称为方法，方法自带一个self变量
    # 实例方法
    def show(self):
        print(f'我叫:{self.name},我今年:{self.age}岁')# 局部变量出了函数便不可使用，单实例属性可以被使用
    # 静态方法，使用装饰器@staticmethod去修饰
    #@staticmethod
    # 类方法，使用装饰器@classmethod修饰


# 创建类的对象
stu1=Student('wjh','21')#init方法中有两个参数
stu2=Student('gmy','21')
stu3=Student('wjt','54')
stu4=Student('zpp','54')
lst=[stu1,stu2,stu3,stu4]
for i in lst:
    i.show()# 对象名打点调用实例方法
# 实例属性，通过对象名打点调用
print(stu1.name,stu1.age)
# 类属性，通过类名打点调用
print(Student.school)