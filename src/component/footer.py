import flet as ft

def create_footer():
    return ft.Container(
        content = ft.Text("© 2024 To-Do App", size = 14, color = ft.colors.WHITE),
        width = None,
        height = 60,
        padding = 10,
        bgcolor = ft.colors.BLUE,
        alignment = ft.alignment.center,
        expand = False
    )