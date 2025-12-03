# To import the turtle module.
import turtle

# To create the canvas.
pen = turtle.Turtle()

# Define function to draw a blue square.
def drawSquare(sqlength):
    pen.color("blue")
    pen.fillcolor("blue")
    pen.begin_fill()

    for x in range(4):

        pen.forward(sqlength)
        pen.right(90)

    pen.end_fill()

# Request user input for the sizes of the shapes.
sqlength=int(input("Enter the length of your square"))

# Define where in the canvas to draw the square.
pen.up()
pen.setposition(150,150)
pen.down()

drawSquare(sqlength)
