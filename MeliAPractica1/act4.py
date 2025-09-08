#4. Cree un programa que dada una lista de números imprima sólo los que son pares. 
# Nota: utilice la sentencia continue donde haga falta.
lista_numeros= [108, 105, 112, 115, 123, 129, 122, 140]
print ("mi lista tiene",len (lista_numeros),"elementos")#Return the number of items in a container.

print ("A continuacion se muestran los numeros pares:")
for elem in lista_numeros:
    if elem % 2 == 0:
        print (elem)
    else: 
        continue
