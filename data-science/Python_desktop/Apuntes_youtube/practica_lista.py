lista1=["maria", "luis", "natalia", "juan", "marcos", "pepe"]#el indice empieza contar desde el cero, ej "luis" seria posicion 2 indice 1

print([lista1])

print(lista1[2])#indico que solo quiero que aparezca el indice 2

print(lista1[-1])#el menos hace que el indice se cuente de derecha a izquierda, en este caso solo aparece el ultimo

print(lista1[:3])#indico que solo se muestren los tres primeros indices, no hace falta por el "cero"

print(lista1[2:])#empiezo desde el indice 2 en adelante hasta el final

lista1.append("carlos")#agregar elemento a la lista, pero lo agrega al final de esta

print([lista1])

lista1.insert(4,"pedro")#inserto el elemento en el indice que indico

print(lista1[:])

lista1.extend(["fabio","lucas","leandro"])#permite agrerar varios elementos a la vez

print(lista1[:])

print(lista1.index("lucas"))#indica en que indice se encuentra el elemento

print("pepe" in lista1)#true o false, indice si el elemento esta o no dentro de la lista
print("peponi" in lista1)

lista2=["vaso", 456, 3.34, True, False, "camila"]#puedo enlistar distintos tipos de variable

lista2.remove(True)#elimino un elemento de la lista indicando el nombre correspondiente

print(lista2[:])

lista2.pop()#elimina el ultimo elemento de la lista

print(lista2[:])

lista3=["cocina", "pokemon"]

lista4=lista1+lista2+lista3#suma las listas, un concatenador es, pero crea una lista mayor por eso se usa otra variable

print(lista4[:])

print(lista1[:]*2) #el multiplicador sirve de repetidor, repite la lista la veces que se indique