import turtle as t
import time as ti
import random as rd
t.bgcolor('yellow')

caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf=t.Turtle()
leaf_shape=((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

score=t.Turtle()
score.speed(0)
score.hideturtle()

game_started=False
text_turtle=t.Turtle()
text_turtle.write('press space to start',align='center')
text_turtle.hideturtle()


def outside_window():
    leftframe=-t.window_width()/2
    rightframe=t.window_width()/2
    topframe=t.window_height()/2
    bottomframe=-t.window_height()/2
    (x,y)=caterpillar.pos()
    outside= x<leftframe or x>rightframe or y>topframe or y<bottomframe
    return outside

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def game_over():
    leaf.color('yellow')
    caterpillar.color('yellow')
    t.penup()
    t.hideturtle()
    t.write("GAME OVER")

def disp_score(current_score):
    score.clear()
    score.penup()
    x=t.window_width()/2-100
    y=t.window_height()/2-100
    score.setpos(x,y)
    score.write(str(current_score),align='right')

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 1
    caterpillar_length = 2
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    disp_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf)<20:
            place_leaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            disp_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()

t.mainloop()
