# 输出所有水仙花数
for i in range(100,1000):
    g=i%10
    s=(i//10)%10
    b=i//100
    if i==(g**3+s**3+b**3):
        print(i)
