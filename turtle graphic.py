from turtle import Turtle,Screen,TurtleScreen
import random


#initialize a turtle
turtle_jimmy = Turtle()
turtle_jimmy.shape('turtle')
turtle_jimmy.pensize(3)
turtle_jimmy.speed('fastest')

#screen setup 
screen = Screen()
screen.colormode(255)
screen.title('welcome to the turtle zoo')

# define a function generating a random color
def random_colors():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)

    color = (r,g,b)
    return color




# 1st challenge : run in a square area
def run_square():
    for _ in range(4):
        turtle_jimmy.forward(100)
        turtle_jimmy.right(90)




# 2rd challenge : drawing dashed line 
def run_in_dashed_line():
    for i in range(50):
        
        
        turtle_jimmy.forward(10)
        turtle_jimmy.penup()
        turtle_jimmy.forward(10)
        turtle_jimmy.pendown()




#3rd challenge : drawing 


#colors =["#B2A4FF","#FFB4B4","#50514F","#FDF7C3","#6096B4","#93BFCF","#BDCDD6","#EEE9DA"]



def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        
        turtle_jimmy.forward(100)
        turtle_jimmy.right(angle)
def draw_many_shapes(numsides):

    while num_sides <=8:
        turtle_color = random.choice(colors)
        turtle_jimmy.color(random_colors())
        draw_shape(num_sides)
        num_sides = num_sides + 1
            


#4thchallenge : random walk turtle

#colors =["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen","DeepPink","DeepSkyBlue"]

def random_walk():

    directions =[0,90,180,270]

    for _ in range(200):
        
        turtle_jimmy.color(random_colors())
        turtle_jimmy.pensize(10)
        turtle_jimmy.speed('fast')


        if(-3000<turtle_jimmy.xcor()<3000 and -3000<turtle_jimmy.ycor()<3000): #check the limited area turtle can move
                
            turtle_jimmy.forward(30)
            turtle_jimmy.setheading(random.choice(directions))
        else:
            
            turtle_jimmy.backward(30)
            turtle_jimmy.setheading(random.choice(directions))















#5th challenge: make a spirograph
def draw_spirograph(size_of_gap):

    for _ in range( int(360/ size_of_gap)):
        
        turtle_jimmy.color(random_colors())
        turtle_jimmy.circle(120)
        current_heading = turtle_jimmy.heading()
        turtle_jimmy.setheading(current_heading+size_of_gap) #tilt the direction of turtle
        










def draw_star():

    for _ in range(500):
        turtle_jimmy.color(random_colors())
        turtle_jimmy.forward(200)
        turtle_jimmy.left(170)
        if abs(turtle_jimmy.position())<1:
            break















screen.exitonclick()






































