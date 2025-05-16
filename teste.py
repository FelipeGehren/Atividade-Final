import requests

url = 'https://jsonplaceholder.typicode.com'
usuarios_db = {}

def login():
    while True:
        nome = input("Usuário: ")
        senha = input("Senha: ")

        if nome in usuarios_db:
            if usuarios_db[nome]['senha'] == senha:
                print(f" Bem-vindo de volta, {nome}!")
                return usuarios_db[nome]['userId']
            print(" Senha incorreta.")
        else:
            user_id = len(usuarios_db) + 1
            usuarios_db[nome] = {'senha': senha, 'userId': user_id}
            print(f" Novo usuário criado: {nome} (ID: {user_id})")
            return user_id

def ver_posts():
    try:
        resposta = requests.get(f'{url}/posts')
        resposta.raise_for_status()
        for post in resposta.json()[:10]:
            print(f"\n Post {post['id']} - {post['title']}")
    except requests.RequestException:
        print("Erro ao buscar posts.")

def ver_comentarios():
    post_id = input("ID do post: ")
    if not post_id:
        print("ID inválido.")
        return
    
    try:
        resposta = requests.get(f'{url}/posts/{post_id}/comments')
        resposta.raise_for_status()
        for c in resposta.json():
            print(f"\n {c['email']}: {c['body']}")
    except requests.RequestException:
        print("Erro ao buscar comentários.")

def ver_meus_posts(user_id):
    try:
        resposta = requests.get(f'{url}/posts', params={'userId': user_id})
        resposta.raise_for_status()
        posts = resposta.json()
        if posts:
            for post in posts:
                print(f"\n {post['title']}\n{post['body']}")
        else:
            print("Nenhum post encontrado.")
    except requests.RequestException:
        print("Erro ao buscar seus posts.")

def sistema():
    print("=== Sistema de Posts ===")
    user_id = login()

    while True:
        print("\nMenu:\n1. Ver posts\n2. Ver comentários\n3. Meus posts\n4. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            ver_posts()
        elif opcao == '2':
            ver_comentarios()
        elif opcao == '3':
            ver_meus_posts(user_id)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")
            

sistema()