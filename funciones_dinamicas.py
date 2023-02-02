def chequear_3_cifras(lista):
 
   for n in lista:
    if n in range(100,1000):
        return True
    else:
        pass
    return False
resultado = chequear_3_cifras([599, 99,6000])
print(resultado)


lista_numeros = [1,-50,502,-5000,755,600,33,61]
 
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True

lista_numeros = [1,50,500,5000,750,600]
 
def suma_menores(lista_numeros):
    suma=0
    for numero in lista_numeros:
        if numero in range(1,1000):
            suma += numero
        else:
            pass
    return suma

lista_numeros = [1,50,502,5000,755,600,33,61]
 
def cantidad_pares(lista_numeros):
    cantidad=0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad  