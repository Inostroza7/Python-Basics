
### Tuples ###

# Definición de tuplas
my_tuple = (35, 1.77, "John", "Doe")

# Acceso a elementos
print(my_tuple[0])  # Primer elemento
print(my_tuple[-1]) # Último elemento

# Longitud de una tupla
print(len(my_tuple))

# Concatenación de tuplas
other_tuple = (60, 30)
concatenated_tuple = my_tuple + other_tuple
print(concatenated_tuple)

# Subtuplas (slicing)
subtuple = concatenated_tuple[2:4]
print(subtuple)

# Conversión de tupla a lista y viceversa
my_tuple_as_list = list(my_tuple)
my_tuple_as_list[2] = "Jane"
my_tuple = tuple(my_tuple_as_list)
print(my_tuple)
