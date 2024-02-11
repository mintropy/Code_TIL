import reflex as rx

from reflex_sample_app.components.nav import navbar


class Articles(rx.State):
    articles: list[dict] = []


@rx.page(route="/articles/")
def articles() -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.hstack(
            rx.heading("Articles"),
            style={"margin_bottom": "20px", "margin-top": "60px"},
        ),
    )
