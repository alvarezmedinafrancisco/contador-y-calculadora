import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Propinas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campo para ingresar el monto de la cuenta
    txt_monto = ft.TextField(
        label="Monto de la cuenta",
        value="700",
        text_align=ft.TextAlign.RIGHT,
        width=200
    )

    # Texto que muestra el porcentaje seleccionado
    txt_porcentaje = ft.Text("Propina: 5%")

    # Texto que muestra el resultado
    txt_resultado = ft.Text("Propina: $35\nTotal a pagar: $735")

    # Función que calcula la propina
    def calcular_propina(e):
        try:
            monto = float(txt_monto.value)
            porcentaje = slider.value

            propina = monto * (porcentaje / 100)
            total = monto + propina

            txt_porcentaje.value = f"Propina: {int(porcentaje)}%"
            txt_resultado.value = f"Propina: ${propina:.2f}\nTotal a pagar: ${total:.2f}"

            page.update()

        except:
            txt_resultado.value = "Ingresa un número válido"
            page.update()

    # Slider para elegir porcentaje
    slider = ft.Slider(
        min=0,
        max=30,
        divisions=30,
        value=5,
        label="{value}%",
        on_change=calcular_propina
    )

    page.add(
        ft.Column(
            [
                txt_monto,
                slider,
                txt_porcentaje,
                txt_resultado
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.run(main)