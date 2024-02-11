"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from reflex_sample_app.models.account_book import AccountBook
from rxconfig import config

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    amount: int = 0

    def print_amount(self) -> None:
        print(self.amount)

    def update_amount(self, amount: int) -> None:
        self.amount = amount


class AccountBookState(rx.State):
    id: int = 0
    amount: int

    def get_account_book(self):
        with rx.session() as session:
            self.books = session.exec(
                AccountBook.select.where(AccountBook.id == self.id)
            ).first()

    def add_account_book(self):
        with rx.session() as session:
            session.add(AccountBook(amount=self.amount))
            session.commit()


class AccountBookTable(rx.State):
    cols: list[dict] = [
        {"title": "ID", "type": "int"},
        {"title": "Amount", "type": "int"},
    ]
    data: list[list] = []

    def get_account_book(self):
        with rx.session() as session:
            books = session.exec(AccountBook.select).all()
            self.data = [[book.id, book.amount] for book in books]


@rx.page(on_load=AccountBookTable.get_account_book)
def index() -> rx.Component:
    return rx.fragment(
        # rx.text(State.amount, font_size=24, style={"margin": "20px"}),
        rx.hstack(
            rx.text("Amount"),
            rx.input(type="number", on_change=State.set_amount),
            rx.button("Update"),
            style={"margin_bottom": "20px"},
        ),
        # rx.data_editor(
        #     columns=AccountBookTable.cols,
        #     data=AccountBookTable.data,
        # ),
        rx.table_container(
            rx.table(
                headers=["id", "amount"],
                rows=[
                    [1, 10000],
                    [2, 55000],
                    [3, 500],
                    [4, 250000],
                ],
            ),
            style={"padding_left": "10%", "padding_right": "10%"},
        ),
    )


# Create app instance and add index page.
style = {"margin": "10px"}

app = rx.App(style=style)
app.add_page(index)
