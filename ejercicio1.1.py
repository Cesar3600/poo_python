
#PRACTICA

class Estudiante():
  def __init__ (self,nombre,edad,grado):
    self.nombre = nombre
    self.edad = edad
    self.grado = grado
    
  def estudiar(self):
    print(f"El estudiante {self.nombre} esta estudiando, tiene {self.edad} de edad y cursa el {self.grado} grado")


nombre = input("Digame su nombre")
edad = input("Digame su edad")
grado = input("Digame su grado")


est = Estudiante(nombre,edad,grado)
est.estudiar()





