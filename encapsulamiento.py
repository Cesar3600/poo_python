

class MiClase:
  def __init__(self):
    self._atributo_privado = "valores"
    

objeto = MiClase()

print(objeto._atributo_privado)



class MiClase:
  def __init__(self):
    self.__atributo_muy_privado = "valores"
  
  def _hablar(self):
    print("Hola, como estas")
  
objeto = MiClase()

print(objeto.__atributo_muy_privado)
print(objeto._hablar())


























