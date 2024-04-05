import sqlite3

conn=sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor=conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS listatareas (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE, DESCRIPCION)")

def crear_tarea(nombre:str, descripcion: str):
    cursor.execute("INSERT INTO listatareas ( NOMBRE, DESCRIPCION) VALUES (?,?)",(nombre, descripcion))
    conn.commit()

def editar_tarea():
    cursor.execute("UPDATE listatareas SET ID='?' WHERE NOMBRE ='?'")
    conn.commit
    
def borrartarea(ID):
    cursor.execute("DELETE FROM listatareas WHERE ID=?",(ID))
    conn.commit

def mostrartarea():
    ress=cursor.execute("SELECT * FROM listatareas")
    data=ress.fetchall()
    return data