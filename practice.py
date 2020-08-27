#查看python中的保留字
import keyword
print(keyword.kwlist)

#字符串的切片操作 [头下标：尾下标：步长]
str='hello world'
print(str[0:4:2])

# 不换行输出
x='a'
y='b'
print(x, end=" ")
print(y, end=" ")
print() #默认换行输出

#模块导入
'''
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''

#Python3 的六个标准数据类型中：
#不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
#可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）


#查询变量所指的对象的类型 type()  isinstance()
a='gggg'
b=[1,2]
print(type(a),type(b))
print(isinstance(a,int))

#type isinstance的区别
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
class A:
    pass
class B:
    pass
print(isinstance(A(),A))
print(type(A())==A)
print(isinstance(B(),A))
print(type(B())==A)

#数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
print(15/2)
print(15//2)

#复数由实数部分和虚数部分构成，可以用a + bj
#complex(a,b)表示， 复数的实部a和虚部b都是浮点型

#列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
#和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
#列表中的元素是可以改变的
li=[1,45,'abf',[1232,'yui']]
print('{}'.format(li[0:3]))

#元组（tuple）,元组的元素不能修改,但它可以包含可变的对象，比如list列表。
#元组写在小括号 () 里，元素之间用逗号隔开。
#元组中的元素类型也可以不相同
tuple=(34,'fgr',34.2)
print(tuple[::-1]) # -1为从末尾开始

#构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号


#string、list 和 tuple 都属于 sequence（序列）

#列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
#键(key)必须使用不可变类型。
#在同一个字典中，键(key)必须是唯一的。
dict={'name':'runoob','age':24}
print(dict)

'''
数字类型
如果改变数字数据类型的值，将重新分配内存空间
int(x) 将x转换为一个整数。
float(x) 将x转换到一个浮点数。
complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
'''
a=34
print(float(a))
print(complex(a))

