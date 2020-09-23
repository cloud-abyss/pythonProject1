# 100以内的素数,不包括1
import math
for i in range(2,100):
    is_prime = True
    for factor in range(2,int(math.sqrt(i))+1):
        if i%factor==0:
            is_prime=False
            break
    if is_prime:
        print(i,end=' ')

