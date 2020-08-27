#猜年龄游戏
#1.允许用户尝试3次
#2.3次后，问用户是否还想要玩
#3.猜对后直接退出

times=0
count=3
while times<=3:
    age=int(input('请输入您猜测的年龄：'))
    if age==20:
        print('恭喜您，猜对了')
        break
        pass
    elif age>20:
        print('猜大了')
        pass
    else:
        print('猜小了')
        pass
    times+=1
    if times==3:
        choose=input('要继续吗 y/n')
        if choose=='y' or choose=='Y':
            times=0
            pass
        elif choose=='N' or choose=='n':
            times=4
            pass
        else:
            print('请重新输入')
        pass