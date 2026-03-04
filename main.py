import flet as ft

def main(page: ft.Page):
    page.title = "contador con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # control que muestra el numero
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def restar(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def sumar(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.Icons.REMOVE, on_click=restar),
                txt_number,
                ft.IconButton(ft.icons.Icons.ADD, on_click=sumar),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


# punto de entrada de la aplicación
ft.run(main)