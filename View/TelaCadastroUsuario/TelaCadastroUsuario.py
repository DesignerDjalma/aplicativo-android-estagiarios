from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp


class TelaCadastroUsuario(MDScreen, StencilBehavior):
    def __init__(self, **kw):
        super().__init__(**kw)
        print("Tela Cadastro Usuario inicializada com sucesso.")
    
    def irParaTela(self, tela: str, direcao: str) -> None:
        print(f"Carregando: {tela}, direção: {direcao}")
        self.app = MDApp.get_running_app()
        self.app.root.transition.direction = direcao
        self.app.root.current = tela

    def irParaTelaRegistrarUsuario(self, *args):
        print("Realizando Cadastro de Novo usuário!")
        self.irParaTela(tela="tela_login", direcao="right")