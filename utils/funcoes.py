from random import randint

def escolherAvatarAleatorio() -> str:
    """Escolhe um numero aleatorio para retornar um avatar.png"""
    numeroAleatorio = randint(1,30)
    return f"avatar{numeroAleatorio}"

def formataNomeDoUsuario(nome_e_sobrenome: str) -> str:
    partes = nome_e_sobrenome.split(' ')
    if len(partes) > 1:
        return f"{partes[0]} {partes[1]}"
    elif len(partes) == 1:
        return f"{partes[0]}"
    else:
        return "Estagiário"

def txt(txt, mod='i'):
    return f"    [{mod}]{txt}[/{mod}]"
