# 百钱百鸡 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for i in range(1,20):# 公鸡
    for j in range(1,33):
        x=100-i-j
        if 5*i+3*j+(1/3)*x==100:
            print('公鸡{}只，母鸡{}只，小鸡{}只'.format(i,j,x))
