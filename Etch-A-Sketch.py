from turtle import Turtle, Screen
import random

tim =  Turtle()
tim.shape('turtle')
tim.color('DeepPink')

screen = Screen()
screen.title('Etch A Sketch')
screen.colormode(255)


def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    rgb= (r,g,b)
    return rgb


def run_forward():
    color = random_color()
    tim.pencolor(color)
    tim.forward(50)

def run_backward():
    color = random_color()
    tim.pencolor(color)
    tim.backward(50)

def turn_left():
    color = random_color()
    tim.pencolor(color)
    tim.left(10)

def turn_right():
    color = random_color()
    tim.pencolor(color)
    tim.right(10)

def clear_drawing():
    tim.clear()
   
    tim.penup()
    tim.home()
    tim.pendown()








screen.listen()
screen.onkey( key='w', fun= run_forward)
screen.onkey( key='s', fun= run_backward)
screen.onkey( key='a', fun= turn_left)
screen.onkey( key='d', fun= turn_right)
screen.onkey( key='c', fun= clear_drawing)










screen.exitonclick()