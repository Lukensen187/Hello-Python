### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.86, "Lucas", "Jara", "Lucas")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuples[4]) IndexError
#print(my_tuples[-6]) IndexError

print(my_tuple.count("Lucas"))
print(my_tuple.index("Jara"))
print(my_tuple.index("Lucas"))

#my_tuple[1] = 1.90 Error

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "LucasDev"
my_tuple.insert(1, "Azul")
print(tuple(my_tuple))
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] TypeError 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined