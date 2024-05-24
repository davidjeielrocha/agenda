# Author: David Jeiel de Araújo Rocha - 2472190119
import os

# Função para adicionar um novo contato à agenda
def adicionar_contato(agenda, nome, tipo_telefone, telefone):
    """Adiciona um novo contato à agenda após verificar se o nome já existe.

    Args:
        agenda: A lista de contatos.
        nome: O nome do contato.
        tipo_telefone: O tipo de telefone (cel ou fixo).
        telefone: O número de telefone.
    """
    if any(contato["nome"].lower() == nome.lower() for contato in agenda):
        print("Usuário já está cadastrado.")
        return
    agenda.append({"nome": nome, "tipo_telefone": tipo_telefone, "telefone": telefone})

# Função para gravar a agenda em um arquivo de texto
def gravar_agenda(agenda, nome_arquivo="David_Jeiel_De_Araujo_Rocha.txt"):
    """Grava os contatos da agenda em um arquivo de texto.

    Args:
        agenda: A lista de contatos.
        nome_arquivo: O nome do arquivo onde a agenda será salva (opcional, padrão: "David_Jeiel_De_Araujo_Rocha.txt").
    """
    with open(nome_arquivo, "w") as arquivo:
        for contato in agenda:
            arquivo.write(f"{contato['nome']},{contato['tipo_telefone']},{contato['telefone']}\n")

# Função para ler a agenda de um arquivo de texto
def ler_agenda(nome_arquivo="David_Jeiel_De_Araujo_Rocha.txt"):
    """Lê os contatos de um arquivo de texto e retorna uma lista de dicionários.

    Args:
        nome_arquivo: O nome do arquivo de onde a agenda será lida (opcional, padrão: "David_Jeiel_De_Araujo_Rocha.txt").

    Returns:
        Uma lista de dicionários, onde cada dicionário representa um contato com as chaves "nome", "tipo_telefone" e "telefone".
    """
    agenda = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                nome, tipo_telefone, telefone = linha.strip().split(",")
                agenda.append({"nome": nome, "tipo_telefone": tipo_telefone, "telefone": telefone})
    return agenda

# Função para ordenar a agenda por nome
def ordenar_agenda(agenda):
    """Ordena a agenda em ordem alfabética pelo nome do contato."""
    agenda.sort(key=lambda contato: contato["nome"].lower())

# Função para buscar um contato na agenda pelo nome
def buscar_contato(agenda, nome):
    """Busca um contato na agenda pelo nome.

    Args:
        agenda: A lista de contatos.
        nome: O nome do contato a ser buscado.

    Returns:
        "Nome cadastrado" se o contato for encontrado, "Nome não cadastrado" caso contrário.
    """
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            return "Nome cadastrado"
    return "Nome não cadastrado"

# Função para listar todos os contatos da agenda
def listar_contatos(agenda):
    """Lista todos os contatos da agenda."""
    if not agenda:
        print("A agenda está vazia.")
    else:
        for contato in agenda:
            print(f"Nome: {contato['nome']}, Tipo de Telefone: {contato['tipo_telefone']}, Telefone: {contato['telefone']}")

# Função principal que executa o programa
def main():
    """Função principal que controla o fluxo do programa."""
    agenda = ler_agenda()
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Ordenar Agenda")
        print("3. Buscar Contato")
        print("4. Listar Contatos")
        print("5. Gravar Agenda")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            tipo_telefone = input("Tipo de Telefone (cel/fixo): ")
            telefone = input("Telefone: ")
            adicionar_contato(agenda, nome, tipo_telefone, telefone)
        elif opcao == '2':
            ordenar_agenda(agenda)
            print("Agenda ordenada com sucesso!")
        elif opcao == '3':
            nome = input("Nome: ")
            resultado = buscar_contato(agenda, nome)
            print(resultado)
        elif opcao == '4':
            listar_contatos(agenda)
        elif opcao == '5':
            gravar_agenda(agenda)
            print("Agenda gravada com sucesso!")
        elif opcao == '6':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
