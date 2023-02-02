nombres = ['Ana', 'hugo', 'Valeria']
edades = [65, 29 , 42]
cuidades = ['lima', 'Madrid', 'mexico']
combinados =list(zip (nombres,edades, cuidades))

for nombre, edades,cuidades in combinados:
    print(f"{nombres} tiene {edades} años y vive en {cuidades}")