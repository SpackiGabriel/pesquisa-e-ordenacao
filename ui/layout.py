import flet
from flet import (
    TextField,
    Dropdown,
    dropdown,
    ElevatedButton,
    Text,
    Column,
    Row,
    SnackBar,
    ProgressRing,
)
from sort_runner import SORT_FUNCTIONS

def build_layout(page):
    snack_bar = SnackBar(content=Text(""))
    page.snack_bar = snack_bar

    size_input = TextField(label="Tamanho da lista", width=200, value="10", keyboard_type="number")
    algo_dropdown = Dropdown(
        label="Algoritmo",
        options=[dropdown.Option(name) for name in SORT_FUNCTIONS.keys()],
        value="Bubble Sort",
        width=200,
    )
    order_dropdown = Dropdown(
        label="Ordem inicial",
        options=[
            dropdown.Option("Normal"),
            dropdown.Option("Ordenada"),
            dropdown.Option("Invertida"),
        ],
        value="Normal",
        width=200,
    )

    original_txt = Text("Lista gerada: —")
    sorted_txt   = Text("Lista ordenada: —")
    time_txt     = Text("Tempo de execução: —")

    run_button  = ElevatedButton(text="Gerar e Ordenar")
    save_button = ElevatedButton(text="Salvar", disabled=True)
    spinner     = ProgressRing(visible=False, width=40, height=40)

    page.add(
        Column(
            [
                Row(
                    [size_input, algo_dropdown, order_dropdown, run_button, save_button, spinner],
                    wrap=True,
                    spacing=10,
                ),
                Column([original_txt, sorted_txt, time_txt], spacing=10),
            ],
            spacing=20,
        )
    )

    return {
        "snack_bar": snack_bar,
        "size_input": size_input,
        "algo_dropdown": algo_dropdown,
        "order_dropdown": order_dropdown,
        "original_txt": original_txt,
        "sorted_txt": sorted_txt,
        "time_txt": time_txt,
        "run_button": run_button,
        "save_button": save_button,
        "spinner": spinner,
    }
