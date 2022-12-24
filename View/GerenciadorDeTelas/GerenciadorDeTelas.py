import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, NoTransition

from kivymd.app import MDApp

from View.telas import telas


class GerenciadorTelas(ScreenManager):
    dialogo_espera = None
    _nomes_telas = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.transition = NoTransition()

    def criar_telas(self, nome_da_tela):
        if nome_da_tela not in self._nomes_telas:
            self._nomes_telas.append(nome_da_tela)
            self.carregador_pacote_de_tela(nome_da_tela)
            exec(f"import View.{telas[nome_da_tela]}")
            self.app.load_all_kv_files(
                os.path.join(self.app.directory, "View", telas[nome_da_tela].split(".")[0])
            )
            view = eval(
                f'View.{telas[nome_da_tela]}.{telas[nome_da_tela].split(".")[0]}View()'
            )
            view.name = nome_da_tela
            return view

    def carregador_pacote_de_tela(self, nome_da_tela) -> None:
        def _load_kv(caminho_do_kv):
            kv_carregado = False
            for caminho_kv_carregadi in Builder.files:
                if caminho_do_kv in caminho_kv_carregadi:
                    kv_carregado = True
                    break
            if not kv_carregado:
                if nome_da_tela in ["list"]:
                    from kivy.factory import Factory

                    Factory.register(
                        "OneLineItem",
                        module="View.common.onelinelistitem.one_line_list_item",
                    )
                Builder.load_file(caminho_do_kv)

        one_line_list_item_path = os.path.join(
            "View", "common", "onelinelistitem", "one_line_list_item.kv"
        )
        dots_path = os.path.join("View", "common", "dots", "dots.kv")

        if nome_da_tela in ["list"]:
            _load_kv(one_line_list_item_path)
        elif nome_da_tela in ["button", "field"]:
            _load_kv(dots_path)

    def trocar_de_tela(self, nome_da_tela: str) -> None:
        def trocar_de_tela(*args):
            if nome_da_tela not in self._nomes_telas:
                self.open_dialog()
                tela = self.criar_telas(nome_da_tela)
                self.add_screen(tela)

            self.current = nome_da_tela
            self.dialogo_espera.dismiss()

        if nome_da_tela not in self._nomes_telas:
            self.open_dialog()
            Clock.schedule_once(trocar_de_tela)
        else:
            self.current = nome_da_tela

    def open_dialog(self) -> None:
        if not self.dialogo_espera:
            image = Image(
                source="assets/images/loading.gif",
                size_hint=(0.15, 0.15),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            self.dialogo_espera = ModalView(
                background="assets/images/modal-bg.png",
            )
            self.dialogo_espera.add_widget(image)
        self.dialogo_espera.open()

    def add_screen(self, view) -> None:
        self.add_widget(view)
