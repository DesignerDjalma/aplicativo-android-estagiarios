from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.app import MDApp

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
        self.app = MDApp.get_running_app()
        usuarios = self.app.carregarBancoDeDados()[1]
        
        if not self.ids.content.children:
            for user in usuarios.keys():
                scard = SliverCard(
                        image=f"{os.environ['MEU_APP_ASSETS']}\\images\\tela_principal\\avatar.jpg"
                    )
                scard.ids.titulodomdcard.text = usuarios[user]['username']
                scard.ids.subtitulodomdcard.text = usuarios[user]['email']
                self.ids.content.add_widget(scard)

