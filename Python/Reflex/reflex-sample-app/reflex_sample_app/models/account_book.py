import reflex as rx  # type: ignore


class AccountBook(rx.Model, table=True):  # type: ignore
    amount: int
