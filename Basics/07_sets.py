
### Sets ###

# Definición de sets
my_set = {"Apple", "Banana", "Cherry"}

# Inserción de elementos
my_set.add("Orange")
print(my_set)

# Eliminación de elementos
my_set.remove("Banana")
print(my_set)

# Búsqueda de elementos
print("Apple" in my_set)
print("Banana" in my_set)

# Longitud de un set
print(len(my_set))

# Unión de sets
other_set = {"Python", "Java", "C++"}
union_set = my_set.union(other_set)
print(union_set)

# Diferencia entre sets
difference_set = union_set.difference(my_set)
print(difference_set)

# Transformación de set a lista
my_list_from_set = list(my_set)
print(my_list_from_set)
