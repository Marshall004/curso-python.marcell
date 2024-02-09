def factorial (num):
    producto=1
    for numero in range (1,num+1):
        producto *= numero

    print ("el factorial de", num, "es:", producto)

factorial(5)