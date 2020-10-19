'''
位置参数

可变参数(收集任意多基于位置或关键字的参数)
func(*arg), func(**kw), func(*arg, **kw)

#命名关键字参数func(posi, *arg, keyword_only, **kw) 
#函数定义时keyword_only必须在变长参数之后，关键字参数之前。函数调用时key_word必须以关键字赋值，不能与默认参数混淆。
#func(a, *b, c, **d)   func(1, 2, c=999)

#name=value的形式，
#在调用时代表关键字参数，调用时只有关键字参数和非关键字参数之分。
#在def定义时代表默认值参数

#参数顺序
#函数调用中，参数出现顺序：任何位置参数(value)，任何关键字参数(name=value)和*sequence形式的组合，**dict形式
#函数头部，参数出现顺序：任何一般参数(name)，任何默认参数(name=value)，*name, name/name=value的kewword-only参数，**name
#调用或函数定义时，**arg必须出现在最后

#赋值的参数匹配顺序
#通过位置分配  非关键字参数
#通过匹配变量名分配  关键字参数
#其他额外的非关键字参数分配到*name元祖中
#其他额外的关键字参数分配到**name字典中
#用默认值分配给在未得到分配的参数
'''

##匹配要点
#拿实参中的非关键字参数来分配给定义中的位置参数
def func(c=222,*arg, **kw):  #c是默认参数
    print('arg: ', arg, ' kw: ',kw, 'c: ', c)
    
func(99,b=7, g=9,a=78)   #arg: () kw: {'b': 7,'g': 9, 'a': 78} 'c': 99
#func(99,c=88 , b=7, g=9,a=78)   #typeError:func() got multiple values for argument 'c'

def func(*arg, c=222, **kw):  #c是kewword-only参数
    print('arg: ', arg, ' kw: ',kw, 'c: ', c)
    
func(c=99,b=7, g=9,a=78)   #arg: () kw: {'b': 7,'g': 9, 'a': 78} 'c': 99
func(88,c=99,b=7, g=9,a=78)   #arg: (88,) kw: {'b': 7,'g': 9, 'a': 78} 'c': 99 