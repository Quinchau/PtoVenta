import reflex as rx
from rxconfig import config
from .components.client import render_search_client


class State(rx.State):
    """The app state."""

    ...


@rx.page(route='/', title='Factura')
def index():
    return rx.container(
        rx.flex(
            # Area 1: Header
            rx.box(
                rx.heading(
                    "QuinChau Motos",
                    font_family="Arial",
                    margin_bottom="1em",
                    padding="1em 0em 0em 2em",
                    size=rx.breakpoints(
                        initial="7",  # móvil
                        sm="7",      # tablet
                        lg="20"       # desktop
                    ),
                    color_scheme="indigo",
                    as_="h1",
                    text_decoration="cursive"),
                width="100%",
                height=["15vh", "10vh", "10vh"],
                box_shadow="10px 5px 5px grey",
                margin="0.2em",  # Increased margin
                border_radius="1em",
                # background="white",
            ),

            rx.box(
                rx.flex(
                    rx.box(
                        rx.flex(
                            rx.box(
                                render_search_client(),
                                width="100%",
                                height=["40vh", "75vh", "20vh"],
                                # height="20%",
                                # Increased shadow
                                box_shadow="10px 5px 5px grey",
                                margin="0.2em",  # Increased margin
                                border_radius="1em",
                                background="linear-gradient(45deg,rgb(219, 219, 219),rgb(230, 231, 238))",
                            ),
                            rx.box(
                                "Area 3 - Busqueda Productos",
                                width="100%",
                                height="80%",
                                # Increased shadow
                                box_shadow="10px 5px 5px grey",
                                margin="0.2em",  # Increased margin
                                border_radius="1em",
                                background="linear-gradient(45deg,rgb(219, 219, 219),rgb(230, 231, 238))",
                            ),
                            direction="column",
                            width="100%",
                            height="100%",
                            gap="0.5em",  # Increased gap
                        ),
                        width=rx.breakpoints(
                            initial="100%",
                            sm="100%",
                            lg="50%"
                        ),
                        height="100%",
                        # background="white",
                    ),
                    rx.box(
                        "Area 4 - Productos en el carrito",
                        width=rx.breakpoints(
                            initial="100%",
                            sm="100%",
                            lg="50%"
                        ),
                        height="100%",
                        # Increased shadow
                        box_shadow="10px 5px 5px grey",
                        margin="0.2em",  # Increased margin
                        border_radius="1em",
                        background="linear-gradient(45deg,rgb(219, 219, 219),rgb(230, 231, 238))",
                    ),
                    direction=rx.breakpoints(
                        initial="column",
                        sm="column",
                        lg="row"
                    ),
                    width="100%",
                    height="100%",
                    gap="0.5em",  # Increased gap
                ),
                width="100%",
                height=["65vh", "75vh", "75vh"],
                margin="0.5em",  # Increased margin
            ),

            # Area 3: Footer
            rx.box(
                "Area 5 - Totales",
                width="100%",
                height=["15vh", "10vh", "10vh"],
                box_shadow="10px 5px 5px grey",
                margin="-0.5em",  # Increased margin
                border_radius="1em",
                background="linear-gradient(45deg,rgb(219, 219, 219),rgb(230, 231, 238))",
            ),
            direction="column",
            width="100%",
            align_items="center",
            gap="0.5em",  # Increased gap
        ),
        width="100%",
        padding="0.5em",  # Increased padding
        size="4",
        # Light lavender to light blue gradient
        background="linear-gradient(45deg,rgba(38, 39, 49, 0.53),rgb(230, 231, 238))"

    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",  # Can be "light" or "dark"
        has_background=True,
        radius="large",      # Options: "none", "small", "medium", "large", "full"
        accent_color="teal",  # Primary color for buttons, typography, etc
        gray_color="mauve",  # Secondary color scheme
        panel_background="solid"  # "solid" or "translucent"
    )
)
