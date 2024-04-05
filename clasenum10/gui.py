
import conn 
import flet as ft

def main (page:ft.page):
    def agregartarea(e):
        nombre= camponombre.value
        descripcion= campodescripcion.value
        conn.crear_tarea(nombre,descripcion)
    camponombre=ft.TextField(label="nombre tarea")
    campodescripcion=ft.TextField(label= "descripcion tarea")
    botonagregar=ft.ElevatedButton("Agregar", on_click= agregartarea )
    page.add(camponombre,campodescripcion,botonagregar)
    def mostrar():
        tareas= conn.mostrartarea()
        for tarea in tareas:
            page.add(ft.Text(tarea[1]+'-'+tarea[2]))
    mostrar()

                              
ft.app(target=main, view=ft.AppView.WEB_BROWSER)