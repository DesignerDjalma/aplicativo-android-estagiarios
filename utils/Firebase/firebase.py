import requests
import json
import threading
from multiprocessing.pool import ThreadPool

def thread(function):
    print("Executando thread...")
    
    def wrap(*args, **kwargs):
        print("Executando thread.wrap")
        t = threading.Thread(target=function, args=args,kwargs=kwargs,daemon=True)
        t.start()
        print("Retornando t.start()")
        return t
    print("Retornando wrap")
    return wrap

def processos(funcao):
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
    acesso: str = "LogarUsuario"
    registro: str = "usuarios"
    recuperar: str = "RecuperarSenha"


class Requisicao:
    @staticmethod
    def tipo(_tipo: TipoRequisicao) -> str:
        return f"{MeuFireBase.url}/py/{_tipo}.json"

class Usuario:
    @staticmethod
    def novoUsuario(nome: str="", setor: str="", email: str="", senha: str=""):
        pass
def getServerStatus():
    return processos(BancoDeDados.status)

  # get the return value from your function.


if __name__ == "__main__":
    getServerStatus()