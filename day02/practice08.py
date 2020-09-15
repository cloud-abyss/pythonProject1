# 输入两个正整数，计算最大公约数和最小公倍数
a=int(input('请输入正整数a：'))
b=int(input('请输入正整数b：'))
if a>b:
    a,b=b,a
for factor in range(a,0,-1):
    if a%factor==0 and b%factor==0:
        print('{}和{}的最大公约数是：{}'.format(a,b,factor))
        print('{}和{}的最小公倍数是：{}'.format(a,b,a*b//factor))
        break