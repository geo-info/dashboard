import flet as ft
from page.home_page import home_page
from component.sidebar import create_sidebar
from component.header import create_header
from component.footer import create_footer


def main(page: ft.Page):
    page.title = "To-Do App с Sidebar, Header и Footer"
    # page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.scroll = "auto"
    page.update()

    # Создаем header, sidebar, footer
    header = create_header()
    footer = create_footer()
    sidebar = create_sidebar(page)

    # Создаем основную область контента
    content = ft.Column(expand=True)

    # Подключаем главную страницу с задачами
    home_page(content)

    # Основная структура приложения: sidebar, header, content и footer
    page.add(
        header,  # Закрепленный в верхней части header
        ft.Row([
            sidebar,  # Боковое меню
            content,  # Основной контент
        ], expand=True),
        footer  # Закрепленный в нижней части footer
    )


# Запуск приложения
ft.app(target = main)