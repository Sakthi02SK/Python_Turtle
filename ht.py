from turtle import *
hideturtle()
speed(1)
bgcolor("pink")
begin_fill()
fillcolor("red")
pensize(8)
lt(135),fd(150)
circle(-70,190),lt(110)
circle(-70,190),fd(150)
end_fill(),up()
rt(135),fd(100),lt(90)
fd(60),rt(115),down(),pensize(5),pencolor("white")
fd(50),rt(135),fd(50),bk(25)
rt(110),fd(14),up(),bk(80),lt(90)
down(),fd(30),bk(57),lt(90)
circle(-15,180),rt(180)
circle(-15,180)
mainloop()