import sqlite3

conn= sqlite3.connect("bd_clase9.sqlite3")
cursor= conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Estudiantes(Nombre, Curso)")

def menu ():
    print( """seleccione la opcion:              
[1] crear estudiante
[2] listar estudiantes
[3] actualizar estudiantes      
[4] borrar estudiante
[5] salir
""")
    opc= int (input("Ingrese a opcion:"))
    
    if opc== 1:
        nombre= input("ingrese el nomnre del estudiante:")
        edad= input ("ingrese la edad del studiante:")
        cedula= input("ingrese la cedula del estudiante")
        cursor.execute("INSERT INTO Estudiantes VALUES (?,?)",(nombre, curso))


