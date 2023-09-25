
#getter y setters
class Persona:
  def __init__(self,nombre,edad):
    self.__nombre = nombre
    self.__edad = edad
  
  def get_nombre(self):
    return self.__nombre

  def get_edad(self):
    return self.__edad

  def set_nombre(self,nombre):
    self.__nombre = nombre

  def set_edad(self,edad):
    self.__edad = edad


persona = Persona("Cesar",21)

persona.set_nombre('Arthur')
nombre = persona.get_nombre()
edad = persona.get_edad()

print(f'soy {nombre} y tengo {edad} de edad')


