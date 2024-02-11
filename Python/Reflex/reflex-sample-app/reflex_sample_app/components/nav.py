import reflex as rx


def navbar():
    return rx.hstack(
        rx.hstack(
            rx.heading("My App"),
        ),
        rx.hstack(
            rx.link("Home", href="/"),
            rx.link("Articles", href="/articles"),
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
        style={"margin-bottom": "50px"},
    )
