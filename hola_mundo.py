# 1. TAREA: imprime "Hola, mundo"
print("Hola, mundo")

# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Noelle"
print("Hola,", name)  # con una coma
print("Hola " + name)  # con un +

# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print("Hola,", name, "!")  # con una coma
# la versión de este ejercicio con el error estará al final de este archivo

# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer {} y {}".format(fave_food1, fave_food2))  # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}")  # con una cadena f

#OTRAS INSTRUCCIONES: 
#5
my_name = "Karli"
print("¡Hola, ", my_name , "!")

#6
my_name = "Karli"
print("¡Hola, " + my_name + "!")

#7
my_num = 16
print("¡Hola, ", my_num , "!")

#8
my_num = 16
print("¡Hola, " + str(my_num) + "!") #BONUS NINJA

#9
comida_uno = "sushi"
comida_dos = "ceviche"
print("Amo comer {} y {}".format(comida_uno, comida_dos))


#10
comida_uno = "sushi"
comida_dos = "ceviche"
print(f"Amo comer {comida_uno} y {comida_dos}")


#BONUS NINJA FINAL
my_dog = "cachorro pony"
age_dog = 5
print("A mi perrita le digo %s aunque ya no es cachorro, porque tiene %d años de edad" % (my_dog, age_dog))


# 3.b imprimir error
name = 42
print("Hola " + name + "!") # con un +, error, porque no se puede concatenar directamente porque name no es una cadena

