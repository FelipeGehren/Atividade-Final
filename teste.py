import requests

# Simula o banco de dados de usuários
usuarios_db = {
    # 'usuario_exemplo': {'senha': '123', 'userId': 1}
}

BASE_URL = 'https://jsonplaceholder.typicode.com'


def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\nMenu:")
    print("1. Ver todos os posts")
    print("2. Ver comentários de um post")
    print("3. Ver meus próprios posts")
    print("4. Sair")


def login_ou_criar_usuario():
    """Gerencia login ou criação de conta."""
    while True:
        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ").strip()

        if nome in usuarios_db:
            if usuarios_db[nome]['senha'] == senha:
                print(f"✅ Login bem-sucedido! Bem-vindo, {nome}")
                return usuarios_db[nome]['userId']
            else:
                print("❌ Senha incorreta. Tente novamente.")
        else:
            print("🔐 Usuário não encontrado. Criando novo usuário...")
            novo_id = len(usuarios_db) + 1
            usuarios_db[nome] = {'senha': senha, 'userId': novo_id}
            print(f"✅ Usuário criado com sucesso! Seu userId é {novo_id}")
            return novo_id


def ver_todos_posts():
    """Exibe os primeiros 10 posts."""
    response = requests.get(f'{BASE_URL}/posts')
    if response.ok:
        posts = response.json()
        for post in posts[:10]:
            print(f"\nPost ID: {post['id']}\nTítulo: {post['title']}")
    else:
        print("Erro ao buscar posts.")


def ver_comentarios_post():
    """Exibe os comentários de um post específico."""
    post_id = input("Digite o ID do post: ").strip()
    if not post_id.isdigit():
        print("ID inválido.")
        return

    response = requests.get(f'{BASE_URL}/posts/{post_id}/comments')
    if response.ok:
        comentarios = response.json()
        for c in comentarios:
            print(f"\nAutor: {c['email']}\nComentário: {c['body']}")
    else:
        print("Erro ao buscar comentários.")


def ver_meus_posts(user_id):
    """Exibe os posts do usuário logado."""
    response = requests.get(f'{BASE_URL}/posts', params={'userId': user_id})
    if response.ok:
        posts = response.json()
        if posts:
            print(f"\nVocê possui {len(posts)} post(s):")
            for post in posts:
                print(f"\nTítulo: {post['title']}\nConteúdo: {post['body']}")
        else:
            print("Você ainda não possui posts.")
    else:
        print("Erro ao buscar seus posts.")


def sistema():
    """Função principal do sistema."""
    print("Bem-vindo ao sistema de posts!")
    user_id = login_ou_criar_usuario()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            ver_todos_posts()
        elif opcao == '2':
            ver_comentarios_post()
        elif opcao == '3':
            ver_meus_posts(user_id)
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Início do programa
if __name__ == "__main__":
    sistema()
