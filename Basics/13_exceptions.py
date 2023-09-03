
### Exception Handling ###

# Excepción base: try except
try:
    print(5 + "1")
except:
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally
try:
    print(5 + 1)
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally:
    print("La ejecución continúa")

# Excepciones por tipo
try:
    print(5 + "1")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción
try:
    print(5 + "1")
except Exception as error:
    print(error)
