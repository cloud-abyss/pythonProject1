# 输入三条边长，如果可以构成三角形就计算周长和面积
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a+b>c and a+c>b and b+c>a:
    print('周长为：%d'%(a+b+c))
    #海伦公式
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print('面积为：%f'%area)
else:
    print('不能构成三角形')
