#6. Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una con los
#número pares y otras con los que son impares. Imprima las listas al terminar de procesarlas.
lista_numeros= [108, 105, 112, 115, 123, 129, 122, 140]
print ("mi lista tiene",len (lista_numeros),"elementos")#Return the number of items in a container.

lista_pares = []
lista_impares = []

for elem in lista_numeros:
    if elem % 2 == 0:
        lista_pares.append(elem)
    else: 
        lista_impares.append(elem)

print("Lista original:", lista_numeros)
print("Números pares:", lista_pares)
print("Números impares:", lista_impares)