# 由于python都是引用，而python有GC机制，所以，del语句作用在变量上，而不是数据对象上。
# del删除的是变量，而不是数据。如果有其他引用，仍然能得到数据

# output:
#1
#[2, 3, 4, 5]
#2    
def test_del():
    li = [1,2,3,4,5]
    a = li[0]
    del li[0]
    print(a)
    print(li)
    print(li[0])
    
    
if __name__ == '__main__':
    test_del()      

    