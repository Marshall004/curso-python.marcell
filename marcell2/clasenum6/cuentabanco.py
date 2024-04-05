cuentas=[]

class CuentaBancaria():
    def __init__ (self, titular, saldo, nroCuenta):
        self.titular = titular
        self.saldo = saldo
        self.nroCuenta = nroCuenta
    def consultarSaldo(self):
        print("su saldo es ", self.saldo)
    def retirar (self,cantidad):
        if cantidad<=self.saldo:
            self.saldo-=cantidad
            print("retirado",cantidad)
            self.consultarSaldo()
        else:
            print("su saldo es insuficiente")
    def depositar (self, cantidad):
        self.saldo += cantidad
        self.consultarSaldo()

    def transferir (self, cantidad, receptor):
        if cantidad<= self.saldo:
            self.saldo-=cantidad
            receptor.saldo += cantidad
            print("Transferido", cantidad)
            self.consultarSaldo()
            receptor.consultarSaldo()
        else:
            
            print("saldo insuficiente")

def registrar_cuenta(nombre, cedula):
    cuenta= CuentaBancaria(nombre,0,len(cuentas)-1)
    cuentas.append(cuenta)
    print("su numero de cuenta es:",len(cuentas)-1)


def menu_principal():
    print ("""
1. pregistrar nueva cuenta
2. iniciar sesion 
3. salir""")
    opc=int(input("ingrese la opcion:"))

    if opc ==1:
        nombre= input ("ingresar su nombre:")
        cedula= input ("ingresar cedula:")
        registrar_cuenta(nombre, cedula)

    elif opc ==2:
        nroCuenta = int (input("ingrese su numero de cuenta:"))
        if nroCuenta>len(cuentas)-1:
            print("el numero de cuenta no existe")
        else:
            print("ingreso exitoso")

            menu_usuario(nroCuenta)

    elif opc==3:
        exit()
    menu_principal()

def menu_usuario(nroCuenta):
    cuenta=cuentas[nroCuenta]
    print ("bienvenido", cuenta.titular)
    print ("""
    1.depositar
    2.transferir
    3.consultar
    4.regresar
    """)
    opc= int ( input ("ingresar opcion:"))
    if opc==1:
        cantidad= int (input("ingrese la cantidad que desea depositar:"))
        cuenta.depositar(cantidad)
        print("deposito exitoso")
    elif opc ==2:
        nro_cuenta_transferir=int (input)
        cuenta_tranferir=cuentas[nro_cuenta_transferir]
        cuenta.transferir(cuenta_tranferir)
    menu_usuario(nroCuenta)
menu_principal()