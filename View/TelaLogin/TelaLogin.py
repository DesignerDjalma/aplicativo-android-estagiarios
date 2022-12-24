from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp


class TelaLogin(MDScreen, StencilBehavior):
    def __init__(self, **kw):
        super().__init__(**kw)
        print("Tela de Login inicializada com sucesso.")

    def irParaTela(self, tela: str, direcao: str) -> None:
        print(f"Carregando: {tela}, direção: {direcao}")
        self.app = MDApp.get_running_app()
        self.app.root.transition.direction = direcao
        self.app.root.current = tela

    def irParaTelaEsqueceuSenha(self):
        self.irParaTela(tela="tela_esqueceu_senha",direcao="left")
          
    def irParaTelaPrincipal(self):
        self.irParaTela(tela="tela_principal",direcao="left")

    def irParaTelaCadastroUsuario(self):
        self.irParaTela(tela="tela_cadastro_usuario",direcao="left")

        

