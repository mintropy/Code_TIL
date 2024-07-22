import reflex as rx


@app.api.get("/")
async def main_api():
    return "Hello World"


app = rx.App()
app.api.add_api_route("", main_api)
