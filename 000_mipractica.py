# Reto 01 FizzBuzz #


for f in range(1, 101):
    if f % 3 == 0 and f % 5 == 0:
        print("fizzbuzz")
    elif f % 3 == 0:
        print("fizz") 
    elif f % 5 == 0:
        print("buzz")
    else:
        print(f)

#