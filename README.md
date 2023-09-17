
# POO CON PYTHON

## **CONCEPTO**

Ayuda a programar de una manera mas entendible, modificable, modularizable
Se utiliza objetos para la programacion orientada a objetos.



## **DESVENTAJAS DE NO USAR POO**



## **CLASES Y OBJETOS** 

un atributo es una propiedad de un objeto, por ejemplo marca o modelo
en el ejemplo los atributos son fijos  estaticos

```py
class Celular():
  marca  = 'Apple'
  modelo = 'MAX'

cel1 = Celular()
print(cel1) 
# se refiere a que se creo un objeto celular en la posicion 0x000002B84AE2BDC0
#<__main__.Celular object at 0x000002B84AE2BDC0>


```
### instancia de una clase
 basicamente es objeto

## **ATRIBUTOS**
son variables

self referencia a si mismo
>[!WARNING]
>__init__ es una funcion que se ejecuta automaticamente
> es una funcion que se ejcuta automaticamente

```py
class Celular:
  def __init__(self,marca,modelo,camara):
    self.marca = marca
    self.modelo = modelo
    self.camara = camara

celular1 = Celular("samsung","s24","33mp")

print(celular1.marca)  # samsung
print(celular1.modelo) # s24
print(celular1.camara) # 33mp
```

## **METODOS**
es una funcion creada dentro de una clase
los metodos sirven para definir las acciones que puede hacer nuestro objeto

>[!WARNING]
>self sirve para autoreferenciar y 
>nececita la f para el formato en print

```py
class Celular:
  def __init__(self, marca, modelo, camara):
    self.marca = marca
    self.modelo = modelo
    self.camara = camara

  def llamar(self):
    print(f'estas haciendo un llamado desde un telefono {self.marca}')

  def cortar(self):
    print(f"cortaste la llamada desde el telefono {self.marca}")
  

celular1 = Celular("Samsung","s24","33MB")
print(celular1.llamar())  # cortaste la llamada
```









