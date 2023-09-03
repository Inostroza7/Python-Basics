
### Functions ###

# Definición de una función simple
def my_function():
    print("Esto es una función")

my_function()

# Función con parámetros de entrada
def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)

# Función con parámetros de entrada y retorno
def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada por clave
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Brais")

# Función con parámetros de entrada por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")

# Función con parámetros de entrada arbitrarios
def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")
