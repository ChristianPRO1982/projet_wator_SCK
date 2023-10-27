import turtle

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y =y
    
class RectangleMap:
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2

class DessinMap:
    def __init__(self,rectangle_map):
        self.rectangle_map= rectangle_map
        self.dessiner_rectangle()

    def dessiner_rectangle(self):
        myturtle = turtle.Turtle()
        myturtle.penup()
        myturtle.goto(self.rectangle_map.point1.x,self.rectangle_map.point1.y)
        myturtle.pendown()
        largeur = self.rectangle_map.point2.x-self.rectangle_map.point1.x
        longueur = self.rectangle_map.point2.y-self.rectangle_map.point1.y
        myturtle.forward(largeur)
        myturtle.left(90)
        myturtle.forward(longueur)
        myturtle.left(90)
        myturtle.forward(largeur)
        myturtle.left(90)
        myturtle.forward(longueur)
        turtle.done()
       

A=Point(-700,-300)
B=Point(700,300)
C= Point(0,0)
D= Point(10,10)

rectangle = RectangleMap(A,B)
dessin = DessinMap(rectangle)
rectangle2= RectangleMap(C,D)
dessin2 = DessinMap(rectangle2)
print(dessin2)

turtle.done()







