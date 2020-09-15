# 判断年份是否为闰年
year=int(input('请输入年份：'))
if year%4==0 and year%100!=0 or year%400==0:
    print('%d 年是闰年'%year)
else:
    print('%d 年不是闰年'%year)