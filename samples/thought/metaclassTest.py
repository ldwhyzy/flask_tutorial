class Atest(type):   #继承了type类的子类同样创建类
    subClasses = {}
    
    def __init__(cls, name, bases, dic):
        print('--in Atest init--')
        print(cls)
        if name != 'ModelCla':
            Atest.subClasses[name] = cls
    
    def __new__(cls, name, bases, dic):
        print('--in Atest new--')
        print(dic)
        dic['score'] = 99
        return super().__new__(cls, name, bases, dic)
    
ModelCla = Atest(name='ModelCla', bases=(), dic={'fun1':(lambda x: x+2)}) #type类是实例是类，即type类(继承了type类的子类同样)的作用是创建类的
#print(ModelCla.__name__)

# class B(a):
#     height = 5
 
'''  
class B(ModelCla):
    pass
'''
class C(ModelCla):
    wieght = '99k'
    @classmethod
    def fun3(cls, value):
        print(cls)
        return value-7
         
    def fun2(self, value):
        return value+90

# print(B.__dict__)    
# print(dir(C))
# print(C.__dict__)
print(C().fun3)
# print(C.score)
# print(Atest.subClasses)
# print(C.func2(5))    

#type重载？
#type(object_be_tested)
#type(name='class_be_created', bases=(inhreit_class), dit={attrs})

'''
class A():
    p = 'mon'
    def __init__(self, name, age ,p):
        print('in A.__init__')
        print(self)
        self.name = name
        self.age = 60
        self.p = p
    def info(self):
        print('name:', self.name, '  age:', self.age, self.p)
        
class E():
    pass
'''


