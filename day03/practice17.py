# 计算两个数的最大公约数和最小公倍数
def gy(x,y):
    if x>y:
        x,y=y,x
    for factor in range(x,0,-1):
        if x%factor==0 and y%factor==0:
            return factor
def gb(x,y):
    return x*y//gy(x,y)
