import os

print("Hello world from ...")
os.system("python --version")

# Desafíos de código Python con Listas

# A Añadir Tamaño: 
"""
Vamos a calcular la longitud de una lista y luego añadir el valor al final de la lista.

1 - Definir la función para aceptar un parámetro para nuestra lista.

2 - Obtener la longitud de la lista.

3 - Añadir la longitud de la lista al final de la lista.

4 - Devuelve la lista modificada.

"""
# A
def añadir_tamaño(mi_lista):
    longitud = len(mi_lista)
    mi_lista.append(longitud)
    return mi_lista

print(añadir_tamaño([23, 42, 197]))

"""
Se define una función llamada "añadir_tamaño" que toma una lista "mi_lista" como argumento. La función calcula la longitud de la lista proporcionada usando "len(mi_lista)", luego agrega esa longitud al final de la lista utilizando "mi_lista.append(longitud)", y finalmente devuelve la lista modificada.

Si ejecutas "añadir_tamaño([23, 42, 197])", la función agrega la longitud de la lista original [23, 42, 197] al final de esta lista. Dado que la longitud de [23, 42, 197] es 3, el resultado impreso será [23, 42, 197, 3], ya que se ha agregado el número 3 al final de la lista original.

"""

# B - Añadir Suma: 

"""
Vamos a crear una función que calcule la suma de los dos últimos elementos de una lista y la añada al final. Después de hacerlo, repetirá este proceso dos veces más y devolverá la lista resultante. 


1 - Define la función para que acepte un parámetro para nuestra lista de números.

2 - Suma el último y el penúltimo elemento de la lista.

3 - Añade el valor calculado al final de la lista.

4 - Repite los pasos 2 y 3 veces más.

5 - Devuelve la lista modificada.

"""
# B
def añadir_suma(mi_lista):
    mi_lista = [1, 1, 2] # Creo una Lista
    suma = mi_lista[-1] + mi_lista[-2] # Sumo el último y el penúltimo elemento de la lista
    mi_lista.append(suma) # Añado el valor calculado al final de la lista
    suma = mi_lista[-1] + mi_lista[-2]
    mi_lista.append(suma)
    suma = mi_lista[-1] + mi_lista[-2]
    mi_lista.append(suma)
    return mi_lista # Devuelvo la lista modificada
print(añadir_suma([1, 1, 2]))

"""
En resumen, la función añadir_suma crea una lista [1, 1, 2], luego calcula la suma de los dos últimos elementos de la lista, la agrega al final de la lista y repite este proceso tres veces más (en total, agrega tres sumas adicionales a la lista).
Finalmente, la función devuelve la lista modificada. 
"""

# C Lista Ampliada

"""
1 - Defina la función para que acepte dos parámetros para nuestras dos listas de números.

2 - Comprobar si la longitud de la primera lista es mayor o igual que la longitud de la segunda lista.

3 - Si es cierto, devuelve el último elemento de la primera lista. En caso contrario, devuelve el último elemento de la segunda lista.

# print(lista_ampliada([4, 10, 2, 5], [-10, 2, 5, 10]))

"""
# C
def lista_ampliada(mi_lista_1, mi_lista_2):
    if len(mi_lista_1) >= len(mi_lista_2):
        return mi_lista_1[-1]
    else:
        return mi_lista_2[-1]

print(lista_ampliada([4, 10, 22, 5], [-10, 2, 5, 10]))

"""
Este código define una función llamada lista_ampliada que toma dos listas como argumentos: mi_lista_1 y mi_lista_2.

La función verifica la longitud de ambas listas con len(mi_lista_1) y len(mi_lista_2). Si la longitud de mi_lista_1 es mayor o igual que la longitud de mi_lista_2, la función devuelve el último elemento de mi_lista_1 utilizando mi_lista_1[-1]. De lo contrario, si la longitud de mi_lista_2 es mayor que la longitud de mi_lista_1, la función devuelve el último elemento de mi_lista_2 usando mi_lista_2[-1].

Al llamar a la función lista_ampliada con las listas [4, 10, 2, 5] y [-10, 2, 5, 10], la longitud de mi_lista_1 es igual a la longitud de mi_lista_2 (ambas tienen 4 elementos), por lo que la función devuelve el último elemento de mi_lista_1, que es 5. Por lo tanto, el resultado impreso será 5.

"""

# D Más de N:

"""
Nuestra fábrica produce una gran variedad de aperitivos de distintos sabores y queremos comprobar el número de casos de un determinado tipo.

Tenemos una cinta transportadora llena de diferentes tipos de aperitivos representados por diferentes números.

Nuestra función aceptará una lista de números (que representan el tipo de tentempié), un número como segundo parámetro (el tipo de tentempié que buscamos) y otro número como tercer parámetro (el número máximo de ese tipo de tentempié en la cinta transportadora). 

La función devolverá True si el snack que buscamos aparece más veces de las que indicamos como tercer parámetro. 


1 - Define la función para que acepte tres parámetros, una lista de números, un número a buscar y un número para el número de instancias.

2 - Contar el número de apariciones de "item" (el segundo parámetro) en "mi_lista" (el primer parámetro).

3 - Si el número de apariciones es mayor que "n" (tercer parámetro), devuelve True. En caso contrario, devuelve False.

"""
# D
def mas_de_n(mi_lista, item, n):
    if mi_lista.count(item) > n:
        return True
    else:
        return False

print(mas_de_n([2, 4, 6, 2, 3, 2, 1, 2], 2,   3))
                #  mi_lista       #item = 2  #n = 3

"""
La función utiliza el método "count()" de las listas en Python. Verifica si el número de veces que item aparece en "mi_lista" es mayor que "n = 3". Si la cantidad de ocurrencias de item en mi_lista es mayor que n, la función devuelve "True", indicando que hay más de n ocurrencias del item en la lista. De lo contrario, devuelve False.

Al llamar a la función mas_de_n con la lista [2, 4, 6, 2, 3, 2, 1, 2], el item 2 y n = 3, la función cuenta cuántas veces aparece "2" en la lista. En este caso, 2 aparece 4 veces en la lista, por lo que mi_lista.count(item) es igual a 4. Como 4 > 3, la función devuelve True. Por lo tanto, el resultado impreso será True.

"""

# E Combinar Ordenar

"""
1 - Define la función para que acepte dos parámetros, uno para cada lista. 

2 - Combina las dos listas en una sola lista.

3 - Ordena la lista resultante

4 - Devuelve la lista resultante.

Podemos combinar listas utilizando el operador +. Para ordenar una lista podemos utilizar la función sorted().

"""
# E
def combinar_listas(mi_lista, mi_lista_2):
    lista_unica = mi_lista + mi_lista_2
    lista_unica.sort()
    return lista_unica
print(combinar_listas([4, 10, 2, 5], [-10, 2, 5, 10]))

"""
La función combinar_listas combina las dos listas usando el operador +, creando una nueva lista llamada lista_unica que contiene todos los elementos de ambas listas. Luego, utiliza el método sort() para ordenar los elementos de esta lista combinada en orden ascendente.

Al llamar a la función combinar_listas con las listas [4, 10, 2, 5] y [-10, 2, 5, 10], la función combinará estas listas, generando [4, 10, 2, 5, -10, 2, 5, 10], y luego la ordenará en orden ascendente, resultando en [-10, 2, 2, 4, 5, 5, 10, 10].

"""