from turtle import*
from Vieleck import*

def draw_simple_flagg(color1, color2, color3):
    speed()
    for color in [color1, color2, color3]:
        fillcolor(color)
        begin_fill()
        rechteck(120,20)
        end_fill()
        pu()
        lt(90)
        fd(20)
        rt(90)
        pd()

reset()
speed(0)

for combination in [["gold", "red", "black"], ["black", "white", "red"], ["orange", "blue", "red"], ["red", "green", "white"]]:
    draw_simple_flagg(combination[0], combination[1], combination[2])
    pu()
    fd(150)
    rt(90)
    fd(60)
    lt(90)
    pd()

mainloop()