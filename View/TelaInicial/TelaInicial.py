from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen


class TelaInicial(MDScreen, StencilBehavior):
    def __init__(self, **kw):
        super().__init__(**kw)
        print("Tela Inicial inicializada com sucesso.")
    

