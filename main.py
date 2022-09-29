#Ejercicio 1
num1 = input("Escribe un numero: ")
print(type(num1))

num2 = int(input("Escribe un numero entero: "))
print(type(num2))

num3 = float(input("Escribe un numero racional: "))
print(type(num3))

#Ejercicio 2
numero1 = int(input("Dime un numero entero: "))
print(str(numero1).zfill(4+len(str(numero1))))
numero2 = float(input("Dime un numero racional: "))
print(str(numero1).zfill(4+len(str(numero1)))) + print("{:.03f}".format(numero2))

#Ejercicio 3 
altura = float(input("Dime tu estatura en metros: "))
peso = float(input("Dime tu peso en kilos: "))
print("Mides {0} metros y pesas {1} Kg".format(altura, peso))
print("Mides {0:<5} metros y pesas {1:>5}Kg".format(altura, peso))

#Hola
