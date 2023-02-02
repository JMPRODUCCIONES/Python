nombre = input("Nombre completo:")
ventas = input("¿Cuantas ventas has realizado este mes?")


ventas= int(ventas)

comision = ventas * 13 / 100

comision = round(comision) 

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
