def saveContact(contact):
    """
    Salva um contato no arquivo "contacts.txt".

    Args:
        contact (dict): Um dicionário contendo as informações do contato.

    """
    # Abre o arquivo "contacts.txt" em modo de adição (append) para escrever o novo contato
    with open("contacts.txt", mode="a+", encoding='utf-8') as file:
        # Escreve os dados do contato no arquivo em formato CSV
        file.write(
            str("{0},{1},{2},{3},{4},{5}\n".format(contact["cpf"], contact["name"], contact["phone"], contact["email"],
                                                   contact["twitter"], contact["instagram"])))
        file.close()


def updateContactList(list):
    """
    Atualiza o arquivo "contacts.txt" com a lista de contatos fornecida.

    Args:
        list (list): Uma lista de dicionários contendo os contatos.

    """
    # Abre o arquivo "contacts.txt" em modo de escrita (write) para reescrever todos os contatos
    with open("contacts.txt", mode="w+", encoding='utf-8') as file:
        # Itera sobre a lista de contatos e escreve cada um no arquivo em formato CSV
        for contact in list:
            file.write(
                f'{contact["cpf"]},{contact["name"]},{contact["phone"]},{contact["email"]},{contact["twitter"]},{contact["instagram"]}\n')
        file.close()


def loadContacts():
    """
    Carrega os contatos do arquivo "contacts.txt" e retorna uma lista de dicionários.

    Returns:
        list: Uma lista de dicionários contendo os contatos carregados.

    """
    # Abre o arquivo "contacts.txt" em modo de leitura (read)
    with open("contacts.txt", "r") as file:
        list = []
        # Itera sobre cada linha do arquivo
        for line in file.readlines():
            # Separa os campos da linha usando a vírgula como delimitador e cria um dicionário para cada contato
            column = line.strip().split(",")
            contact = {
                "cpf": column[0],
                "name": column[1],
                "phone": column[2],
                "email": column[3],
                "twitter": column[4],
                "instagram": column[5]
            }
            list.append(contact)
    file.close()
    return list


# Função para criar dados de teste caso o arquivo "contacts.txt" esteja vazio
def createTestData():
    """
    Cria dados de teste se o arquivo "contacts.txt" estiver vazio.

    """
    list = []
    try:
        # Tenta carregar os contatos do arquivo
        list = loadContacts()
        # Se não houver contatos, adiciona um contato de teste
        if len(list) == 0:
            raise
    except:
        print("Test new data")
        # Abre o arquivo "contacts.txt" em modo de adição (append) para adicionar um contato de teste
        file = open("contacts.txt", "a+")
        contact = {
            "cpf": "11111111111",
            "name": "David",
            "phone": "11 11111 1111",
            "email": "david@gmail.com",
            "twitter": "@david",
            "instagram": "@instadavid"
        }
        # Escreve os dados do contato de teste no arquivo
        file.write(str("{},{},{},{},{},{}\n".format(contact["cpf"], contact["name"], contact["phone"], contact["email"],
                                                    contact["twitter"], contact["instagram"])))
        list.append(contact)
        file.close()


def cpfRegistered(list, cpf):
    """
    Verifica se um CPF está registrado na lista de contatos.

    Args:
        list (list): Uma lista de dicionários contendo os contatos.
        cpf (str): O CPF a ser verificado.

    Returns:
        bool: True se o CPF estiver registrado, False caso contrário.

    """
    if len(list) > 0:
        for contact in list:
            if contact["cpf"] == cpf:
                return True
    return False


def add():
    """
    Adiciona um novo contato à lista de contatos.

    """
    list = loadContacts()
    cpf_input = input("Enter the CPF without symbols or spaces: ")
    if cpfRegistered(list, cpf_input):
        print('This CPF is registered in the agenda')
    else:
        contact = {
            "cpf": cpf_input,
            "name": input("Enter the name: "),
            "phone": input("Enter the phone: "),
            "email": input("Enter the email: "),
            "twitter": input("Enter the Twitter: "),
            "instagram": input("Enter the Instagram: ")
        }
        saveContact(contact)
        print("The contact {} was registered\n".format(contact["name"]))


def createRegistrationDictionary(list):
    """
    Cria um novo dicionário de contato com base nas informações inseridas pelo usuário.

    Args:
        list (list): Uma lista de dicionários contendo os contatos.

    Returns:
        dict: Um dicionário contendo as informações do novo contato, ou None se o CPF já estiver registrado.

    """
    cpf_input = input("Enter the CPF without symbols or spaces: ")
    if cpfRegistered(list, cpf_input):
        print(f'The CPF {cpf_input} is registered in the agenda')
        return None
    else:
        contact = {
            "cpf": cpf_input,
            "name": input("Enter the name: "),
            "phone": input("Enter the phone: "),
            "email": input("Enter the email: "),
            "twitter": input("Enter the Twitter: "),
            "instagram": input("Enter the Instagram: ")
        }
        return contact


def saveContacts():
    """
    Salva múltiplos contatos na lista de contatos.

    """
    quantity = int(input("How many contacts will be inserted?"))
    inclusion_list = []
    list = loadContacts()
    if quantity >= 2:
        i = 1
        while i <= quantity:
            print("")
            print(f'Registration {i}')
            print("")
            registration_contact = createRegistrationDictionary(list)
            inclusion_list.append(registration_contact)
            i += 1
        added_list = list + inclusion_list
        updateContactList(added_list)
    else:
        print("Please enter a quantity greater than or equal to 2")


def change():
    """
    Altera as informações de um contato existente.

    """
    list = loadContacts()
    if len(list) > 0:
        cpf = input("Enter the CPF without symbols or spaces: ")
        if cpfRegistered(list, cpf):
            for line in list:
                if line["cpf"] == cpf:
                    new_data = {
                        "name": input("Enter the new contact name: "),
                        "phone": input("Enter the new contact phone: "),
                        "email": input("Enter the new contact email: "),
                        "twitter": input("Enter the new contact twitter: "),
                        "instagram": input("Enter the new contact instagram: ")
                    }
                    line["name"] = new_data["name"]
                    line["phone"] = new_data["phone"]
                    line['email'] = new_data["email"]
                    line['twitter'] = new_data["twitter"]
                    line['instagram'] = new_data["instagram"]

            saveContacts(list)
            print('Change made successfully')
            print('')
        else:
            print("There is no contact with the CPF {}. \n".format(cpf))
    else:
        print("There is no contact as the informed CPF.\n")


def search():
    """
    Pesquisa um contato pelo nome e exibe suas informações.

    """
    list = loadContacts()
    name = input('Enter the contact name: ')
    for contact in list:
        registration_data = {}
        if name == contact["name"]:
            registration_data = {
                "name": contact["name"],
                "cpf": contact["cpf"],
                "phone": contact["phone"],
                "email": contact["email"],
                "twitter": contact["twitter"],
                "instagram": contact["instagram"]
            }

    if len(registration_data) == 0:
        print("Contact not found")
        print('')
    else:
        print('')
        print(f'Name      {registration_data["name"]}')
        print(f'CPF       {registration_data["cpf"]}')
        print(f'Phone     {registration_data["phone"]}')
        print(f'E-mail    {registration_data["email"]}')
        print(f'Twitter   {registration_data["twitter"]}')
        print(f'Instagram {registration_data["instagram"]}')
        print('')
        print('')


def list():
    """
    Lista todos os contatos registrados no arquivo "contacts.txt".

    """
    list = []
    list = loadContacts()
    if len(list) > 0:
        for i, contact in enumerate(list):
            print("Contact {}: ".format(i + 1))
            print("\tName: {}".format(contact["name"]))
            print("\tCPF: {}".format(contact["cpf"]))
            print("\tPhone: {}".format(contact["phone"]))
            print("\tEmail: {}".format(contact["email"]))
            print("\tTwitter: {}".format(contact["twitter"]))
            print("\tInstagram: {}".format(contact["instagram"]))

        print("Total contacts: {}\n".format(len(list)))
    else:
        print("There is no contact registered in the system.\n")


def report():
    """
    Gera um relatório mostrando os CPFs, nomes, e-mails, twitters e instagrams de todos os contatos registrados.

    """
    list = []
    list = loadContacts()
    if len(list) > 0:
        print("{:<15} {:<40} {:<30} {:<15} {:<15}".format('CPF', 'NAME', 'EMAIL', 'TWITTER', 'INSTAGRAM'))
        for i, contact in enumerate(list):
            print("{:<15} {:<40} {:<30} {:<15} {:<15}".format(contact["cpf"], contact["name"], contact["email"],
                                                              contact["twitter"], contact["instagram"]))
        print("Total contacts: {}\n".format(len(list)))
    else:
        print("There is no contact registered in the system.\n")


def remove():
    """
    Remove um contato existente da lista de contatos.

    """
    list = []
    list = loadContacts()
    if len(list) > 0:
        cpf = input("Enter the CPF without symbols or spaces: ")
        for i, contact in enumerate(list):
            if contact["cpf"] == cpf:
                print("Contact{}:".format(i + 1))
                print("Name: {}".format(contact["name"]))
                print("CPF: {}".format(contact["cpf"]))
                print("Phone: {}".format(contact["phone"]))
                print("Email: {}".format(contact["email"]))
                print("Twitter: {}".format(contact["twitter"]))
                print("Instagram: {}".format(contact["instagram"]))
                print(" ")
                print("Please answer only 'yes' or 'no'")
                question = input("Confirm the contact deletion? ")
                print("")
                if question == "yes":
                    list.pop(i)
                    saveContacts(list)
                    print("Contact deleted successfully!")
                    print("")
                elif question == "no":
                    print("Contact deletion canceled!")
                    print("")


def exit():
    """
    Função de saída.

    """
    pass


def mainMenu():
    """
    Menu principal do programa.

    """
    createTestData()
    while True:
        print("CONTACT AGENDA")
        print("1 - Add contact")
        print("2 - Edit contact")
        print("3 - Search contact")
        print("4 - List contacts")
        print("5 - Generate report")
        print("6 - Remove contact")
        print("7 - Exit")
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                print(" CONTACT REGISTRATION ")
                add()
            elif option == 2:
                print(" CONTACT EDITION ")
                change()
            elif option == 3:
                print(" CONTACT SEARCH ")
                search()
            elif option == 4:
                print(" CONTACT LISTING ")
                list()
            elif option == 5:
                print("REPORT")
                report()
            elif option == 6:
                print(" CONTACT REMOVAL ")
                remove()
            elif option == 7:
                print(" EXIT THE AGENDA ")
                print("The agenda will be closed, see you soon!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 7.")
        except ValueError:
            print("Invalid option. Please enter a number.")



mainMenu()