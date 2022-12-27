from View.TelaCadastroUsuario import TelaCadastroUsuario
from View.TelaEsqueceuSenha import TelaEsqueceuSenha
from View.TelaInicial.TelaInicial import TelaInicial
from View.TelaLogin.TelaLogin import TelaLogin
from View.TelaPrincipal.TelaPrincipal import TelaPrincipal
from View.Widgets.minhaTopBarLogin import MinhaTopBarLogin
from View.Widgets.minhaTopBar import MinhaTopBar
from View.TelaPrincipal.TelaPrincipal import UsuarioCard
from utils.Firebase.firebase import Usuarios
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from pathlib import Path
import os
import sys

from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')


#Window.size = (360,650)


if getattr(sys, "frozen", False):
    os.environ["MEU_APP_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["MEU_APP_ROOT"] = str(Path(__file__).parent)

os.environ["MEU_APP_ASSETS"] = os.path.join(os.environ["MEU_APP_ROOT"], f"assets{os.sep}")
Window.softinput_mode = "below_target"


class EstagiariosIterpaApp(MDApp):    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.title = "Estagiários ITERPA 2023"
        self.icon = "./assets/images/icon.png"
        print('\n'*10,self.theme_cls)

    def build(self, kv="./interface.kv"):
        return Builder.load_file(kv)



if __name__ == "__main__":
    EstagiariosIterpaApp().run()
    

