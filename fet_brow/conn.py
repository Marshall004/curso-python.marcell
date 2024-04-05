import sqlite3
conn=sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor=conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS listatareas (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE varchar(30), DESCRIPCION varchar(100))")

def crear_tarea(NOMBRE: str,):
    cursor.execute("INSERT INTO listatareas VALUES (1, Marcell, no)")
    conn.commit()

def editar_tarea():
    cursor.execute("UPDATE listatareas SET ID='?' WHERE NOMBRE ='?'")
    
def borrartarea():
    cursor.execute("DELETE FROM listatareas WHERE ID='?'")

def mostrartarea():
    ress=cursor.execute("SELECT FROM * FROM listatareas")
    data=ress.fetchall()
    

