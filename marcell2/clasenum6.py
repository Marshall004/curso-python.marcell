#promedio de lista de numero

def promedio_lista ():
    listanumeros = []
    cantidadnum =int(input("cuantos numeros?:")) 
    for i in range (cantidadnum):
        numero =int (input())
        listanumeros.append (numero)
    suma=0
    for i in listanumeros:
        suma += i
    promedio = suma/cantidadnum
    return promedio
resultado = promedio_lista()
print (resultado)
