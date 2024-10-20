import flet as ft

def task_list(page, tasks):
    task_input = ft.TextField(hint_text="Введите новую задачу", width=300)

    def add_task(e):
        task_text = task_input.value
        if task_text:
            task = ft.Row(
                controls=[
                    ft.Checkbox(label=task_text, on_change = task_status_changed),
                    ft.IconButton(icon=ft.icons.DELETE, on_click = lambda e: delete_task(task))
                ]
            )
            tasks.controls.append(task)
            task_input.value = ""
            page.update()

    def task_status_changed(e):
        checkbox = e.control
        if checkbox.value:
            checkbox.label = f"✅ {checkbox.label}"
        else:
            checkbox.label = checkbox.label.replace("✅ ", "")
        page.update()

    def delete_task(task):
        tasks.controls.remove(task)
        page.update()

    return ft.Column(controls=[
        ft.Row([task_input, ft.ElevatedButton("Добавить", on_click=add_task)]),
        tasks
    ])