import math
#Se importa math por que se necesita para realizar varias operaciones matematicas
#La clase punto y linea es lo mas basico para la clase forma, en general se ponen setters y getters en todo el codigo para encpsulamiento
class Point:
    def __init__(self, x:int, y:int ):
        self._x= x
        self._y= y
    def get_x(self):
        return self._x
    
    def set_x(self, x):
        self._x = x
    
    def get_y(self):
        return self._y
    
    def set_y(self, y):
        self._y = y

    def compute_distance(self,Secondpoint):
        distance_x=self._x- Secondpoint.get_x()
        distance_y=self._y- Secondpoint.get_y()
        return (distance_x**2+distance_y**2)**0.5 #Se usa pitagoras
    
    #Esta clase utiliza la clase punto y uno de sus metodos para crear lineas
class Line:
    def __init__(self, start_point:Point,end_point:Point) :
        self._start_point=start_point
        self._end_point=end_point
        self._length=start_point.compute_distance(end_point)
    
    def get_start_point(self):
        return self._start_point
    
    def set_start_point(self,start_point):
        self._start_point=start_point
        self._length=start_point.compute_distance(self._end_point)

    def get_end_point(self):
        return self._end_point
    
    def set_end_point(self, end_point):
        self._end_point=end_point
        self._length=self._start_point.compute_distance(self._end_point)
    
    def get_length(self):
        return self._length
    
    def __str__(self):
        return f"Line(length: {self._length:.2f})"

#Clase madre de donde parten las demas clases 
class Shape():
  
    def __init__(self, vertices, edges, is_regular=False, inner_angles=None):
        self._is_regular = is_regular
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles if inner_angles is not None else [] # si inner_angles fue pasado como argumento se usa tal cual.
         #Si no se pasó nada (None), se inicializa _inner_angles como una lista vacía [].
    
    def get_is_regular(self):
        return self._is_regular
    
    def set_is_regular(self,is_regular):
        self._is_regular=is_regular

    def get_vertices(self):
        return self._vertices  
    
    def set_vertices(self,vertices):
        self._vertices = vertices

    def get_edges(self):
        return self._edges 
    
    def set_edges(self,edges):
     self._edges = edges 
 
    def get_inner_angles(self):
        return self._inner_angles
    
    def set_inner_angles(self,inner_angles):
        self._inner_angles=inner_angles 
  #Cada clase tiene su forma de calcular esto
    def compute_area(self):
     raise NotImplementedError("Este método debe ser implementado por la subclase.")
    
    def compute_perimeter(self):
      raise NotImplementedError("Este método debe ser implementado por la subclase.")
    
    def compute_inner_angles(self):
      raise NotImplementedError("Este método debe ser implementado por la subclase.")
    #Clase reangulo, hereda atributos de shape
class Rectangle(Shape):
    def __init__(self,vertices):
        #Aqui accede a los vertices utilizando la posicion de la lista que ha sido asignada
        edges= [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[3]),
            Line(vertices[3], vertices[0])  
        ]
        inner_angles=[90,90,90,90]
        super().__init__(vertices, edges, is_regular=False,inner_angles=inner_angles)

        

    def compute_area(self):
        width = self.get_edges()[0].get_length()
        height= self.get_edges()[1].get_length()
        return width * height
    
    def compute_perimeter(self):
        count_length=0
        for edge in self.get_edges():
            count_length+= edge.get_length()
        return count_length
    #Para rectangle y square no es necesario calcular angulos ya que son fijos (90°)
    def compute_inner_angles(self):
        return self.get_inner_angles()
    
class Square(Rectangle):
    def __init__(self,vertices):
        super().__init__(vertices) #Lo unico que cambio respecto a rectangle es que es regular 
        self.set_is_regular(True)

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
