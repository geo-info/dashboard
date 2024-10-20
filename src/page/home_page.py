import flet as ft
from component.task_list import task_list

def home_page(content):
    # Список задач
    tasks = ft.Column()
    # Добавляем To-Do список на основную страницу
    content.controls.append(task_list(content, tasks))