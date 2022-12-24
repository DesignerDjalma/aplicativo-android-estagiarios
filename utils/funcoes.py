
def irParaTela(app, tela: str, direcao: str) -> None:
    print(f"Carregando: {tela}, direção: {direcao}")
    app.root.transition.direction = direcao
    app.root.current = tela