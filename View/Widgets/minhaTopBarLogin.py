from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp


class MinhaTopBarLogin(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Minha Top Bar Login inicializada com sucesso!")
        self._parametros: dict = {"theme_text_color":"Custom",
            "text_color":self.theme_cls.primary_color,}

    def sairApp(self, *args):
        print("Saindo do App")
        self.app = MDApp.get_running_app()
        self.app.stop()

    def fecharDialogo(self, *args):
        print("Fechando Dialogo!")
        self.dialogo.dismiss(force=True)

    def funcaoVoltarLogin(self, *args):
        print("Fechando Dialogo!")
        self.dialogo.dismiss(force=True)
    
    def funcaoHelpBox(self, *args):
        print("Criando Dialogo de Ajuda.")
        self.dialogo = MDDialog(title="Ajuda",
            text="[b]Como usar:[/b]\n\nVocê pode logar dentro do Aplicativo e vizualizar seus status utilizando o botão login. \n\nVocê pode sempre registrar uma nova conta utilizando o botão Registrar-se. \n\nVocê também pode clicar em \"esqueceu sua senha\" caso não lembre de sua senha, um e-mail será enviado para você com mais instruções.\n\n[b]EM FASE DE TESTES[/b]",
            buttons=[
                MDFlatButton(
                    text="ENTENDI",
                    on_release=lambda btn: self.fecharDialogo(btn),
                    **self._parametros)
            ],
        )
        self.dialogo.open()

    def funcaoLogout(self, *args):
        print("Criando Dialogo Logout.")

        self.dialogo = MDDialog(title="Fechar Aplicativo?",
            text="Você está prestes a sair do aplicativo.",
            buttons=[
                MDFlatButton(
                    text="CANCELAR",
                    on_release=lambda btn: self.fecharDialogo(btn),
                    **self._parametros
                    ),
                MDFlatButton(
                    text="SIM",
                     on_release=lambda btn: self.sairApp(btn),
                    **self._parametros
                    ),
            ],
        )
        self.dialogo.open()



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
