nombre_de_lista = input ("ingrese el nombre de la lista: ")
mi_lista = {}
mi_lista[nombre_de_lista] = []

print ("lista creada con exito")
contenido = input ("ingrese el contenido de la lista:")
mi_lista[nombre_de_lista].append(contenido)
print ("contenido agregado con exito")
print ("\n lista actualizada:")
for item in mi_lista[nombre_de_lista]:
    print (item)
print ("el nombre de la lista es: " + nombre_de_lista)