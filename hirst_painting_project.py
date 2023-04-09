import colorgram,turtle as t 
import random
colors = colorgram.extract('hirst_painting.jpg',30)  # return a list of color objects which let you access rgb, hsl and the proportion of the image was that color

# first_color = colors[0]
# rgb = first_color.rgb  #tuple
# hsl = first_color.hsl  #tuple

# proportion = first_color.proportion

#print(rgb) ==> Rgb(r=246, g=243, b=239)



# rgb_colors =[]
# for color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     rgb = (r,g,b)
#     rgb_colors.append(rgb)

screen = t.Screen()
screen.colormode(255)
screen.mode('world')




extracted_color_lists = [(246, 243, 239), (247, 241, 244), (202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]


#initialize a turtle :
tim = t.Turtle()

tim.shape('turtle')

tim.color('DeepPink')





def draw_dot():
    
    for _ in range(7):
        color = random.choice(extracted_color_lists)
        tim.dot(20,color)
        tim.penup()
        tim.forward(50)
        tim.dot(20,color)

#0-east, 90-north, 180-west, 270-south



def hist_painting():

    for _ in range(7):
        tim.setheading(90) 
        draw_dot()
        tim.setheading(180)
        tim.penup()
        tim.forward(50)
        tim.setheading(270)
        draw_dot()
        tim.setheading(180)
        tim.penup()
        tim.forward(50)

hist_painting()
    








      

                
       


        

       









screen.exitonclick()
