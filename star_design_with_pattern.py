import turtle 

col = ('yellow','red','orange','white', 'blue','green')

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(30)

for i in range(150):
    t.color(col[i%6]) # choose color from col
    t.forward(i*4) # defined length
    t.left(150) # defined angle
    t.width(4) # defined width of  line
