'''
开发升级版猜数字小游戏，实现以下功能：
程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
用户输入 4 位数进行猜测，程序返回相应提示
用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
用户猜测后，程序返回 A 和 B 的数量
比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
猜对或用完 10 次机会，游戏结束
'''
import random
def true_num():
    '''制造一个随机四位数，先生成一个列表，然后用列表生成数字'''
    list1 = list(range(10))
    true_list = []
    while len(true_list) < 4:
        i = int(random.random() * 10) - len(true_list)
        a = list1.pop(i)
        if int(a) == 0 and len(true_list) == 0:
            pass
        else:
            true_list.append(a)
    #num = ''.join(str(e) for e in true_list)#字符串
    num2 = int(''.join(str(e) for e in true_list))#四位数字
    return num2 #可以不用变量，直接返回上面结果，继续精简

def com_num(num0,g_num):
    '''对比两个数字，先把数字转化成字符串，然后逐个去对比，最后返回结果'''
    count_a = 0
    count_b = 0
    list1 = str(num0)
    list2 = str(g_num)
    #list2 = [int(x) for x in str(list_g)]
    for i in range(4):
        if list1[i] == list2[i]:
            count_a += 1
        elif list1[i] != list2[i] and list1[i] in list2:
            count_b += 1
        else:
            pass
        i += 1
    return count_a,count_b

def guess():
    '''主程序，计数，猜数'''
    n = 10
    num0 = true_num()
    print('我心里想了一个四位数，由不同的四个数字组成，猜猜看吧！')
    while n > 0 :
        print('输入数字猜猜看')
        g_num = input('>')
        if g_num.isdigit() and len(g_num) == 4:
            a,b = com_num(num0,int(g_num))
            if a == 4:
                print('good')
                exit('job')
            else:
                print('你猜的结果为:%dA%dB,come on！' % (a,b))
            n -= 1
            print('你现在还有%d次机会' % n)
        else:
            print('麻烦输入一个四位数啦')
    print('游戏结束啦，正确答案为：%d' % num0)
guess()
