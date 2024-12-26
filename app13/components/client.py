import reflex as rx


def render_search_client() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.text("Cliente:"),
                rx.input(
                    placeholder="Seleccionar Cliente",
                ),
                rx.text("Precio:"),
                rx.input(
                    placeholder="Tipo de Precio",
                ),
                padding="1em 0em 0em 2em",
            ),
            rx.hstack(
                rx.text("Nombre"),
                rx.text("Juan Crisostomo Falcon"),
                padding="0.3em 0em 0em 2em",

            ),
            rx.hstack(
                rx.text("Direccion"),
                rx.text("Calle 25, Brisas del Lago, Maracay"),
                padding="0.3em 0em 0em 2em",

            ),
            spacing="0"
        ),

    )
