import turtle

BACKGROUND_COLOR="#9EC388"
CRUST_COLOR="#ECA84F"
SAUCE_COLOR="#AD0509"
CHEESE_COLOR="#FBC70F"
PEPPERONT_LOCATIONS=[
    [-70,105],
    [-80,175],
    [-25,50],
    [-15,100],
    [-25,150],
    [-30,205],
    [15,50],
    [20,120],
    [30,200],
    [60,156],
    [71,215],
    [80,90],
    [100,150],
]

screen=turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Pizza Hut")

my_tut=turtle.Turtle()
my_tut.pensize(2)
my_tut.shape("circle")

def draw_circle(radius,line_color,fill_color):
 my_tut.color(line_color)
 my_tut.fillcolor(fill_color)
 my_tut.begin_fill()
 my_tut.circle(radius)
 my_tut.end_fill()

def move_turtle(x,y):
 my_tut.up()
 my_tut.goto(x,y)
 my_tut.down()

draw_circle(150,CRUST_COLOR,CRUST_COLOR)
move_turtle(0,25)
draw_circle(125,SAUCE_COLOR,CHEESE_COLOR) 

for location in PEPPERONT_LOCATIONS:
    move_turtle(location[0],location[1])
    draw_circle(10,SAUCE_COLOR,SAUCE_COLOR)

move_turtle(0,150)
my_tut.color(BACKGROUND_COLOR)

for x in range(0,8):
 my_tut.pendown()
 my_tut.left(45)
 my_tut.forward(150)
 my_tut.penup()
 my_tut.backward(150)


turtle.done()
    
