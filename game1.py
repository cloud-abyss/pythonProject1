#根据身高、体重计算BMI
height=float(input('请输入身高：(米)'))
weight=float(input('请输入体重：(kg)'))
BMI=weight/(height**2)
print('BMI的值是：{}'.format(BMI))
if BMI<18.5:
    print('太轻了')
    pass
elif 18.5<=BMI<25:
    print('体重正常')
    pass
elif 25<=BMI<28:
    print('微胖')
    pass
else:
    print('肥胖')
    pass
