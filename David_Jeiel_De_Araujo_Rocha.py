import os

def adicionar_contato(agenda, nome, tipo_telefone, telefone):
    if any(contato["nome"].lower() == nome.lower() for contato in agenda):
        print("Usuário já está cadastrado.")
        return
    agenda.append({"nome": nome, "tipo_telefone": tipo_telefone, "telefone": telefone})

def gravar_agenda(agenda, nome_arquivo="David_Jeiel_De_Araujo_Rocha.txt"):
    with open(nome_arquivo, "w") as arquivo:
        for contato in agenda:
            arquivo.write(f"{contato['nome']},{contato['tipo_telefone']},{contato['telefone']}\n")

def ler_agenda(nome_arquivo="David_Jeiel_De_Araujo_Rocha.txt"):
    agenda = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                nome, tipo_telefone, telefone = linha.strip().split(",")
                agenda.append({"nome": nome, "tipo_telefone": tipo_telefone, "telefone": telefone})
    return agenda

def ordenar_agenda(agenda):
    agenda.sort(key=lambda contato: contato["nome"].lower())

def buscar_contato(agenda, nome):
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            return "Nome cadastrado"
    return "Nome não cadastrado"

def listar_contatos(agenda):
    if not agenda:
        print("A agenda está vazia.")
    else:
        for contato in agenda:
            print(f"Nome: {contato['nome']}, Tipo de Telefone: {contato['tipo_telefone']}, Telefone: {contato['telefone']}")

def main():
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
