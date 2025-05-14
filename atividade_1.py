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

historico_buscas = []

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
    opcao = input("Escolha uma opção: ")
    return temas.get(opcao)

def ver_historico():
    if historico_buscas:
        print("\n Histórico das buscas realizadas:")
        for tema, quantidade in historico_buscas:
            print(f"Tema: {tema}, Quantidade de buscas: {quantidade}")
    else:
        print("Nenhuma busca realizada.")


def buscar_noticias(tema, quantidade):

    params = {
        'q': tema,
        'pageSize': quantidade,
        'sortBy': 'publishedAt',
        'Language': 'pt',
    }


    resposta = requests.get(url=url, headers=headers, params=params)

    if resposta.status_code == 200:
        noticias = resposta.json().get('articles', [])
        if noticias:
            print(f"{len(noticias)} noticias encontradas sobre o tema: {tema}")
        
        for noticia in noticias:
            titulo = noticia.get('title', 'Sem título')
            fonte = noticia.get('source')
            autor = noticia.get('author')

            print(f"Título: {titulo}")
            print(f"Fonte: {fonte}")
            print(f"Autor: {autor}")
            
        return len(noticias)
    
while True:

    opcao = menu()
   
    if opcao == "0":
        print("Saindo do programa.")
        break
    elif opcao == "1":
        tema = selecionar_tema()
        if tema:
            quantidade = int(input("Quantas noticias deseja visualizar? (Máximo 5): "))
            if quantidade > 0 and quantidade <= 10:
                quantidade_noticias = buscar_noticias(tema, quantidade)
            else:
                print("Quantidade inválida, tente novamente.")

    elif opcao == "2":
        ver_historico()
    
    else:
        print("Solicitação inválida, tente novamente.")