import json
import requests
from multiprocessing.pool import ThreadPool
from kivy.network.urlrequest import UrlRequest


# def thread(function):
#     print("Executando thread...")
    
#     def wrap(*args, **kwargs):
#         print("Executando thread.wrap")
#         t = threading.Thread(target=function, args=args,kwargs=kwargs,daemon=True)
#         t.start()
#         print("Retornando t.start()")
#         return t
#     print("Retornando wrap")
#     return wrap

def processos(funcao) -> str:
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(funcao, ())
    return async_result.get()


def isBancoDeDadosOnline(url: str) -> bool:
    """Retorna um responde.status_code. 200 -> Online."""
    print("Pegando resposta do servidor...")
    r = requests.get(url)
    print(f"Resposta: {r}")
    return False if r.status_code != 200 else True 

def statusBancoDeDados() -> str:
    """Verifica se o BD está online."""
    res = isBancoDeDadosOnline(MeuFireBase.url)
    msg = "online" if res else "offline"
    print(f"Banco de Dados: {msg.upper()}!")
    return msg.upper()

class BancoDeDados:

    banco_de_dados_status: str

    @staticmethod
    def status():
        print("Executando função com Thread BandoDeDados.status()")
        return statusBancoDeDados()





class MeuFireBase:
    url: str = "https://appcadastro-72250-default-rtdb.firebaseio.com/"
    

class TipoRequisicao:
    acesso: str = "usuarios"
    registro: str = "usuarios"
    recuperar: str = "RecuperarSenha"


class Requisicao:
    @staticmethod
    def tipo(_tipo: TipoRequisicao) -> str:
        return f"{MeuFireBase.url}py/{_tipo}.json"

class Usuario:
    usuarios_dict = {}

    @staticmethod
    def novoUsuario(nome: str="", setor: str="", email: str="", senha: str=""):
        pass
    @staticmethod
    def verUsuarios(tipo: TipoRequisicao = TipoRequisicao.acesso) -> None:
        """Entra na base dos dados e mostra o tipo especificado de dado."""
        
        url = Requisicao.tipo(tipo)
        req = requests.get(url)
        if req.status_code != 200:
            return False, "Erro"
        else:
            users = json.loads(req.text)
            if isinstance(users, list):
                return False, users[1:]
            else:
                return True, users
    
    @staticmethod
    def verUsuariosKivy(tipo: TipoRequisicao = TipoRequisicao.acesso) -> None:
        """Entra na base dos dados e mostra o tipo especificado de dado."""

        def success(req, result):
            print(result)
            print('success')

        def fail(req, result):
            print('fail')

        def error(req, result):
            print('error')

        def progress(req, result, chunk):
            print('loading')


        url = Requisicao.tipo(tipo)
        print(f"URL {url}")
        
        req = UrlRequest(
            url,
            on_success=success,
            on_failure=fail,
            on_error=error,
            on_progress=progress
        )
        req.wait()

        if req.resp_status != 200:
            return False, "Erro"
        else:
            users = json.loads(req.text)
            if isinstance(users, list):
                return False, users[1:]
            else:
                return True, users

def getServerStatus():
    return processos(statusBancoDeDados)


  # get the return value from your function.


if __name__ == "__main__":
    # print(Usuario.verUsuarios())
    #print(getServerStatus())
    u = Usuario.verUsuariosKivy()
    print(u)