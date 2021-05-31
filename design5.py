import turtle

numSides = int(input("I will draw a series of rotated polygons. How many sides should each polygon have?"))
numPolygons = int(input("How many of those polygons should I draw?"))
print("Please click on the 'result' tab above to see the drawing")

s = turtle.Screen()
t = turtle.Turtle()

t.speed(0)  # draw fast so we're not waiting too long

for i in range(numPolygons):  # repeat for each polygon
    # rotate just enough so they will be distributed evenly in a cirle of rotation:
    t.right(360 / float(numPolygons))
    for j in range(numSides):  # draw a regular polygon
        t.forward(100)
        t.left(360 / float(numSides))

s.exitonclick()