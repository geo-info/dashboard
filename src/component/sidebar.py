import flet as ft

def create_sidebar(page):
    # Функция для отображения и скрытия sidebar
    def toggle_sidebar(e):
        sidebar.visible = not sidebar.visible
        page.update()

    # Скрываемое боковое меню
    sidebar = ft.Container(
        content = ft.Column([
            ft.TextButton("home", on_click=lambda e: print("home")),
            ft.TextButton("dashboard", on_click=lambda e: print("dashboard")),
            ft.TextButton("login", on_click=lambda e: print("login"))
        ], width=200, expand=True),
        visible = True,
        width = 300,
        bgcolor = ft.colors.BLUE_50,
        padding = 10
    )

    # Кнопка для открытия/закрытия меню
    toggle_button = ft.IconButton(icon=ft.icons.MENU, on_click=toggle_sidebar)

    # Возвращаем кнопку и само меню
    return ft.Container(
        content=ft.Column([
            toggle_button,  # Кнопка в верхней части для открытия/закрытия
            sidebar         # Само меню
        ]),
        width=300,  # Ширина закрытого состояния sidebar
    )