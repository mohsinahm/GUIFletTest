import flet as ft
import time
import asyncio

def main(page: ft.Page):

    def handler(e):
      time.sleep(3)
      page.add(ft.Text("Handler clicked"))

    async def handler_async(e):
      await asyncio.sleep(3)
      page.add(ft.Text("Async handler clicked"))

    page.add(
        ft.ElevatedButton("Call handler", on_click=handler),
        ft.ElevatedButton("Call async handler", on_click=handler_async)
    )

ft.app(main)
