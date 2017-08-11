'''
题目：
程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
程序根据用户输入，给予一定提示（大了、小了、正确）
猜对或用完 10 次机会，游戏结束
输入模块
判断大小
随机生成数
10次机会判断
'''
'''
import random
def comp(b):
    a = input('猜数字游戏开始，请输入\n>')
    if a>b:
        print("大了")
    elif a<b:
        print("小了")
    elif a==b:
        print("正确")
        exit('游戏结束')
    else:
        print("输入有误")

def game_times():
    times = 10
    if times > 0:
        while times > 0:
            print("你还有%d次机会" % times)
            comp()
            times -= 1
    else:
        print('游戏结束')

def game():
    ture_num = int(random.random() * 10)
    comp(ture_num)
'''

import random
print('我想到一个20以内的数字，猜猜看？')
n = 10
b = int(random.random() * 20)
while n > 0:
    a = input('请输入你猜测的数字\n>')
    if not a.isdigit():
        print('麻烦输入数字啦')
    elif int(a) < b:
        print("小了")
    elif int(a) == b:
        exit('恭喜你答对啦！\n游戏结束')
    else:
        print("大了")
    n -= 1
    print('你还有%d次机会' % n)

print('游戏结束！很可惜，正确答案是%d' % b)

