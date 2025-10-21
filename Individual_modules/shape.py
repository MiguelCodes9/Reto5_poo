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