from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height= 400)

user_bet = screen.textinput(title ='Make your bet', prompt='which turtle will win the race? Enter a color : ')

colors =['red','orange','yellow','green','blue','purple']

def create_turtles():
    turtles =[]
    position=0
    for color in colors:
        new_turtle =  Turtle(shape='turtle')
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230,y=-120+position)
    
        position=position+50
        turtles.append(new_turtle)

    return turtles



turtles = create_turtles()





def race():
    is_race_on = True


    while is_race_on:
        distances =[10,50,30,20,65]
    
        for turtle in turtles:
           if turtle.xcor() >= 200:
                is_race_on = False
                winning_color = turtle.color()
                if winning_color== user_bet:
                    print('congrats! your bet is right')
                else:
             
                    print('your bet is wrong , turtle with color {} has won'.format(turtle.pencolor()))
                
                break
           else:
                turtle.forward(random.choice(distances))
            
                
       
        

race()














screen.exitonclick()
    