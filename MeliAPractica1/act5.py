#5.CHAT GPT Implementa un programa que solicite al usuario que ingrese una lista de números. Luego,
#imprime la lista pero detén la impresión si encuentras un número negativo. Nota: utilice la
#sentencia break cuando haga falta.

entrada = input("Ingresa una lista de números separados por espacio: ")


lista_numeros = list(map(int, entrada.split())) # Convertimos la entrada en una lista de enteros
print("Imprimiendo la lista hasta encontrar un número negativo:")
for elem in lista_numeros:
    if elem < 0:
        print("Se encontró un número negativo:", elem, "→ Se detiene la impresión.")
        break
    print(elem)


