from pickle import FALSE


texto = input("Escriba su frase favorita:")
letra = [] 


texto = texto.lower()

letra.append(input("ingresa la primera letra").lower())
letra.append(input("ingresa la segunda letra").lower())
letra.append(input("ingresa la tercera letra").lower())


print("\n")
print("cantidad de letras")
cantidad_letras1 = texto.count(letra[0])
cantidad_letras2 = texto.count(letra[1])
cantidad_letras3 = texto.count(letra[2])
  
print (f"Hemos encontrado la letra '{letra[0]}' repetida {cantidad_letras1} veces")
print (f"Hemos encontrado la letra '{letra[1]}' repetida {cantidad_letras2} veces")
print (f"Hemos encontrado la letra '{letra[2]}' repetida {cantidad_letras3} veces")




print("\n")
print("cantidad de palabras")
palabras = texto.split()

print(f"Hemos encontrado {len(palabras)} en tu texto")


print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}' ")




print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()

texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reves va a decir:'{texto_invertido}")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'Python'{dic[buscar_python]} se encuentra en el texto")