#2-Haz un programa que pida al usuario que ingrese una temperatura en grados 
#Celsius y luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.
temperaturaC =int(input("Ingresa una temperatura en grados celcius: "))
print(type(temperaturaC))
print ("En grados celcius ingresaste la temperatura de:", temperaturaC)
temperaturaF = (temperaturaC * 1.8) + 32
print ("En grados farenheit:", temperaturaF)