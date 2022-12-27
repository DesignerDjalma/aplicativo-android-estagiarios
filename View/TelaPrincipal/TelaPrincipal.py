from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from os.path import dirname, abspath
import os
import sys
sys.path.append(dirname(dirname(dirname(abspath(__file__)))))
from utils.Firebase.firebase import Usuarios
from utils.funcoes import escolherAvatarAleatorio


class RectangularCard(MDCard):
    pass

class UsuarioCard(RectangularCard):
    image = StringProperty()


class TelaPrincipal(MDScreen, StencilBehavior):

    lista_de_cards: set = set()

    def __init__(self, **kw):
        super().__init__(**kw)
        print("Tela Principal inicializada com sucesso.")

    
    def on_enter(self):
        usuarios = Usuarios().getUsuariosKivy()
        
        if not self.ids.content.children:
            for user in usuarios.keys():

                # Só pra pegar a info do setor
                try: setor = usuarios[user]['setor']
                except: usuarios[user]['setor'] = "SEM INFO"

                scard = UsuarioCard(
                        image=abspath(f"{os.environ['MEU_APP_ASSETS']}images/avatar/{escolherAvatarAleatorio()}.jpg"),
                    )
                scard.ids.titulodomdcard.text = f"{usuarios[user]['username']} - {usuarios[user]['setor']}"
                scard.ids.subtitulodomdcard.text = usuarios[user]['email']
                self.lista_de_cards.add(scard)
                self.ids.content.add_widget(scard)


        for i in self.ids.content.children:
            print(i)

    def on_leave(self, *args):
        for i in self.lista_de_cards:
            print(f"Removendo {i}")
            self.ids.content.remove_widget(i)
        self.lista_de_cards = set()


if __name__ == "__main__":

    print(Usuarios().getUsuariosKivy())