import reflex as rx


class AccountBook(rx.Model, table=True):
    amount: int
