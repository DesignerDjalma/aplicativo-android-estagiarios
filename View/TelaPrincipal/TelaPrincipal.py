from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen


class TelaPrincipal(MDScreen, StencilBehavior):
    def __init__(self, **kw):
        super().__init__(**kw)
        print("Tela Principal inicializada com sucesso.")

    
    

