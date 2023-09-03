
### Classes ###

# Definición de una clase vacía
class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía

print(MyEmptyPerson)
print(MyEmptyPerson())

# Definición de una clase con constructor, funciones y propiedades públicas
class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública

    def walk(self):
        print(f"{self.full_name} está caminando")

# Creación de instancias de la clase
my_person = Person("Brais", "Moure")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()

# Modificación de una propiedad pública
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)
