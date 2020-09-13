import turtle
# 设置画笔属性
turtle.speed(2)
turtle.pensize(4)
turtle.pencolor('blue')
turtle.fillcolor('blue')
# 画矩形,填充颜色
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()
# 隐藏画笔形状
turtle.ht()

turtle.mainloop()
# 启动事件循环 -调用Tkinter的mainloop函数。
# 必须是乌龟图形程序中的最后一个语句。