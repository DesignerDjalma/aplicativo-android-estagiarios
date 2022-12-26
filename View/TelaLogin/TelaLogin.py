from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
import sys
sys.path.append(r"C:\Users\dflfilho\Documents\repositorios\aplicativo-android-estagiarios\utils\Firebase")
import firebase

BANCO_DE_DADOS = firebase.BancoDeDados()

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

    def on_enter(self, *args):
        res = firebase.statusBancoDeDados()
        
        if res == "ONLINE":
            self.ids.server_status.text_color = [93/255,157/255,93/255]
        else:
             self.ids.server_status.text_color = [1,0,0]

        self.ids.server_status.text = res

from multiprocessing.pool import ThreadPool

def processos(funcao) -> str:
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(funcao, ())
    return async_result.get()
