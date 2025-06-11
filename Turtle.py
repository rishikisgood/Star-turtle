import turtle
turtle.Screen() .bgcolor("light blue")
turtle.Screen() .setup(300, 400)
polygon= turtle.Turtle()

num_sides= int(input("Please Enter a Number of sides: "))
side_length= 80
angle=360/num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

