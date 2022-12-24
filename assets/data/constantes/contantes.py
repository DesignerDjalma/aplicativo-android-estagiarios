from dataclasses import dataclass


@dataclass
class Constantes:
    user_email: str
    user_name: str
    user_password: str
    tela_atual: str
    telas_visitadas: list


if __name__ == "__main__":
    print(Constantes)

    c = Constantes(
        user_email="example@your.email.com",
        user_name="Your_username",
        user_password="Password@123",
        )
        
    print(c)

    c.user_email = "other@email.com"
    c.user_name = "Other_username"
    c.user_password = "Other@pw123"

    print(c.__getattribute__('user_email'))