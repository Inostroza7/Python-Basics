
### Loops ###

# While loop
my_condition = 0

while my_condition < 5:
    print(my_condition)
    my_condition += 1

print("Fin del bucle while")

# For loop with a list
my_list = [35, 24, 62, 52, 30]

for element in my_list:
    print(element)

print("Fin del bucle for con lista")

# For loop with a tuple
my_tuple = (35, 1.77, "John", "Doe")

for element in my_tuple:
    print(element)

print("Fin del bucle for con tupla")

# For loop with a set
my_set = {"Apple", "Banana", "Cherry"}

for element in my_set:
    print(element)

print("Fin del bucle for con conjunto")

# For loop with a dictionary
my_dict = {"Name": "John", "Age": 35, "Language": "Python"}

for key, value in my_dict.items():
    print(key, value)

print("Fin del bucle for con diccionario")
