import timeit#导入计时模块
l1 = '这是第一行'
print (l1)
print ('这是/n')
print (4//2)#整数结果
print (4/2)#浮点数，p2中是整数
print (4%2)
print (2%4)
print (('a','b'))

def test():
    for i in range(100):
        pass#略过

a = timeit.timeit(test)#使用计时模块，函数形式
print (a)