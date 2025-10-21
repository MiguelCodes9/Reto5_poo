import math
from shape import Shape
from line import Line



class Triangle(Shape):
    def __init__(self,vertices):
        edges=[
            Line(vertices[0],vertices[1]),
            Line(vertices[1],vertices[2]),
            Line(vertices[2],vertices[0]),
        ]
        super().__init__( vertices, edges,is_regular=False)
        self.compute_inner_angles()
    #Formas generales para calcular perimetro ya rea
    def compute_perimeter(self):
        count_length=0
        for edge in self.get_edges():
            count_length+= edge.get_length()
        return count_length
    
    def compute_area(self):
        a = self.get_edges()[0].get_length()
        b = self.get_edges()[1].get_length()
        c = self.get_edges()[2].get_length()
        s = self.compute_perimeter()/2 
        t_area = (s*(s-a)*(s-b)*(s-c))**0.5
        return t_area
    #Para cada clase hay un metodo especifico para calcular sus angulos
    def compute_inner_angles(self):
         raise NotImplementedError("Cada tipo de triángulo debe implementar su propio cálculo de ángulos")
    #De aqui para abajo cada tipo de triangulo hereda los atributos de Triangle , lo unico que cmabia es la forma de calcular los angulos
class Equilateral(Triangle):
    def __init__(self,vertices):
        super().__init__(vertices)
        self.set_is_regular(True)
        self.compute_inner_angles()

    def compute_inner_angles(self):
        self.set_inner_angles([60,60,60])
        return self.get_inner_angles()

class Isosceles(Triangle):
    def __init__(self,vertices):
        super().__init__(vertices)
        self.set_is_regular(False)
        self.compute_inner_angles()

    def compute_inner_angles(self):
        a = self.get_edges()[0].get_length()
        b = self.get_edges()[1].get_length()
        c = self.get_edges()[2].get_length()  
        A_angle = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        B_angle = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        C_angle = 180 - A_angle - B_angle  
        angles=[A_angle,B_angle,C_angle]
        self.set_inner_angles(angles)
        return angles

class Scalene(Triangle):
    def __init__(self,vertices):
        super().__init__(vertices)
        self.set_is_regular(False)
        self.compute_inner_angles()

    def compute_inner_angles(self):
        a = self.get_edges()[0].get_length()
        b = self.get_edges()[1].get_length()
        c = self.get_edges()[2].get_length()
        A_angle = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        B_angle = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        C_angle = 180 - A_angle - B_angle  
        angles=[A_angle,B_angle,C_angle]
        self.set_inner_angles(angles)
        return angles

    
class RectTriangle(Triangle):
    def __init__(self,vertices):
        super().__init__(vertices)
        self.set_is_regular(False)
        self.compute_inner_angles()
    def compute_inner_angles(self):

        a = self.get_edges()[0].get_length()
        b = self.get_edges()[1].get_length()
        c = self.get_edges()[2].get_length()

        ordered_sides=sorted([a,b,c])
        leg1,leg2,hypotenuse= ordered_sides 
        A_angle = math.degrees(math.asin(leg1 / hypotenuse))
        B_angle = math.degrees(math.asin(leg2 / hypotenuse))
        C_angle = 90.0  
        
        new_angles=[A_angle, B_angle,C_angle]
        self.set_inner_angles(new_angles)
        return new_angles
