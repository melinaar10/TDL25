#1-Desarrolla un programa que solicite al usuario que ingrese su edad y luego calcule y muestre cuántos años le faltan para alcanzar los 100 años.
#edad =int(input("Ingresa tu edad: "))
#print(type(edad))
#print ("Le faltan",100-edad,"años para llegar a los 100")

#2- REVISAR!! Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.
temperaturaC =int(input("Ingresa una temperatura en grados celcius: "))
print(type(temperaturaC))
print ("En grados celcius ingresaste la temperatura de:", temperaturaC)
temperaturaF = (temperaturaC * 1,8) + 32
print ("En grados farenheit:", temperaturaF)


#3-Crea un programa que calcule la suma de los primeros 100 números naturales utilizando un bucle for.
acum= 0
for i range (100)
    acum= acum + i
