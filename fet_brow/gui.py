import conn 
import flet as ft
def main (page:ft.page):
    tareas=conn.mostrarTareas()