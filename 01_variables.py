# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacíon de variables en un print
print(my_bool_variable, my_int_to_str_variable, my_string_variable)
print("este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea !cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Lucas", "Jara", "Lukensen", 36
print("Me llamo:", name, surname, ". Mi edad es:", age,  "Y mi alias es:", alias)




# Inputs
"""
name = input("Cual es tu nombre?")
age = input("Cuanto años tenes?")
print(name)
print(age)
"""

# Cambiamos su tipo
name = 35
age = "Lucas"
print(name)
print(age)

# Forzamos el tipo?
address: str = "Mi dirección"
address = 32
address = 1.5
address = True
print(type(address))