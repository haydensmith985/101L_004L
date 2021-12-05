#Hayden Smith, CS101L Inheretence Lab
#This lab will create a series of classes with different abilities from the turtle class which allows for graphics output
#There are classes for points, boxes (filled/not filled) and circles (filled/not filled)

import turtle #importing modules

class Point(): #creating point class
    def __init__(self, x1, y1, color):
        self.x1 = x1
        self.y1 = y1
        self.color = color
    
    def draw(self): #drawing a point
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    
    def draw_action(self):
        turtle.dot()

class Box(Point): #creating box class
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height
    
    def draw_action(self): #method to draw box
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box): #box object with filling
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor
    
    def draw(self): #filling method
        turtle.begin_fill(self.fillcolor)
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point): #circle class
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius
    
    def draw_action(self): #drawing a circle
        turtle.color(self.color)
        turtle.goto(self.x1, self.y1)
        turtle.circle(self.radius)

class CircleFilled(Circle): #making a filled circle object
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor
    
    def draw_action(): #drawing a filled circle
        turtle.goto(self.x1, self.y1)
        turtle.begin_fill(self.fillcolor)
        Circle.draw_action(self)
        turtle.end_fill()








