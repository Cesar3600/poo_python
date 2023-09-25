
#herencia y herencia multiple

class Persona:
  def __init__(self,nombre,edad,nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad
    
  def hablar(self):
    print("hola estoy hablando un poco")
    
class Artista:
  def __init__(self,habilidad):
    self.habilidad = habilidad

  def mostrar_habilidad(self):
    return f"mi habilidad es {self.habilidad}"
    
class EmpleadoArtista(Persona,Artista):
  def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
    Persona.__init__(self,nombre,edad,nacionalidad)
    Artista.__init__(self,habilidad)
    self.salario = salario
    self.empresa = empresa
    
  def mostrar_habilidad(self):
    return f'no tengo habilidad'
  
  def presentarse(self):
    return f'{self.mostrar_habilidad()}'
    

empleado = EmpleadoArtista("Cesar","46","Peruana","Programador",18000,"Amazon")
print(empleado.presentarse())


is_subclase = issubclass(EmpleadoArtista,Persona)
print(is_subclase)


is_instance = isinstance(empleado,EmpleadoArtista)
print(is_instance)