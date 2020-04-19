def numeros(num):
    if num==1:
        print("Tu numero es 1")
    elif num==2:
        print("Tu numero es 2")
    elif num==3:
        print("Tu numero es 3")
    elif num==4:
        print("Tu numero es 4")
    else:
        print ("No hay opción")

numeros (2)
numeros (5)

print("********************************************************************************")

def numeros_idiom(num2):
    if num2 in (1,2,3,4):
        print("Tu numero es {}".format(num2))
    else:
         print("{} No es una opcion".format(num2))

numeros_idiom(2)
numeros_idiom(5)

print("********************************************************************************")
def obtenerMasGrande(a,b,c):
     if a > b:
         if a > c:
             return a
         else:
             return c
     else:
          if b > c:
              return b
          else:
               return c
print("El mas grande es {}".format(obtenerMasGrande(7,13,1) ))            
           
