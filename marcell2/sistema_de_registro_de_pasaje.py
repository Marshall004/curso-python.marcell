pasajeros ={}
def menu ():
    global pasajeros
    opc=int (input( """sistema de registro de pasaje
[1] registrar pasaje
[2] listar pasajeros
[3] borrar data          
[4] salir
"""))
    
    
    if opc ==1:
        nombre= input("ingrese su nombre: ")
        cedula= input("ingrese su cedula:" )
        asiento= input("ingrese su asiento:")
        pasajeros[asiento]= [nombre, cedula]
    
    elif opc ==2:
        for llave,valor in pasajeros.items():
            print("el asiento:",llave, "le corresponde al pasajero:", valor[0] )

    elif opc ==3:
        pasajeros={}

    elif  opc ==4:
        quit()

    menu()
menu()
