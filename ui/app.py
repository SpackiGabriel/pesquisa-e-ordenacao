from flet import Page
from ui.layout import build_layout
from ui.handlers import register_handlers

def run_app(page: Page):
    page.title = "Comparador de Sorts"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    page.padding = 20

    controls = build_layout(page)
    register_handlers(page, controls)
