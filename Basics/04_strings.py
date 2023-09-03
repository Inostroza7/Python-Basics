
### Strings ###

# Definición de cadenas de texto
my_string = "Hola Python"
print(my_string)

# Concatenación de cadenas
greeting = "Hola"
name = "Python"
print(greeting + " " + name)

# Longitud de una cadena
print(len(my_string))

# Acceso a un carácter específico
print(my_string[0])  # Primera letra
print(my_string[-1]) # Última letra

# División (slicing) de cadenas
language_slice = my_string[5:11]
print(language_slice)

# Reversión de una cadena
reversed_language = my_string[::-1]
print(reversed_language)

# Formateo de cadenas
age = 30
print(f"Mi lenguaje favorito es {name} y tengo {age} años.")

# Funciones comunes de cadenas
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("Hola"))
