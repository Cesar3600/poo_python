class Persona:
  def __init__(self,nombre,edad):
    self.nombre = nombre
    self.edad = edad
    
  def mostrar_datos(self):
    print(f'nombre: {self.nombre}') 
    print(f'edad: {self.edad}') 
    
    
class Estudiante(Persona):
  pass
  def __init__(self,nombre,edad,grado):
    super().__init__(nombre,edad)
    self.grado = grado
  
  def mostrar_grado(self):
    print(f'{self.grado}')


estudiante = Estudiante('cesar',45,'quinto')

estudiante.mostrar_datos() 
estudiante.mostrar_grado() 
