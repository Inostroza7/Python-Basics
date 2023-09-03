
### Lists ###

# Definición de listas
my_list = [35, 24, 62, 52, 30]
print(my_list)

# Acceso a elementos
print(my_list[0])  # Primer elemento
print(my_list[-1]) # Último elemento

# Longitud de una lista
print(len(my_list))

# Concatenación de listas
other_list = [1, 2, 3]
print(my_list + other_list)

# Agregar elementos
my_list.append(40)
print(my_list)

# Insertar elementos en una posición específica
my_list.insert(1, 100)
print(my_list)

# Eliminación de elementos
my_list.remove(100)
print(my_list)

# Uso de pop para eliminar y retornar un elemento
popped_element = my_list.pop(2)
print(popped_element)
print(my_list)

# Reversión de una lista
my_list.reverse()
print(my_list)

# Ordenar una lista
my_list.sort()
print(my_list)

# Sublistas (slicing)
sublist = my_list[1:3]
print(sublist)
