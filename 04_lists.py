### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 56, 30, 30, 15]

print(my_list)
print(len(my_list))  

my_other_list = [35, 1.77, "Lucas", "Jara"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)
#print(my_list - my_other_list)



my_list = "Hola Python"
print(my_list)
print(type(my_list))