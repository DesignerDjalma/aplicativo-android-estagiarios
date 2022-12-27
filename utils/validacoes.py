import string
import re
from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))
from utils.funcoes import txt

def validaCaracteres(palavra: str) -> bool:
    for l in palavra:
        if l in [i for i in f" {string.punctuation}"]:
            return False
    return True

def validaEmail(email: str) -> bool:   
    expressao_regex = re.compile(R'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    email_valido = re.fullmatch(expressao_regex, email)
    
    if email_valido:
        return True
    else:
        return False

def validaSenha(senha: str) -> bool:
    expressao_regex = re.compile(R"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$")
    senha_valido = re.fullmatch(expressao_regex, senha.replace(' ',''))
    print(f"{senha, senha_valido}")
    
    if senha_valido:
        print(f"Essa senha é válida")
        return True
    else:
        print(f"Essa senha não é válida")
        return False

class Validacao:
    # _nome_valid: bool = False
    # _email_valid: bool = False
    # _usuario_valid: bool = False
    # _senha_valid: bool = False
    # _senha_check_valid: bool = False
    # _senha_verificar: bool = False

    def validarEmail(self, email: str="email@gmail.com"):
        email = str(email)
        msgErro = ""
        
        if email:
            if validaEmail(email):
                msgErro = txt(
                    "Esse email é válido"
                )
                return True, email, msgErro
            else:
                msgErro = txt(
                    "Esse email não é válido"
                )
                return False, email, msgErro
        else:
            msgErro = txt(
                "Esse email não é válido"
            )
            return False, email, msgErro         

    def validaUsername(self, username: str="Estagiário") -> tuple:
        username = str(username)
        msgErro = ""
        if username:
            if not validaCaracteres(username):
                msgErro = txt(
                    "Caracteres especiais não são permitidos"
                    )
            else:
                if 3 >= len(username) >= 1:
                    msgErro = txt(
                        "O nome de usuário deve ter pelo menos 4 caracteres"
                        )

                if 20 < len(username):
                    msgErro = txt(
                        "O nome de usuário deve ter no máximo 20 caracteres"
                        )
        else:
            msgErro = txt(
                "Forneça um usuário válido"
                )
            
        if not msgErro:
            # self._usuario_valid = True
            return True, username, msgErro
        return False, username, msgErro

    def validaSenha(self, senha: str="Abc@1234") -> tuple:
        senha = str(senha)
        msgErro = ""
        if validaSenha(senha):
            if 7 >= len(senha) >= 1:
                msgErro = txt(
                    "A senha deve conter pelo menos 8 caracteres"
                    )
            elif 32 < len(senha): 
                msgErro = txt(
                    "A senha deve ter no máximo 32 caracteres"
                    )
            else:
                #self._senha_valid = True
                pass
        else:
            msgErro = txt(
                "Forneça uma senha válida"
                )
        if not msgErro:
            msgErro = txt(
                "Essa senha é forte"
                )
            return True, senha, msgErro
        return False, senha, msgErro


if __name__ == "__main__":
    print(dirname(dirname(dirname(abspath(__file__)))))
    print(Validacao().validaUsername(""))
    # print(Validacao().validaSenha())
    # print(Validacao().validarEmail(""))