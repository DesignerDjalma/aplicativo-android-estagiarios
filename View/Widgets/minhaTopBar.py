from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp


class MinhaTopBar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Minha Top Bar inicializada com sucesso!")
        self._parametros: dict = {"theme_text_color":"Custom",
            "text_color":self.theme_cls.primary_color,}

    def irParaTela(self, tela: str, direcao: str) -> None:
        print(f"Carregando: {tela}, direção: {direcao}")
        self.app = MDApp.get_running_app()
        self.app.root.transition.direction = direcao
        self.app.root.current = tela

    def funcaoVoltarLogin(self, *args):
        self.irParaTela(tela="tela_login", direcao="right")



if __name__ == "__main__":
    pass















# Menu Items
# def funcaoHelpBox(self, btn):
#     menu_items = [
#         {
#             "viewclass": "OneLineListItem",
#             "text": f"Ajuda...",
#             "height": dp(48),
#             "on_release": lambda x=f"Ajuda...": self.funcaoMenuDropDownMostrarAjuda(x),
#         }
#         ]
#     self.menu = MDDropdownMenu(
#         items=menu_items,
#         width_mult=4,
#     )
#     self.menu.caller = btn
#     self.menu.open()
