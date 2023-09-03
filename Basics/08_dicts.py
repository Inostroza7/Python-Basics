
### Dictionaries ###

# Definición de diccionarios
my_dict = {
    "Name": "John",
    "Age": 35,
    "Languages": ["Python", "Java", "C++"]
}

# Acceso a elementos
print(my_dict["Name"])  # Acceso por clave
print(my_dict.get("Age")) # Acceso usando get

# Inserción de elementos
my_dict["Address"] = "123 Main Street"
print(my_dict)

# Actualización de elementos
my_dict["Name"] = "Jane"
print(my_dict)

# Eliminación de elementos
del my_dict["Address"]
print(my_dict)

# Longitud de un diccionario
print(len(my_dict))

# Obtener claves, valores y elementos
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# Creación de diccionario con claves predeterminadas
keys = ["Name", "Age", "Address"]
default_dict = dict.fromkeys(keys, "Unknown")
print(default_dict)
