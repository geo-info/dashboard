import flet as ft

def create_header():
    return ft.Container(
        content=ft.Text("To-Do App", size=24, color=ft.colors.WHITE),
        width = None,
        height=60,
        padding=10,
        bgcolor=ft.colors.BLUE,
        alignment=ft.alignment.center,
        expand=False
    )