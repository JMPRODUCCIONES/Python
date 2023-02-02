def multiplicar (numero1, numero2):
    total = numero1 * numero2
    return total


resultado = multiplicar(5,10)
print(resultado)


def potencia (numero3, numero4):
    totales = numero3 ** numero4
    return totales

resultado_potencia = potencia(40,2)
print (resultado_potencia)



dolares = 1200
def usd_a_eur(dolares):
    return dolares*0.90


palabra = "Curso de Python"
 
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra