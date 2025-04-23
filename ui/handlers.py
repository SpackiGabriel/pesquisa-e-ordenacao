import os
import threading
from flet import Text
from datetime import datetime


def register_handlers(page, c):
    def on_run_click(e):
        try:
            size = int(c["size_input"].value)
            if size < 0:
                raise ValueError()
        except ValueError:
            c["snack_bar"].content = page.controls["snack_bar"].content = page.controls["snack_bar"].content = None
            c["snack_bar"].content = page.controls["snack_bar"].content = None
            c["snack_bar"].content = page.controls["snack_bar"].content = f"Por favor, insira um número inteiro ≥ 0."
            c["snack_bar"].open = True
            page.update()
            return

        order    = c["order_dropdown"].value
        alg_name = c["algo_dropdown"].value
        sort_fn  = __import__("sort_runner", fromlist=["SORT_FUNCTIONS"]).SORT_FUNCTIONS[alg_name]

        c["spinner"].visible = True
        c["run_button"].disabled = True
        c["save_button"].disabled = True
        page.update()

        def worker():
            arr, sorted_arr, elapsed = None, None, None
            arr = __import__("sort_runner", fromlist=["generate_list"]).generate_list(size, order)
            sorted_arr, elapsed = __import__("sort_runner", fromlist=["run_sort"]).run_sort(sort_fn, arr)
            c["original_txt"].value = f"Lista gerada ({order}): {arr}"
            c["sorted_txt"].value   = f"{alg_name} → {sorted_arr}"
            c["time_txt"].value     = f"Tempo: {elapsed*1000:.3f} ms"

            c["last_run"] = {
                "size": size,
                "order": order,
                "algorithm": alg_name,
                "original": arr,
                "sorted": sorted_arr,
                "time_ms": elapsed * 1000,
            }

            c["save_button"].disabled = False
            c["spinner"].visible = False
            c["run_button"].disabled = False
            page.update()

        threading.Thread(target=worker).start()

    def on_save_click(e):
        os.makedirs("outputs", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        lr = c["last_run"]
        fn = f"{lr['algorithm'].replace(' ', '')}_{lr['size']}_{lr['order']}_{ts}.txt"
        path = os.path.join("outputs", fn)
        txt = (
            f"Algoritmo: {lr['algorithm']}\n"
            f"Tamanho: {lr['size']}\n"
            f"Ordem inicial: {lr['order']}\n"
            f"Tempo: {lr['time_ms']:.3f} ms\n"
            f"\n-------------------------\n\n"
            f"Lista gerada: {lr['original']}\n"
            f"Lista ordenada: {lr['sorted']}\n"
        )
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(txt)
            c["snack_bar"].content = Text(f"Salvo em: {path}")
        except Exception as err:
            c["snack_bar"].content = Text(f"Erro ao salvar: {err}")
        c["snack_bar"].open = True
        c["save_button"].disabled = True
        page.update()

    c["run_button"].on_click = on_run_click
    c["save_button"].on_click = on_save_click
