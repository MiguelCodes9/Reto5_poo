from shape import Shape
from line import Line 
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
    