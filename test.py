import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        tb1_math= int(tb1.value)
        tb2_math = int(tb2.value)
        answer = tb1_math + tb2_math
        str(answer)
        t.value = f"Textboxes values are:  '{answer}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(label="Standard")
    tb2 = ft.TextField(label="Standard")
    tb3 = ft.TextField(label="Standard")
    tb4 = ft.TextField(label="Standard")
    tb5 = ft.TextField(label="Standard")
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)

ft.app(main)