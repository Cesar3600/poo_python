
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

## **HERENCIA**
>[!WARNING]
>Permite a la clase hija acceder a los metodos y tener las propiedades de la clase padre 
>

```py
class Persona:
  def __init__(self,nombre,edad,nacionalidad):
    self.nombre = nombre
    self.edad=edad
    self.nacionalidad=nacionalidad
    

class Estudiante(Persona):
  def __init__(self,nombre,edad,nacionalidad,id_estudiante,t_estudio,institucion_educativa):
    super().__init__(nombre,edad,nacionalidad)
    self.id_estudiante = id_estudiante
    self.t_estudio = t_estudio
    self.institucion_educativa = institucion_educativa
  def mensaje(self):
    return f'La estudiante {self.nombre} es excepcionalmente inteligente y tiene un gran futuro'



estudiante = Estudiante('Mikaela',1,'Peruana',33,'medicina','Cayetano Heredia')

print(estudiante.mensaje())

```
### ejemplo:

```py
class Citizen:
  def __init__(self,dni,name,lastname):
    self.dni=dni
    self.name=name
    self.lastname=lastname
  def show_citizen(self):
    return f'nombre:{self.name}'
    

class Worker(Citizen):
  def __init__(self,dni,name,lastname,charge,salary):
    super().__init__(dni,name,lastname)
    self.charge=charge
    self.salary=salary
  def show_worker(self):
    return f'me llamo {self.name} {self.lastname}, mi dni es {self.dni} trabajo como {self.charge} y gano {self.salary}'
  
  
worker =  Worker(10620349,'Cesar','Contreras','Programador fullStack','5000 EUR')

print(worker.show_worker())
```

```py
class Citizen:
  def __init__(self,dni,name,lastname):
    self.dni=dni
    self.name=name
    self.lastname=lastname
  def show_citizen(self):
    return f'nombre:{self.name}'
    

class Worker(Citizen):
  def __init__(self,dni,name,lastname,charge,salary):
    super().__init__(dni,name,lastname)
    self.charge=charge
    self.salary=salary
  def show_worker(self):
    return f'Me llamo {self.name} {self.lastname}, mi dni es {self.dni} trabajo como {self.charge} y gano {self.salary}'
  
  
worker =  Worker(10620349,'Cesar','Contreras','Programador fullStack','5000 EUR')


class Student(Citizen):
  def __init__(self,dni,name,lastname,id_student,faculty,year_init):
    super().__init__(dni,name,lastname)
    self.id_student = id_student
    self.faculty = faculty
    self.year_init = year_init
  def student_msg(self):
    return f'me llamo {self.name} {self.lastname} y estudio en la facultad de {self.faculty}'    
    


print(worker.show_worker())

student_data = Student(10620349,'Cesar','Contreras','10033','Informatica','2020')

print(student_data.student_msg())

```

### HERENCIA MULTIPLE


```py
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
```

>[issubclass]
>sirve para saber si una clase es subclase de otra
>```py
>is_subclase = issubclass(EmpleadoArtista,Persona)
>print(is_subclase)
>```

>[isinstance]
>Devuelve un booleano si un objeto es una instancia de una clase
>```py
>is_instance = isinstance(empleado,EmpleadoArtista)
>print(is_instance)
>```

