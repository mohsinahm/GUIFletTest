from flet import *
import flet_fastapi

async def main(page: Page):
    await page.add_async(Text("Testing is working bro", size=30, weight="bold"))

app = flet_fastapi.app(main)
