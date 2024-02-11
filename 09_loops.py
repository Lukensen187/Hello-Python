### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual a 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiende la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 56, 30, 30, 15]  # Guardan elementos de forma ordenada en 1 en 1

for element in my_list:
    print(element)

my_tuple = (35, 1.86, "Lucas", "Jara", "Lucas") # Guardan elementos pero no se puede retocar

for element in my_tuple:
    print(element)

my_set = {"Lucas", "Jara", 35} # Guardan elementos que no estan repetidos

for element in my_set:
    print(element)

my_dict = {"Nombre":"Lucas", "Apellido":"Jara", "Edad":35, 1:"Python"} # Guardan elementos forma clave y valor

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta") 
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continúa")   