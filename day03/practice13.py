# CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
# 简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
# 玩家第一次如果摇出2点、3点或12点，庄家胜；
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
# 设置玩家初始资金为1000
from random import randint

money = 1000

while money>0:
    print('你的总资产为：%d元'%money)
    go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0<debt<=money:
            break

    first = randint(1,6)+randint(1,6)
    print('玩家摇出{}点'.format(first))
    if first==7 or first==11:
        print('玩家胜出！')
        money+=debt
    elif first==2 or first==3 or first==12:
        print('庄家胜出！')
        money-=debt
    else:
        go_on=True

    while go_on:
        go_on=False
        second=randint(1,6)+randint(1,6)
        print('玩家摇出{}点'.format(second))
        if second==first:
            print('玩家胜出！')
            money+=debt
        elif second==7:
            print('庄家胜出！')
            money-=debt
        else:
            go_on=True

print('你破产了，游戏结束！')


