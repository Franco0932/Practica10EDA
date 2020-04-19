def cuenta(limite):
    i = limite
    while True:
        print(i)
        i = i -1
        if i == 0:
            break
cuenta(10)

print("********************************************************************************")

def factorial (n):
    i = 2
    tmp = 1
    while i < n+1:
        tmp = tmp * i
        i = i + 1
        return tmp
    
print (factorial(4))
print (factorial(6))

