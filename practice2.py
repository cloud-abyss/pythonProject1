#1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
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
        rank[index],rank[index+1]=rank[index+1],rank[index]
    index+=1
print(rank)
'''
# #4.斐波那契数列
# #斐波那契数列就是将前两个数字相加会得到第三个数字
# #迭代
# n=int(input('请输入想要斐波那契数：'))
# def feib(n):
#     if (n==1 or n==2):
#         return 1
#     else:
#         return feib(n-1)+feib(n-2)
# print(feib(n))
#
# #循环
# def fib(n):
#     a, b = 1, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     return a
#
# print(fib(3))

# #题目5：将一个列表的数据复制到另一个列表中。
# c1=[1,2,'tec','lll']
# c2=c1.copy()
# print(c2)

# #题目6：输出 9*9 乘法口诀表。
# # 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
# for r in range(1,10):
#     for c in range(1,r+1):
#         print('{}*{}={}'.format(r,c,r*c),end='\t')
#     print('\n')

# #题目7：暂停一秒输出。
# #程序分析：使用 time 模块的 sleep() 函数。
# import time
#
# dict1={1:'a',2:'b',3:'c'}
# for key,value in dict.items(dict1):
#     print(value)
#     time.sleep(2)

