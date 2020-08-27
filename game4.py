#找出传入列表中奇数位的元素，组成新列表输出
def processFunc(a):
    index=1
    lista=[]
    for i in a:
        if index%2==1:
            lista.append(i)
            pass
        index+=1
        pass
    return lista

print(processFunc([1,2,3,4,5]))