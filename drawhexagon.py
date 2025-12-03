import turtle

# To create the canvas.
pen = turtle.Turtle()


# Define functionto drawa a green hexagon.
def drawhexagon(hexalength):
    pen.color("green")
    pen.fillcolor("green")
    pen.begin_fill()

    for x in range(6):

        pen.forward(hexalength)
        pen.left(300)

    pen.end_fill()


hexalength=int(input("Enter the hexal length of your hexagon"))

# Define where on the canvas to draw the hexagon.
pen.up()
pen.setposition(-250,100)
pen.down()

drawhexagon(hexalength)