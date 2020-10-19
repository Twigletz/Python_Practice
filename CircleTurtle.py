import math # need for math.pi for circle maths
import turtle # need for turtle!
  
# Set up Turtle and window
turtle.setup(700, 700)  # Determine the window size
wn = turtle.Screen()  # Get a reference to the window
wn.title("Circle Sectors")  # Change the window title
wn.bgcolor("black")  # Set the background color
t = turtle.Turtle()  # Create the turtle
t.color("white")

# define some functions for drawing things with the turle easily 
def draw_circle(radius):
    t.setheading(90) # faces the turtle up/north

def draw_sector(radius, angle):
    t.setheading(90) # faces the turtle up/north

def draw_text(message):
    t.penup()
    t.goto(100,200)
    style = ('Courier', 16)
    t.color('deep pink')
    t.write(message, font=style, align='center')
    t.hideturtle()
                            
def get_radius():
    while True:
        try:
            return float(input("Radius? "))
        except:
            print('That isn\'t a number, please try again!')

def get_angle():
    while True:
        try:
            return float(input("Sector Angle? "))
        except:
            print('That isn\'t a number, please try again!')

# Funcions defined, lets get some input from user.
radius = get_radius()
arc_angle = get_angle()
# extra bit of error handling for values over 360°,where the sector area 
# becomes greate than the area of teh full circle:
while arc_angle > 360:
    print("Sector Angle must not be more than 360°")
    arc_angle = get_angle()

#-----------------------
# This section does the maths bit.

# Finds proportion
proportion = arc_angle / 360

# Finds area
area = math.pi * (radius**2)
rounded_area = round(area, 3)

# Finds circumference
circumference = (2 * math.pi) * radius
rounded_circumference = round(circumference, 3)

# Finds sector area
sector_area = area * proportion
rounded_sector_area = round(sector_area, 3)

# Finds arc length
arc_length = circumference * proportion
rounded_arc_length = round(arc_length, 3)

#-----------------------
# This section prints the answers to the console.
print("Answers:")
print("Area = ", area)
print("Circumference = ", circumference)
print("Sector area = ", sector_area)
print("Arc Length = ", arc_length)

# Print rounded answers
print("Rounded values:")
print("Area = ", rounded_area)
print("Circumference = ", rounded_circumference)
print("Sector area = ", rounded_sector_area)
print("Arc Length = ", rounded_arc_length)

# Bundle all of that into a string to send to our turtle
message = "build you message here"


# Now draw!
draw_circle(100)                # draw the cirles - using 100 for radius because it fits the screen nicely
draw_sector(100, arc_angle)     # draw the secrot part and fill it in
draw_text(message)              # write the message

turtle.done()                   # allow click to exit