lista = ['a', 'b', 'c']


for indice,item in enumerate(lista):
    print(indice,item)
    
lista2 = ['a', 'c', 'd']
mis_tuples = list(enumerate(lista2))
print(mis_tuples[1][0])

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)