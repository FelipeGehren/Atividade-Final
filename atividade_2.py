#Permita um menu interativo onde o usuário possa:
#Primeiro, se identificar e, com isso, fazer uma verificação se usuário existe (tenha um dicionário simulando um banco de dados com código, e-mail e senha, por exemplo).
#Após login, permita a ele: visualizar posts e comentários.
#Visualizar seus próprios posts.
#Filtrar posts por algum outro usuário.
#Criar um novo post (usar usuário logado).
#Exibir um resumo das interações feitas ao sair do laço (quantos posts e comentários foram visualizados e quantos posts foram criados por ele).

import requests

url = "https://jsonplaceholder.typicode.com/"

def menu():
    print("\nMenu de opções:")
    print("""
    0 - Sair
    1 - Login
    2 - Cadastre-se
    """)
    return input("Escolha uma opção: ")

