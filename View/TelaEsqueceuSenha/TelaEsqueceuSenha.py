from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp


class TelaEsqueceuSenha(MDScreen, StencilBehavior):
    def __init__(self, **kw):
        super().__init__(**kw)
        print("Tela Esqueceu Senha inicializada com sucesso.")
    
    def irParaTela(self, tela: str, direcao: str) -> None:
        print(f"Carregando: {tela}, direção: {direcao}")
        self.app = MDApp.get_running_app()
        self.app.root.transition.direction = direcao
        self.app.root.current = tela

    def irParaTelaLogin(self, *args):
        self.irParaTela(tela="tela_login", direcao="right")
