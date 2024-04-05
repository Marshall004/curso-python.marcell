import sqlite3

conn= sqlite3.connect("bd_clase9.sqlite3")
cursor= conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Estudiantes (nombre,curso)")
"""cursor.execute("INSERT INTO Estudiantes VALUES('Carlos','6to')") """
conn.commit()
res=cursor.execute("SELECT * FROM Estudiantes")
data=res.fetchall()
for valor in data:
    print(f"nombre={valor[0]},curso:{valor[1]}")
""" cursor.execute ("INSERT INTO Estudiantes VALUES ('Carlos','4to')")
conn.commit() """
cursor.execute ("UPDATE Estudiantes SET curso='7mo' WHERE nombre ='Marcell'")
conn.commit()
cursor.execute ("DELETE FROM Estudiantes WHERE nombre='Carlos'")
conn.commit()
""" cursor.execute("INSERT INTO Estudiantes VALUES ('Carlos','9no')") """
conn.commit()
cursor.execute ("DELETE FROM Estudiantes WHERE nombre='Daniel'")
conn.commit()
