# CLASES Y OBJETOS

class Celular():
  marca='apple'
  modelo='max'


cel1 = Celular()
print(cel1) 
# se refiere a que se creo un objeto celular en la posicion 0x000002B84AE2BDC0
#<__main__.Celular object at 0x000002B84AE2BDC0>

class Automovil():
  marca="kia"
  price = 30000

auto = Automovil()
print(auto.price)


# INSTANCIA DE UNA CLASE
class Celular:
  def __init__(self,marca,modelo,camara):
    self.marca = marca
    self.modelo = modelo
    self.camara = camara

celular1 = Celular("Samsung","s24","33MB")
celular2 = Celular("Apple","15","77MB")

print(celular1.marca)  #Samsung
print(celular1.modelo) #S24
print(celular1.camara) #33mp


# METODOS
class Celular:
  def __init__(self,marca,modelo,camara):
    self.marca = marca
    self.modelo = modelo
    self.camara = camara

  def llamar(self):
    print(f'estas haciendo un llamado desde un telefono {self.marca}')

  def cortar(self):
    print(f"cortaste la llamada desde el telefono {self.marca}")
  

celular1 = Celular("Samsung","s24","33MB")
print(celular1.llamar())  # cortaste la llamada

#PRACTICA

class Estudiante():
  def __init__ (self,nombre,edad,grado):
    self.nombre = nombre
    self.edad = edad
    self.grado = grado
    
  def estudiar(self):
    print(f"El estudiante {self.nombre} esta estudiando, tiene {self.edad} de edad y cursa el {self.grado} grado")


est = Estudiante("Carlos","34","3er")
est.estudiar()