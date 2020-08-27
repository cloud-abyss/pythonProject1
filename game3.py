#求n个数的累加和
def sumFunc(*args):
    sum=0
    for item in args:
        sum+=item
        pass
    return sum

re=sumFunc(1,2,3,4)
print(re)
