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

def añadir_tamaño(mi_lista):
    longitud = len(mi_lista)
    mi_lista.append(longitud)
    return mi_lista

print(añadir_tamaño([23, 42, 197]))

"""
Se define una función llamada "añadir_tamaño" que toma una lista "mi_lista" como argumento. La función calcula la longitud de la lista proporcionada usando "len(mi_lista)", luego agrega esa longitud al final de la lista utilizando "mi_lista.append(longitud)", y finalmente devuelve la lista modificada.

Si ejecutas "añadir_tamaño([23, 42, 197])", la función agrega la longitud de la lista original [23, 42, 197] al final de esta lista. Dado que la longitud de [23, 42, 197] es 3, el resultado impreso será [23, 42, 197, 3], ya que se ha agregado el número 3 al final de la lista original.

"""

