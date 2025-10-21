
from point import Point 
from rect import Rectangle , Square
from triangle import Isosceles, Scalene, Equilateral , RectTriangle 


if __name__ == "__main__":
  #Para imprimir es muy parecido, solamente hay que llamar la variable y funcion especifica
  print("----------|FUNCIONAMIENTO DE LAS CLASES|----------")

  print("---------->   1.Rectangulo de 6x4    ")
  rectangle_points=[
      Point(0,0),
      Point(6,0),
      Point(6,4),
      Point(0,4)
  ]
  Rectangulo=Rectangle(rectangle_points)
  print(" Area =", Rectangulo.compute_area())
  print(" Perimetro =", Rectangulo.compute_perimeter())
  print(" Angulo =", Rectangulo.compute_inner_angles())
  print(" ¿Es regular?", Rectangulo.get_is_regular())

  print("---------->   2. Cuadrado de 3x3    ")
  square_points=[
      Point(0,0),
      Point(3,0),
      Point(3,3),
      Point(0,3),
      
  ]
  Cuadradito=Square(square_points)
  print(" Area =", Cuadradito.compute_area())
  print(" Perimetro =", Cuadradito.compute_perimeter())
  print(" Angulo =", Cuadradito.compute_inner_angles())
  print("¿Es regular?", Cuadradito.get_is_regular())

  print("---------->   3. Triangulo Isosceles   ")
  triangulo1_points=[
      Point(-3,0),
      Point(3,0),
      Point(0,4),
  ]
  Triangulo1=Isosceles(triangulo1_points)
  print(" Area =", Triangulo1.compute_area())
  print(" Perimetro =", Triangulo1.compute_perimeter())
  print(" Angulo =", Triangulo1.compute_inner_angles())
  print("¿Es regular?", Triangulo1.get_is_regular())

  print("---------->   4. Triangulo Escaleno   ")
  triangulo2_points=[
      Point(0,0),
      Point(7,0),
      Point(4.15, 4.46)
          ]
  Triangulo2=Scalene(triangulo2_points)
  print(" Area =", Triangulo2.compute_area())
  print(" Perimetro =", Triangulo2.compute_perimeter())
  print(" Angulo =", Triangulo2.compute_inner_angles())
  print("¿Es regular?", Triangulo2.get_is_regular())
  
  print("---------->   5. Triangulo Equilatero  ")
  triangulo3_points=[
      Point(0,0),
      Point(6,0),
      Point(5.0, 5.196)
          ]
  Triangulo3=Equilateral(triangulo3_points)
  print(" Area =", Triangulo3.compute_area())
  print(" Perimetro =", Triangulo3.compute_perimeter())
  print(" Angulo =", Triangulo3.compute_inner_angles())
  print("¿Es regular?", Triangulo3.get_is_regular())
  
  print("---------->   5. Triangulo Rectangulo ")
  triangulo4_points=[
      Point(0,0),
      Point(6,0),
      Point(0,4)
          ]
  Triangulo4=RectTriangle(triangulo4_points)
  print(" Area =", Triangulo4.compute_area())
  print(" Perimetro =", Triangulo4.compute_perimeter())
  print(" Angulo =", Triangulo4.compute_inner_angles())
  print("¿Es regular?", Triangulo4.get_is_regular())
  