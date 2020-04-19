#Iteración en diccionarios
elementos = { 'hidrogeno': 1, 'helio':2, 'carbon':6}

for llave, valor in elementos.items():
    print(llave, "=", valor)

print("*****************************************************************************")

for llave in elementos.keys():
    print(llave)
    
print("*****************************************************************************")
for valor in elementos.values():
    print (valor)
    
print("*****************************************************************************")
for idx, x in enumerate(elementos):
    print("El indice es: {} y el elemento: {}".format(idx, x))

print("*****************************************************************************")

def cuenta_idiom(limite):
    for i in range(limite, 0, -1):
        print (i)
    else:
        print("Cuenta finalizada")
cuenta_idiom(5)        
        
print("*****************************************************************************")
def cuenta_idiomv2(limite):
    for i in range(limite, 0, -1):
        print (i)
        if i == 3:
            break
    else:
        print("Cuenta finalizada")
cuenta_idiomv2(5)        
