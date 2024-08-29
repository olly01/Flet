from flet import *;

def main(page: Page):
    BG = '#041855'
    FWG = '#96B4FF'
    FG= '#3450a1'
    PINK = '#eb06ff'
    page_1 =Container()
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor = FG
            )
        ]
    )
    container = Container(
        width=400, 
        height = 850, 
        bgcolor=BG,
        border_radius =35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    page.add(container)
    

app(target=main)