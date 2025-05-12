import flet as ft
import flet_fastapi


async def root_main(page: ft.Page):
    await page.add_async(ft.Text("This is root app!"))


async def sub_main(page: ft.Page):
    await page.add_async(ft.Text("This is sub app!"))


app = flet_fastapi.FastAPI()


app.mount("/sub-app", flet_fastapi.app(sub_main))
app.mount("/", flet_fastapi.app(root_main))
