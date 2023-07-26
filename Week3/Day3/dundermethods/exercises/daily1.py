import turtle

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    
    def perimeter(self):
        return 2*self.radius*3.14    
    
    
    def __add__(self,othercircle: 'Circle'):
        rescircle = self.area + othercircle.area
        return rescircle
    
    def __eq__(self,othercircle: 'Circle'):
         return self.area == othercircle.area
        
    def __gt__(self,othercircle: 'Circle'):
        return self.area > othercircle.area
    
    def __lt__(self,othercircle: 'Circle'):
        return self.area < othercircle.area
        
    def draw(self):
        t = turtle.getscreen
        return t
      
    def circlelisted(self,othercircle:'Circle'):
        CirclesList.append[self]
        CirclesList.append[othercircle]
    
CirclesList = []  
NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
print(Circle)
print(NewCircle.draw)

NewCircle2 = Circle(10)
print(NewCircle2.area())
print(NewCircle2.perimeter())
print(Circle.__add__)
print(Circle.__eq__)
print(Circle.circlelisted)

        
    
