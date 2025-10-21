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
    