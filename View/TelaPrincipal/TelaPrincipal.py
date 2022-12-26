from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
import os

class RectangularCard(MDCard):
    pass

class SliverCard(RectangularCard):
    image = StringProperty()


class TelaPrincipal(MDScreen, StencilBehavior):
    def __init__(self, **kw):
        super().__init__(**kw)
        print("Tela Principal inicializada com sucesso.")

    
    def on_enter(self):
        if not self.ids.content.children:
            for x in range(10):
                self.ids.content.add_widget(
                    SliverCard(
                        image=f"{os.environ['MEU_APP_ASSETS']}\\images\\tela_principal\\avatar.jpg"
                    )
                )

