from turtle import Turtle, Screen
import random
size=int(input("Size:"))
tim=Turtle()
tim.shape("turtle")
screen=Screen()
screen.colormode(255)
for n in range(3, 11):
    r=random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor((r, g, b))
    an=360/n
    for _ in range(n):
        tim.forward(100)
        tim.right(an)
screen.clear()
screen.colormode(255)
tim.speed("fastest")
tim.pensize(7)
for _ in range(200):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor((r, g, b))
    dir=random.choice([90, 180, 270, 360])
    tim.right(dir)
    tim.forward(30)
screen.clear()
screen.colormode(255)
def draw(size):
    for n in range(int(360/size)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tim.pencolor((r, g, b))
        tim.circle(100)
        tim.setheading(tim.heading()+size)

draw(size)
screen.exitonclick()
