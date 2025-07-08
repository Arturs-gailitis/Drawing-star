import turtle

## Function that draws a star
def drawingStar(myTurtle, points, linesize):

    ## Checks if the number of points is 1 or less, which is invalid for a star.
    if points <= 1:

        print('The star points must be more than 1')

        #Ends the programm after error message
        exit()

    # Checks if the number of points is an odd number and proceeds with drawing the star.
    elif points % 2 == 1:

        #Adjusts turtle drawing speed
        myTurtle.speed(10)

        # Loop to draw the star based on the number of points.
        for _ in range(points):

            myTurtle.forward(linesize)

            myTurtle.right(180 - (180 / points))

    # If the number of points is even, prints out error message and exits the program.
    else:

        print('The star points must be odd number')

        exit()

# Try block to prompt the user for input values for points and line size.
try:

    pointcount = int(input('How many points in a star: '))

    linesize = int(input('How big lines shoud be: '))

# Catch any value errors if the input isn't a valid integer.
except ValueError:

    print('Must be an number')

    exit()

# Creates turtle object
t = turtle.Turtle()

# Creates turtle's screen object
scene = turtle.Screen()

# Set up the turtle's screen size.
scene.screensize(linesize + 100, linesize + 100)

drawingStar(t, pointcount, linesize)

# Complete the turtle drawing and close the window.
turtle.done()