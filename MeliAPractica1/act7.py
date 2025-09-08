#7. Escribe un programa que tome una lista de números enteros como entrada del usuario. Luego,
#convierte cada número en la lista a string y únelos en una sola cadena, separados por guiones
#(‘-’). Sin embargo, excluye cualquier número que sea múltiplo de 3 de la cadena final.

# Pedimos al usuario que ingrese números separados por espacios
entrada = input("Ingrese números enteros separados por espacios: ")

# Convertimos la entrada en una lista de enteros
l_numeros = [int(x) for x in entrada.split()] #l método split, retorna una lista con los elementos de la cadena de caracteres.

# Inicializamos la lista donde guardaremos los números que no sean múltiplos de 3
numeros_filtrados = []

# Recorremos cada número y lo agregamos si no es múltiplo de 3
for i in l_numeros:
    if i % 3 != 0:
        numeros_filtrados.append(str(i))  # Convertimos a string al agregarlo

# Unimos los números con guiones
resultado = '-'.join(numeros_filtrados) #resultado es la cadena/texto final

# Mostramos el resultado
print("Cadena resultante:", resultado)