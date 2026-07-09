# La version de Python tiene propiedades (atributos) desde la version 1.0.

# Las propiedades en Python
# Propiedades (tambien conocidas como atributos) son variables que pertenecen a un objeto.


class Car:
    def __init__(self, make, model, year):
        self.make = make  # Atributo publico
        self.model = model
        self.year = year


# Crear una instancia de la clase Coche
my_car = Car("Toyota", "Corolla", 2020)

# Acceder a los propiedades
print('My car is a', my_car.year, my_car.make, my_car.model, '.')
# Mi coche es un Toyota Corolla de 2020.

# Modificando propiedades
my_car.year = 2021
print('My car is now a', my_car.year, my_car.make, my_car.model, '.')
# Mi coche ahora es una Toyota Corolla de 2021.

# Nota: Las propiedades de los objetos son similares a las variables, pero estan vinculadas a instancias especificas de objetos.
# Propiedades pueden ser accedidas y modificadas directamente, proporcionando flexibilidad en como objetos almacenan y administran datos.
