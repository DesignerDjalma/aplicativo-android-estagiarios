from kivy.network.urlrequest import UrlRequest


class TipoRequisicao:

    geral: str = ""
    usuarios: str = "usuarios"


class Requisicao:

    @staticmethod
    def tipo(_tipo: TipoRequisicao) -> str:
        return f"{MeuFireBase.url}py/{_tipo}.json"


class MeuFireBase:

    usuarios_dict: dict
    servidor_status: str = "OFFLINE"
    url: str = "https://appcadastro-72250-default-rtdb.firebaseio.com/"

    def success(self, req, result):
        print('success')
        self.servidor_status = "ONLINE"

    def fail(self, req, result):
        print('fail')

    def error(self, req, result):
        print('error')

    def progress(self, req, result, chunk):
        print('loading')

    def getUsuarios(self, req, result):
        usuarios.usuarios_dict = result
        # print(result) # Meu dicionario de usuarios

    def verStatusServidor(self, tipo: TipoRequisicao = TipoRequisicao.geral) -> None:
        url = Requisicao.tipo(tipo)
        print(f"URL {url}")
        req = UrlRequest(url, on_success=self.success, on_failure=self.fail,
            on_error=self.error, on_progress=self.progress)
        req.wait()

    def getUsuariosKivy(self, tipo: TipoRequisicao = TipoRequisicao.usuarios) -> None:
        url = Requisicao.tipo(tipo)
        print(f"URL {url}")
        req = UrlRequest(url,
            on_success=self.getUsuarios,
            on_failure=self.fail,
            on_error=self.error,
            on_progress=self.progress)
        req.wait()
        return usuarios.usuarios_dict

    def novo(self, args):
 
class Usuarios:

    usuarios_dict: dict
  
    def getUsuariosKivy(self, tipo: TipoRequisicao = TipoRequisicao.usuarios) -> None:
        """Entra na base dos dados e mostra o tipo especificado de dado."""
        meuFB = MeuFireBase()
        todos_os_usuarios = meuFB.getUsuariosKivy()
        return todos_os_usuarios

  
usuarios = Usuarios()



if __name__ == "__main__":

    print("Inicio")
    r = Usuarios().getUsuariosKivy()
    print(r)

    meuFB = MeuFireBase()
    meuFB.verStatusServidor()
    print(meuFB.servidor_status)