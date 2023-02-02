lista = [ 'a', 'b', 'c', 'd']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"letra {numero_letra}: {letra}")
    
    
    listados = ['pablo', 'laura','fede', 'luis', 'ana']
    
    
    for nombre in listados :
        if nombre.startswith ('l'):
            print(nombre)
            
        else :
            print ("Nombre que no comienza con l")