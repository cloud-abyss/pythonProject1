#1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count=0  #统计总数
for g in range(1,5):
    for s in range(1,5):
        for b in range(1,5):
            if(g!=s) and(g!=b) and (s!=b):
                result=str(b)+str(s)+str(g)
                print(result)
                count+=1
                pass
print(count)

#2：输入某年某月某日，判断这一天是这一年的第几天？
year=int(input('请输入年份：'))
month=int(input('请输入月份：'))
day=int(input('请输入天数：'))
days=0
months=[0,31,59,90,120,151,181,212,243,273,304,334]
if 0<month<=12:
    days=months[month-1]
else:
    print('请输入正确的月份') #无法在输入错误后直接中止

days+=day

if (year%4==0) or (year%400==0) and (year%100!=0):
    if month>2:
        days+=1
print('这一天是这一年的第{}天'.format(days))

#3：输入三个整数x,y,z，请把这三个数由小到大输出。

#第一种
x=int(input('请输入第一个数字：'))
y=int(input('请输入第二个数字：'))
z=int(input('请输入第三个数字：'))

if (x<y):
    if(x<z):
        if (y<z):
            print(x,y,z)
        else:
            print(x,z,y)
    else:
        print(z,x,y)
else:
    if(z<x):
        print(z,x,y)
    else:
        if(y<z):
            print(x,y,z)
        else:
            print(x,z,y)

#第二种
x=int(input('请输入第一个数字：'))
y=int(input('请输入第二个数字：'))
z=int(input('请输入第三个数字：'))
rank=[x,y,z]
index=0
while index<2:
    if rank[index]>rank[index+1]:
        l=rank[index]
        rank[index]=rank[index+1]
        rank[index+1]=l
    index+=1
print(rank)

