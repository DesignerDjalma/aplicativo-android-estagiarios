from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(dirname(abspath(__file__)))))
from utils.validacoes import Validacao


class TelaCadastroUsuario(MDScreen, StencilBehavior):
    def __init__(self, **kw):
        super().__init__(**kw)
        print("Tela Cadastro Usuario inicializada com sucesso.")
        
    def on_pre_enter(self, *args):
        self.limparTudo()

    def on_enter(self, *args):
        pass

    def irParaTela(self, tela: str, direcao: str) -> None:
        print(f"Carregando: {tela}, direção: {direcao}")
        self.app = MDApp.get_running_app()
        self.app.root.transition.direction = direcao
        self.app.root.current = tela

    def irParaTelaRegistrarUsuario(self, *args):
        print("Realizando Cadastro de Novo usuário!")
        self.irParaTela(tela="tela_login", direcao="right")

    def limparTudo(self) -> None:
        self.ids.nome_field.text = ""
        self.ids.nome_field_txt_erro.text = ""
        self.ids.username_field.text = ""
        self.ids.username_field_txt_erro.text = ""
        self.ids.setor_field.text = ""
        self.ids.setor_field_txt_erro.text = ""
        self.ids.email_field.text = ""
        self.ids.email_field_txt_erro.text = ""
        self.ids.senha_field.text = ""
        self.ids.senha_field_txt_erro.text = ""
        self.ids.confirmar_senha_field.text = ""
        self.ids.confirmar_senha_field_txt_erro.text = ""

    def registrarNovoUsuario(self, *args):
        pass

    def validarDados(self, *args):
        v1 = self.validarEmail()     
        v2 = self.validarUsername()  
        v3 = self.validarNome()      
        v4 = self.validarSenha()     
        v5 = self.confirmarSenhas()  
        v6 = self.validarSetor()    
        
        validacoes = [v1,v2,v3,v4,v5,v6]

        if all(validacoes):
            print("Validações Okay!")
            self.registrarNovoUsuario()
        else:
            print("Validção NOT Okay!")


    def validarEmail(self, *args) -> bool:
        email_valid = Validacao().validarEmail(self.ids.email_field.text)
        self.ids.email_field_txt_erro.text = email_valid[2]
        
        if email_valid[0]:
            self.ids.email_field_txt_erro.text_color = [0.00,0.65,0.00]
            return True
        else:
            self.ids.email_field_txt_erro.text_color = [0.99,0.00,0.00]
            return False

    def validarUsername(self, *args) -> bool:
        username_valid = Validacao().validaUsername(self.ids.username_field.text)
        self.ids.username_field_txt_erro.text = username_valid[2]

        if username_valid[0]:
            self.ids.username_field_txt_erro.text_color = [0.00,0.65,0.00]
            return True
        else:
            self.ids.username_field_txt_erro.text_color = [0.99,0.00,0.00]
            return False

    def validarNome(self, *args) -> bool:
        return True

    def validarSenha(self, *args) -> bool:
        return True

    def confirmarSenhas(self, *args) -> bool:
        return True

    def validarSetor(self, *args) -> bool:
        return True



if __name__ == "__main__":
    pass