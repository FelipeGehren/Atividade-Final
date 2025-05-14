# Crie um menu interativo onde o usuário pode ficar fazendo consultas de notícias
# Pergunte ao usuário um tema de notícia 
# Pergunte quantas notícias ele quer buscar sobre o tema, lembre de fazer um limitador
# Busque as N notícias mais recentes sobre o tema usando a API da News API
# Apresente as informações de título da notícia, qual a fonte e o nome da pessoa que escreveu, de forma organizada para o usuário 
# Armazene o histórico de temas que o usuário buscou e ao sair do menu, apresente no final quais foram as palavras buscadas e quantas notícias foram buscadas ao total
# Faça o envio pelo commit do Github

import requests
import os 
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY_NEWS")

if not api_key:
    raise ValueError("API key não encontrada nas variáveis de ambiente")

url = "https://newsapi.org/v2/everything"

headers = {
    'x-api-key': api_key
}

temas = {
    '1': 'tecnologia',
    '2': 'política',
    '3': 'investimentos',
    '4': 'criminal'
}

historico = []
total_noticias = 0


def menu():
    while True:

        print("\nMenu de opções:")
        print("""
            0 - Sair
            1 - Temas de notícias
            2 - Visualizar escolhas
            """)
        return input("Escolha uma opção: ")
    


def selecionar_tema():

    print("\nMenu de opções:")
    print("""
        0 - Sair
        1 - Tecnologia
        2 - Política
        3 - Investimentos
        4 - Criminal
        """)
    return temas.get(input('Escolha um tema: '))

def buscar_noticias(tema, quantidade):
    global total_noticias
    params = {
        'q': tema,
        'pageSize': quantidade,
        'sortBy': 'publishedAt',
        'Language': 'pt',
    }
    resposta = requests.get(url=url, headers=headers, params=params)
    if resposta.status_code == 200:
        noticias = resposta.json().get('articles', [])
        


while True:

    opcao = menu()
   
    if opcao == "0":
        print("Saindo do programa.")
        break
    elif opcao == "1":
        selecionar_tema()
         