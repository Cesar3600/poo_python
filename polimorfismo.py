
class Animal():
  def sonido(self):
    pass

class Gato:
  def sonido(self):
    return 'miau'
  
class Perro:
  def sonido(self):
    return 'guauuu'    

def hacer_sonido(animal):
  print(animal.sonido())

#aplicando polimorfismo

gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())


#esta es otra forma de ahcer polimorfismo

hacer_sonido(gato)
hacer_sonido(perro)

#polimorfismo de cohersion

num1 = 3
num2 = 4.4

resultado = num1 + num2

print(resultado)
print(type(resultado))


def recorrer(elemento):
  for item in elemento:
    print(f'El elemento actual es {item}')
    

lista1 = [1,2,3,4]
lista2 = "maquina" 

recorrer(lista1)
recorrer(lista2)




