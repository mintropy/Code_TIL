import reflex as rx
from rxconfig import config

# from reflex_sample_app.api.main import app as _app
# from reflex_sample_app.api.main import main_api
from reflex_sample_app.components.nav import navbar
from reflex_sample_app.models.account_book import AccountBook
from reflex_sample_app.pages.articles import articles

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    amount: int = 0

    def print_amount(self) -> None:
        print(self.amount)

    def update_amount(self, amount: int) -> None:
        self.amount = amount


class AccountBookTable(rx.State):
    cols: list[dict] = [
        {"title": "ID", "type": "int"},
        {"title": "Amount", "type": "int"},
    ]
    data: list[list] = []

    def get_account_book(self):
        with rx.session() as session:
            books = session.exec(AccountBook.select).all()  # type: ignore
            self.data = [[book.id, book.amount] for book in books]

    def create_account_book(amount: int):
        with rx.session() as session:
            session.add(AccountBook(amount=amount))
            session.commit()


def index() -> rx.Component:
    sample_data = [[1, 1000], [2, 4000], [3, 5500], [4, 10000]]

    return rx.fragment(
        navbar(),
        rx.hstack(
            rx.text("Amount"),
            rx.input(type="number", on_change=State.set_amount),
            rx.button("Update"),
            style={"margin_bottom": "20px", "margin-top": "60px"},  # type: ignore
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("id"),
                    rx.table.column_header_cell("amount"),
                )
            ),
            rx.table.body(
                *[
                    rx.table.row(rx.table.cell(data[0]), rx.table.cell(data[1]))
                    for data in sample_data
                ]
            ),
        ),
        # rx.table_container(
        #     rx.table(
        #         headers=["id", "amount"],
        #         rows=[
        #             [1, 10000],
        #             [2, 55000],
        #             [3, 500],
        #             [4, 250000],
        #         ],
        #     ),
        #     style={"padding-left": "10%", "padding-right": "10%"},
        # ),
    )


# Create app instance and add index page.
style = {"margin": "10px"}

app = rx.App(style=style)
app.add_page(index)
app.add_page(articles)


# app.api.api_route("", main_api)
# app.api.add_route("/", _app)
# app.api.add_api_route("/", main_api)
@app.api.get("/")
async def main_api():
    return "Hello World"
