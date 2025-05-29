equipamentos = []


def cadastrar_equipamento():
    print('\n === Cadastrar equipamento.')
    print('1 - Notebook')
    print('2 - Tablet')
    print('3 - Celular')

    opcao = input('\n Escolha uma opcao: ')

    if opcao == '1':
        adicionar_notebook()
    elif opcao == '2':
        adicionar_tablet()
    elif opcao == '3':
        adicionar_celular()
    else:
        print('operacao invalida!')

def adicionar_notebook():
    print('\n === Cadastro de Notebook ===')
    marca = input('Digite a marca do notebook: ').upper()
    modelo = input('Digite o modelo do notebook: ').upper()
    serial = int(input('Digite o serial: '))

    if serial_check('Notebook', serial):
        print('Erro, existe um notebook com este serial!')
        return


    novo_notebook = {
        'Tipo': 'Notebook',
        'Marca': marca,
        'Modelo': modelo,
        'Serial': serial
    }


    equipamentos.append(novo_notebook)
    print(f'o Notebook {novo_notebook["Modelo"]} foi cadastrado!')

def adicionar_tablet():

    print('\n === Cadastro de tablet ===')
    marca = input('Digite a marca: ').upper()
    modelo = input('Digite o modelo: ').upper()
    serial = int(input('Digite o serial'))

    if serial_check('Tablet', serial):
        print('Erro, existe um tablet com este serial!')
        return
    
    
    
    novo_tablet = {
        'Tipo': 'Tablet',
        'Marca': marca,
        'Modelo': modelo,
        'Serial': serial
    }

    equipamentos.append(novo_tablet)
    print(f'o Tablet {novo_tablet["Modelo"]} foi cadastrado!')

def serial_check(tipo, serial):
    if any(equipamento['Tipo'] == tipo and equipamento['Serial'] == serial for equipamento in equipamentos):
        return True
    return False

def adicionar_celular():
    print('\n === Cadastro de Celular ===')
    marca = input('Digite a marca do celular: ')
    modelo = input('Digite o modelo do celular: ')
    serial = int(input('Digite o serial: '))
    
    if serial_check('Celular', serial):
        print('Erro, existe um celular com este serial!')
        return

    novo_celular = {
        'Tipo': 'Celular',
        'Marca': marca,
        'Modelo': modelo,
        'Serial': serial
    }

    equipamentos.append(novo_celular)
    print(f'o Celular {novo_celular["Marca"]} foi cadastrado!')




while True :
    print('\n === Menu ===')
    print('1 - Cadastrar Equipamentos')
    print('2 - Listar Equipamentos')
    print('3 - Deletar Equipamento')
    print('4 - Sair')

    menu_option = input('Digite a opcao: ')
    
    if menu_option == '1':
        cadastrar_equipamento()

    elif menu_option == '2':
        print('\n === Mostrar equipamentos ===')
        for equipamento in equipamentos:
            print(f"{equipamento['Tipo']}  {equipamento['Marca']}  {equipamento['Modelo']}  {equipamento['Serial']}");

    elif menu_option =='3':
        print('\n === Digite o serial do equipamento a ser remoido ===')
        serial_remove = int(input('Digite o serial'))
        
        for equipamento in equipamentos:
            if equipamento['Serial'] == serial_remove:
                equipamentos.remove(equipamento)
                print('Equipamento removido.')
                
    elif menu_option == '4':
        exit()

    else:
        print('Escolha uma opcao valida.')

    