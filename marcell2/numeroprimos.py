def es_primo():
    numero =int (input())
    for i in range (2,numero):
        if numero % i == 0 :
            print ("no es primo")
            return "no es primo"
    print ("es primo")

es_primo()